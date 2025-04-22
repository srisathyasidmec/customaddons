from odoo import models
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def unlink(self):
        for order in self:
            if order.state in ['sale'] and order.state not in ['draft', 'cancel']:
                raise UserError("You cannot delete a Sales Order that is not in Draft or Canceled state.")
        return super(SaleOrder, self).unlink()
