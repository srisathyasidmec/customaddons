from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_name = fields.Char("Customer Name")