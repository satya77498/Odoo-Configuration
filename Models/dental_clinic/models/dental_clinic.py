from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr
from odoo.exceptions import ValidationError

import math
import base64


class DentalClinic(models.Model):
    _name = 'dental.clinic'

    seq_no = fields.Char(string="SEQ NO.", required=True, copy=False, readonly=True, default=lambda self: _('New'))

    prefix = fields.Selection([('mr', 'Mr'),
                               ('ms', 'Ms'),
                               ('mrs', 'Mrs')], string="Prefix")
    name = fields.Char(string="Name" , required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone", required=True)

    age = fields.Integer(string="age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'female'),
        ('other', 'Other')], string="Choose Your Gender", required=True)
        # ('other', 'Other')], string="Choose Your Gender", required=True, compute="set_prefix")

    location = fields.Char(string="Location")
    appointment_date = fields.Date(string="Appointment Date", required=True)
    notes = fields.Text(string="Notes")
    upload_image = fields.Image(string="Upload Image", max_width=100, max_height=100)
    active = fields.Boolean("Active", default=True)

# Warning
    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age <= 5:
                raise ValidationError(('The Age is Incorrect'))
# _____Warning_____

    # # Compute

    # @api.depends('prefix')
    # def set_prefix(self):
    #     for rec in self:
    #         if rec.prefix:
    #             if rec.prefix == 'mr':
    #                 rec.gender = 'male'
    #             else:
    #                 rec.gender = 'female'

    # _____Compute____


    # Notepad
    dental_clinic_notepad = fields.One2many('dental.clinic.notepad', 'dental_clinic_ids', string='Dental clinic Line')

    class DentalClinicNotepad(models.Model):
        _name = 'dental.clinic.notepad'

        issues = fields.Many2one('product.product', string="Issues")
        xyz = fields.Float(string="anything")
        dental_clinic_ids = fields.Many2one('dental.clinic', string="Complain")


    # Sequence No

    @api.model
    def create(self, vals):
        if vals.get('seq_no', _("New")) == _('New'):
            vals['seq_no'] = self.env['ir.sequence'].next_by_code('dental.clinic.seq') or _('New')
        result = super(DentalClinic, self).create(vals)
        return result


    # ___Sequence No___

    # Smart Button
    doc_count = fields.Integer(compute='_compute_attached_docs_count', string='Number of Doc Attached')
    doc_count2 = fields.Integer(compute='_compute_attached_docs_count2', string='Number of Doc Attached')


    def _compute_attached_docs_count(self):
        Attachment = self.env['ir.attachment']
        for project in self:
            project.doc_count = Attachment.search_count([
                '&',
                ('res_model', '=', 'land.expenditure'), ('res_id', '=', self.id),
            ])


    def _compute_attached_docs_count2(self):
        Attachment = self.env['ir.attachment']
        for project in self:
            project.doc_count2 = Attachment.search_count([
                '&',
                ('res_model', '=', 'land.expenditure'), ('res_id', '=', self.id),
            ])


    # Smart Button
    def meeting(self):
        return
    def feedback(self):
        return
    # >.....................

# State/Status Bar

    def action_confirm(self):
        for rec in self:
            rec.state="confirm"
    def action_cancel(self):
        for rec in self:
            rec.state="cancel"
    # def reschedule_appointment(self):
    #     for rec in self:
    #         rec.state="reschedule appointment"

    state = fields.Selection([
            ('draft','Draft'),
            ('confirm','Confirm'),
            ('done', 'Done'),
            ('cancel', 'Cancel'),
        ], string='Status', readonly=True, default='draft')

# _____State/Status Bar_____