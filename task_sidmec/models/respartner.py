from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
import re

class ResPartner(models.Model):
    _inherit = "res.partner"

    gst_value = fields.Char("GST No.")

    customer_code = fields.Char("Customer Code", default="New", readonly=True)

    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)

    @api.constrains('gst_value')
    def _check_gstnum(self):
        for record in self:
            if record.gst_value and len(record.gst_value) == 15:
                gts_pattern = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$'
                if not re.match(gts_pattern, record.gst_value):
                    raise ValidationError("Please enter a valid GST Number.")
            else:
                raise ValidationError("Please enter a valid GST Number.")

    @api.depends('dob')
    def _compute_age(self):
            today = date.today()
            for rec in self:
                if rec.dob:
                    born = rec.dob
                    ages = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
                    rec.age = ages
                else:
                    rec.age = 0

    @api.model
    def create(self, vals):
        vals["customer_code"] = self.env['ir.sequence'].next_by_code('res.partner')
        return super(ResPartner, self).create(vals)
