from odoo import fields, models, api, _
from datetime import date

class CustomerReport(models.TransientModel):
    _name = 'customer.invoices.wizard'
    _description = 'customer invoices report'

    name = fields.Many2one("customer.details", "Name")
    age = fields.Integer("Age", compute="change_age")
    email = fields.Char("Email")
    dob = fields.Date("DoB")

    @api.onchange('name')
    def update_details(self):
        for rec in self:
            if rec.name:
                rec.dob = rec.name.dob
                rec.email = rec.name.email
                rec.age = rec.name.age

    @api.depends("dob")
    def change_age(self):
        for rec in self:
            if rec.dob:
                today = date.today()
                born = rec.dob
                rec.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            else:
                rec.age = 0

    def view_pdf_report(self):
        for rec in self:
            rec.name.dob = rec.dob
            rec.name.email = rec.email
            rec.name.age = rec.age
            rec.name.status = 'confirmed'