from odoo import fields, models


class CustomerReport(models.TransientModel):
    _name = 'sales.wizard'
    _description = 'salesman report'

    salesperson= fields.Many2one("res.partner",String="Salesman")
    from_date= fields.Date(String="From_date")
    to_date= fields.Date(String="to_date")

    def view_salesman_report(self):
        return self.env.ref('task_sidmec.report_wizard_customer_pdf').report_action(self)
        # print("Hello")
        # pass