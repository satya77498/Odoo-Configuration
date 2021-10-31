
from odoo import api, fields, models, _

class RescheduleAppointment(models.TransientModel):
    _name = 'reschedule.appointment'

    seq_no = fields.Many2one('dental.clinic', string='Choose Ur No')
    appointment_date = fields.Date(string="Appointment Date", required=True)


