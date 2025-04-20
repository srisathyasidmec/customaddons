from odoo import models

class ReportPatientXlsx(models.AbstractModel):
    _name = 'report.hospital_management_system.report_patient_report_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size':14,'align':'center','bold':True})
        format2 = workbook.add_format({'font_size':10,'align':'center',})

        sheet = workbook.add_worksheet("Patient Report")
        sheet.write(0,0,'Patient Name',format1)
        sheet.write(0,1,'Age',format1)
        sheet.write(0,2,'Gender',format1)
        sheet.write(0,3,'Address',format1)
        sheet.write(0,4,'Email Id',format1)
        sheet.write(0,5,'Doctor Name',format1)
        sheet.write(0,6,'Products',format1)
        sheet.write(0,7,'Quantity',format1)
        sheet.write(0,8,'Unit_Price',format1)
        sheet.write(0,9,'Total',format1)

        sheet.write(1,0,lines.patient_name,format2)
        sheet.write(1,1,lines.age,format2)
        sheet.write(1,2,lines.gender,format2)
        sheet.write(1,3,lines.address,format2)
        sheet.write(1,4,lines.patient_email,format2)
        sheet.write(1,5,lines.patient_doctor.doctor_name,format2)

        row = 1  # Start writing from row 1
        for line in lines.patient_lines:
            sheet.write(row, 6, line.product_id.name, format2)
            sheet.write(row, 7, line.qty, format2)
            sheet.write(row, 8, line.unit_price, format2)
            sheet.write(row, 9, line.total, format2)
            row += 1
