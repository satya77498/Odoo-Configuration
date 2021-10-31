from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr

import math
import base64

#    Inherit Sales

class JobOrderInherit(models.Model):
    _inherit = "sale.order"
    job_name = fields.Char(string='Job Name')

#    Inherit Inventory

class InventoryInherit(models.Model):
    _inherit = "product.template"

    uof = fields.Many2one('uom.uom', string='Purchase Unit of Measure')

    # uom_id = fields.Many2one('uom.uom', string='Unit of Measure')
    # uom_po_id = fields.Many2one('uom.uom', string='Purchase Unit of Measure')

    alternative_unit = fields.Many2one('uom.uom',string='Alternative Unit')
    conversion_unit = fields.Many2one('conversion.unit',string='Conversion Unit')

    @api.onchange('uom_id')
    def _onchange_uom_id(self):
        if self.uom_id:
            self.uom_po_id != self.uom_id.id

    @api.onchange('uom_po_id')
    def _onchange_uom(self):
        if self.uom_id and self.uom_po_id and self.uom_id.category_id != self.uom_po_id.category_id:
            self.uom_po_id != self.uom_id

# On change function in job order Doesn't work

    # @api.onchange('name')
    # def onchange_name(self):
    #     if self.name:
    #         if self.name.gender:
    #             self.gender = self.name.gender


class JobOrder(models.Model):
    _name = "job.order"
    _rec_name = "slno"

    slno = fields.Char(string='SL. No', required=True, copy=False, redonly=True, default=lambda self: _('New'))
    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(int='Phone', required=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string="Choose Your Gender",required=True)
    job_company_line = fields.One2many('job.company.line', 'job_company_ids', string="Job Line")
    experience = fields.Selection([('fresher','Fresher'),('experience','Experience')],string="Job Experience")
    language = fields.Many2many('sale.order',string='Language You Know')
    dist= fields.Many2one('sale.order',string="Choose Your Dist")
    notes = fields.Text(string="Notes")
    class JobCompanyLine(models.Model):
        _name = 'job.company.line'

        product_id = fields.Many2one('product.product', string="product")
        qty = fields.Float(string="Quantity")
        job_company_ids = fields.Many2one('job.order', string="Job IDs")

    doc_count = fields.Integer(compute='_compute_attached_docs_count', string='Number of Doc Attached')

    def _compute_attached_docs_count(self):
        Attachment = self.env['ir.attachment']
        for project in self:
            project.doc_count = Attachment.search_count([
                '&',
                ('res_model', '=', 'land.expenditure'), ('res_id','=', self.id),
            ])

    def manage_document(self):
        return
    def delete_document(self):
        return

    @api.model
    def create(self, vals):
        if vals.get('slno', _("New")) == _('New'):
            vals['slno']= self.env['ir.sequence'].next_by_code('job.order.seq') or _('New')
        result=super(JobOrder, self).create(vals)
        return result

    @api.model
    def create_document(self):
        return {
            'name': _('Doc'),
            'type': 'ir.actions.act_window',
            'res_model': 'account.payment',
            'context': {'create': False},
        }


    def confirm_button(self):
        return
    def cancel_button(self):
        return

    state = fields.Selection([
            ('draft','Draft'),
            ('confirm','Confirm'),
            ('done', 'Done'),
            ('cancel', 'Cancel'),
        ], string='Status', readonly=True, default='draft')

