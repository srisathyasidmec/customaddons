from odoo import models, fields, api
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _rec_name = "patient_name"
    _inherit = ['mail.thread', 'mail.activity.mixin']  # inherits in this DB

    patient_name = fields.Char(string="Patient Name")
    age = fields.Integer(string="Age")
    address = fields.Char(String="Address")

    patient_email = fields.Char(string="Patient Email")

    patient_doctor = fields.Many2one(comodel_name="hospital.doctor", domain=[("email", "!=", False)],
                                     string="Doctor Name", tracking=True, required=True, )
    # comodel_name is used as target model this field connects to
    # domain helps in filtering & shows doctors whose mail is present

    doctor_mail = fields.Char(related="patient_doctor.email", string="Doctor email")  # compute="compute_doctor_email"

    patient_id = fields.Many2one(comodel_name="res.partner", string="PId from Partner", tracking=True, required=True, )

    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender")
    # left value stores in Db and right value shows in Odoo UI

    admit_date = fields.Date("Admit date")  # adds date total calendar
    is_patient_is_discharged = fields.Boolean("is patient is discharged")
    # boolean is like checkbox. If ticks acts as True else False
    discharge_date = fields.Date("discharge Date")

    # #parameter is not needed in doctor_mail field
    # @api.onchange("patient_doctor")  #this will display when we change the patient_doctor field , after changing it adds mail of that doctor
    # def onchange_patient(self):
    #     for rec in self:
    #         print(rec)
    #         rec.doctor_mail = rec.patient_doctor.email   #adds mail from patient_doctor

    # def compute_doctor_email(self):
    #     for rec in self:
    #         rec.doctor_mail = rec.patient_doctor.email

    patient_lines = fields.One2many("hospital.patient.line", "patient", "Order lines")
    # if we add attribute One2Many then Many2One should also be done

    user_id = fields.Many2one("res.users", "user", compute="compute_user_company")
    company_id = fields.Many2one("res.company", "Company", compute="compute_user_company")

    def compute_user_company(self):
        for rec in self:
            rec.user_id = self.env.user
            rec.company_id = self.env.user.company_id.id

    # to add image from module
    image_1920=fields.Binary(string="image")

    def send_email(self):
        # print("Hello")
        for rec in self:
            template = self.env.ref("hospital_management_system.mail_template_patient_confirm")
            template.send_mail(rec.id, force_send=True)

    # this is field used for status bar purpose
    status = fields.Selection([("op", "OP"), ("admit", "Admitted"), ("discharge", "Discharged")], "status",
                              default='op', compute="status_update")

    op_date = fields.Date("OP date")

    # @api.onchange("status")
    def status_update(self):
        for res in self:
            today = date.today()
            if today == res.op_date:
                res.status = "op"
            elif today < res.discharge_date:
                res.status = "admit"
            else:
                res.status = "discharge"
            # print(today)

    # thsi function used as one smart button action
    def view_patient_lines(self):
        self.ensure_one()
        for rec in self:
            return {
                'name': "view patient invoices",
                'view_mode': 'list',
                'res_model': 'hospital.patient.line',
                'domain': [('patient', '=', rec.patient_name)],
                'type': 'ir.actions.act_window',
            }


class HospitalPatientLines(models.Model):
    _name = "hospital.patient.line"

    product_id = fields.Many2one("product.product", "product Name")
    qty = fields.Integer("qty")
    unit_price = fields.Float("Unit price")
    total = fields.Integer("Total Amount")
    patient = fields.Many2one("hospital.patient", "patient")

    @api.onchange("unit_price")
    def total_val(self):
        for rec in self:
            rec.total = rec.qty * rec.unit_price
