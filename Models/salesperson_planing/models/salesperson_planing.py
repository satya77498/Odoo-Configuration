from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr

import math
import base64


class SalesPersonPlaning(models.Model):
    _name = 'salesperson.planing'
    _description = "salesperson_planing"


class SalesPersonEmployee(models.Model):
    _name = 'salesperson.employee'
    _description = "salesperson_employee"

    employee = fields.Char(string="Employee Name")
    color = fields.Char('Color Index')


class SalesPersonLocation(models.Model):
    _name = 'salesperson.location'
    _description = "salesperson_location"

    location = fields.Char(string="Location")
    street = fields.Char(string="Street")
    street1 = fields.Char(string="Street1")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    country = fields.Char(string="Country")
    zip = fields.Char(string="Zip")


class SalesPersonRole(models.Model):
    _name = 'salesperson.role'
    _description = "salesperson_role"

    choose_role = fields.Char(string="Your Role")
    employee = fields.Many2many('salesperson.employee', string="Employee Name")

    appointment_date = fields.Date(string="Appointment Date")
    appointment_end_date = fields.Date(string="Appointment End Date")

    color = fields.Char('Color Index')

    # # State/Status Bar-
    # def action_new(self):
    #     for rec in self:
    #         rec.state = "new"
    #
    # def action_progress(self):
    #     for rec in self:
    #         rec.state = "progress"
    #
    # def action_close(self):
    #     for rec in self:
    #         rec.state = "close"
    #
    # state = fields.Selection([
    #     ('new', 'New'),
    #     ('progress', 'Progress'),
    #     ('close', 'Close'),
    #
    # ], string='Status', readonly=True, default='new')
