from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.osv import expression
from datetime import date

class CustomerDetails(models.Model):
    _name = "customer.details"
    _rec_name = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("Name")

    partner_name = fields.Many2one("res.partner", string="Partner Name")

    dob = fields.Date("Date of Birth")
    email = fields.Char("Email")

    age=fields.Integer("Age", compute="change_age")

    status = fields.Selection([("pending", "Pending"), ("confirmed", "Confirmed")], "status",
                              default='pending')

    @api.depends("dob")
    def change_age(self):
        for rec in self:
            if rec.dob:
                today = date.today()
                born = rec.dob
                rec.age =  today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            else:
                rec.age = 0

    user_id = fields.Many2one(comodel_name="res.users",String="User", compute="change_ids")
    company_id = fields.Many2one(comodel_name="res.company",String="Company", compute="change_ids")

    def change_ids(self):
        for rec in self:
            rec.user_id = self.env.user
            rec.company_id = self.env.user.company_id.id

    def send_email(self):
        # print("Hello")
        for rec in self:
            template = self.env.ref("task_sidmec.mail_template_customer")
            template.send_mail(rec.id, force_send=True)

    @api.constrains('dob')
    def _check_valid_age(self):
        for rec in self:
            if rec.dob > date.today():
                raise ValidationError("DoB must be entered valid value")

    @api.depends('status')
    def status_update(self):
        for res in self:
            res.status = 'confirmed'

    class ResPartner(models.Model):
        _inherit = 'res.partner'

        @api.model
        def name_search(self, name='', args=None, operator='ilike', limit=100):
            args = []
            domain = []
            if name:
                domain = expression.OR([
                    [('name', operator, name)],
                    [('phone', operator, name)],
                    [('email', operator, name)],
                    [('gst_value', operator, name)],
                ])
            records = self.search(expression.AND([args, domain]), limit=limit)
            return [(rec.id, f"{rec.name}") for rec in self.browse(records.ids)]


class CustomerAccounting(models.Model):
    _inherit = 'account.move'