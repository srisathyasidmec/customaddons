from odoo import fields, models

class CustomerReport(models.TransientModel):
    _name = 'sales.wizard'
    _description = 'Salesman report Wizard'

    # salesperson = fields.Many2one("res.partner",String="Salesman")
    users = fields.Many2one("res.users",String="Users")
    from_date = fields.Date(String="From_date")
    to_date = fields.Date(String="To_date")

    def view_salesman_report(self):
        for rec in self:
            domain = [('user_id', '=', rec.users.id)]

            if rec.from_date:
                domain.append(('date_order', '>=', rec.from_date))
            if rec.to_date:
                domain.append(('date_order', '<=', rec.to_date))

            sale_orders = self.env["sale.order"].search(domain, limit=10, order='date_order desc')

            total_amount = sum(order.amount_total for order in sale_orders)

            data = {
                'sale_orders': [
                    {
                        'name': order.name,
                        'amount_total': order.amount_total,
                        'customer_name': order.partner_id.name,
                    }
                    for order in sale_orders
                ],
                'wizard': {
                    'partner_name': rec.users.name,
                    'from_date': rec.from_date,
                    'to_date': rec.to_date,
                    'total_amount': total_amount,
                }
            }

            return self.env.ref('task_sidmec.report_wizard_salesperson_pdf').report_action(self, data=data)