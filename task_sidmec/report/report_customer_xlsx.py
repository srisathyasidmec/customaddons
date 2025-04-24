from odoo import models

class ReportCustomerXlsx(models.AbstractModel):
    _name = 'report.task_sidmec.report_customer_report_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size':14,'align':'center','bold':True})
        format2 = workbook.add_format({'font_size':10,'align':'center',})

        sheet = workbook.add_worksheet("Customer Report")
        sheet.write(0,0,'Name',format1)
        # sheet.write(0,1,'Partner Name',format1)
        sheet.write(0,1,'Age',format1)
        sheet.write(0,2,'Dob',format1)
        sheet.write(0,3,'Email',format1)

        sheet.write(1,0,lines.name,format2)
        # sheet.write(1,1,lines.partner_name,format2)
        sheet.write(1,1,lines.age,format2)
        sheet.write(1,2,lines.dob,format2)
        sheet.write(1,3,lines.email,format2)