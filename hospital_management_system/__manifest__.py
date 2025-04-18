{
    "name":"Hospital Management System",
    "author":"Sri Sathya",
    "version":"18.0",
    "depends":["sale","sale_management","mail",],
    "data":[
        "security/ir.model.access.csv",
        "views/view_patient.xml",
        "views/view_doctor.xml",
        "views/view_sale_order.xml",
        "views/view_patient_lines.xml",
        "data/patient_confirm_mail.xml",
        "wizard/patient_wizard_invoices.xml",
        "report/report_patient_template.xml",
        "report/report.xml",
        "views/menu.xml",
    ],
    #"application":True,
}