from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _rec_name = "patient_id"
    _description = "Hospital Appointment Details"
    _inherit = ['mail.thread', 'mail.activity.mixin']  # inherits in this DB

    # patient_name = fields.Char(string="Name")
    patient_id = fields.Many2one("res.partner", "Name", domain=[
        ("email", "!=", False),
    ])
    age = fields.Integer(string="Age")
    patient_email = fields.Char(string="Email", tracking=True)

    date = fields.Date("Date")
    apdate_time = fields.Datetime("Appointmet Date and Time")

    company_id = fields.Many2one("res.company", "Company", compute="compute_user_company")
    user_id = fields.Many2one("res.users", "user", compute="compute_user_company")

    status = fields.Selection([("draft", "Draft"), ("confirmed", "Confirmed")], "status",
                              default='draft')

    appointment_lines = fields.One2many("hospital.appointment.line", "patient", "lines")

    def compute_user_company(self):
        for rec in self:
            rec.user_id = self.env.user
            rec.company_id = self.env.user.company_id.id

    def confirm_appointment(self):
        for rec in self:
            patient = self.env["hospital.patient"].search([('appointment_id', '=', rec.id)])
            if patient:
                raise ValueError("record existed")
            else:
                vals = {
                    'patient_id': rec.patient_id.id,
                    'patient_email': rec.patient_email,
                    'age': rec.age,
                    'op_date': rec.date,
                    'patient_lines': [(0, 0, {
                        'product_id': i.product_id.id,
                        'qty': i.qty,
                        'unit_price': i.unit_price,
                        'total': i.sub_total,

                    }) for i in rec.appointment_lines]

                }
            self.env["hospital.patient"].create(vals)
            rec.status = "confirmed"


    def action_reset_to_draft(self):
        for rec in self:
            if rec.status == "confirmed":
                rec.status = "draft"


    def action_send_email(self):
        template = self.env.ref("hospital_management_system.mail_template_demo_patient_invoice")
        for rec in self:
            if not rec.patient_email:
                raise ValueError("pls add patient email")
            else:
                rec.user_id = self.env.user.id
                template.send_mail(rec.id, force_send=True)

    def view_appointment(self):
        self.ensure_one()
        for rec in self:
            return {
                'name': "view patient",
                'view_mode': 'list',
                'res_model': 'hospital.patient',
                # 'domain': [('patient', '=', rec.patient_name)],
                'type': 'ir.actions.act_window',
            }


class HospitalAppointmentLines(models.Model):
    _name = "hospital.appointment.line"

    product_id = fields.Many2one("product.product", "product Name")
    qty = fields.Integer("qty")
    unit_price = fields.Float("Unit price")
    sub_total = fields.Integer("Sub Total")
    patient = fields.Many2one("hospital.appointment", "patient")

    @api.onchange("unit_price")
    def total_val(self):
        for rec in self:
            rec.sub_total = rec.unit_price * rec.qty
