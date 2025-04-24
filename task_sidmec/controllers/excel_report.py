# import io
# import xlsxwriter
# from odoo import http
# from odoo.http import request
#
# class ExcelReportController(http.Controller):
#     _inherit = 'report.report_xlsx.abstract'
#
#     @http.route('/excel/customer_report', type='http', auth='user', csrf=False)
#     def download_excel(self, workbook, data, lines):
#         # output = io.BytesIO()
#         # workbook = xlsxwriter.Workbook(output)
#         # worksheet = workbook.add_worksheet("Customers")
#
#         format1 = workbook.add_format({'font_size': 14, 'align': 'center', 'bold': True})
#         format2 = workbook.add_format({'font_size': 10, 'align': 'center', })
#
#         sheet = workbook.add_worksheet("Customer Report")
#         sheet.write(0, 0, 'Name', format1)
#         sheet.write(0, 1, 'Partner Name', format1)
#
#         sheet.write(1, 0, lines.patient_name, format2)
#         sheet.write(1, 1, lines.age, format2)
#
#         # Headers
#         headers = ['Name', 'partner_name', 'DoB', 'Email', 'Age']
#         for col, header in enumerate(headers):
#             worksheet.write(0, col, header)
#
#         # ✅ Correct env usage inside a controller
#         partners = request.env["customer.details"].sudo().search([], limit=100)
#         for row, partner in enumerate(partners, start=1):
#             worksheet.write(row, 0, partner.name)
#             worksheet.write(row, 1, partner.partner_name or '')
#             worksheet.write(row, 2, str(partner.dob) or '')
#             worksheet.write(row, 3, partner.email or '')
#             worksheet.write(row, 4, partner.age or '')
#
#         workbook.close()
#         output.seek(0)
#         filecontent = output.read()
#
#         return request.make_response(
#             filecontent,
#             headers=[
#                 ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
#                 ('Content-Disposition', 'attachment; filename="Customer_Report.xlsx"')
#             ]
#         )
