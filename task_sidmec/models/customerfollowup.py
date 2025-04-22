from odoo import models, fields, api
from datetime import date

class CustomerFollowUp(models.Model):
    _name = "customer.followup"
    _rec_name = "salesperson"

    salesperson = fields.Char(string="Sales Person")
    current_date = fields.Date("Current Date")

    @api.model
    def default_get(self, fields_list):
        defaults = super(CustomerFollowUp, self).default_get(fields_list)

        if 'salesperson' in fields_list:
            defaults['salesperson'] = self.env.user.name

        if 'current_date' in fields_list:
            defaults['current_date'] = date.today()

        return defaults