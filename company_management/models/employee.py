from odoo import models, fields

class CompanyEmployee(models.Model):
    _name = "company.employee"

    employee_name=fields.Char(string="Name")
    experience=fields.Integer(string="Experience")