from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class ShipmentDocument(models.Model):
    _name = "shipment.document"

    document_code = fields.Char(default="New")
    name = fields.Char(string="Customer Name", copy=False)
    description = fields.Text(string="Description")

    file = fields.Binary(string="add file here")
    file_filename = fields.Text("File Name")

    document_status = fields.Selection([("pending", "Pending"), ("completed", "Completed")], "status",
                              default='pending', compute="status_update")

    @api.model
    def create(self, vals):
        vals["document_code"] = self.env['ir.sequence'].next_by_code('shipment.document')
        return super(ShipmentDocument, self).create(vals)

    @api.constrains('file_filename')
    def _check_pdf_file(self):
        for record in self:
            if record.file_filename and not record.file_filename.lower().endswith('.pdf'):
                raise ValidationError("Only PDF files are allowed.")

    def status_update(self):
        for res in self:
            if res.file:
                res.document_status = "completed"
            else:
                res.document_status = "pending"

    def unlink(self):
        for record in self:
            if record.document_status == 'completed':
                raise UserError("You cannot delete documents for a completed shipment.")
        return super(ShipmentDocument, self).unlink()