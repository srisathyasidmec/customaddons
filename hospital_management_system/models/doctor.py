from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Hospital Doctor"
    _rec_name = "doctor_name"   #used to over-ride the label in the _name field that displays in UI below patient form

    doctor_name = fields.Char(string="Name")
    role = fields.Char(string="Role")
    email = fields.Char(string="Mail Id")
    address = fields.Char(string="Address")

    patient_names = fields.Many2many(comodel_name="hospital.patient", string="Patient Names")