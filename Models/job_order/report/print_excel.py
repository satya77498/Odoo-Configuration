from odoo import models
import datetime

class JobOrderExcel(models.AbstractModel):
    _name = "report.job_order.job_order_excel_id"
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, joborder):
        for obj in joborder:
            report_name = obj.name
            sheet = workbook.add_worksheet (report_name[:31])
            bold = workbook.add_format ({'bold': True})
            sheet.write(0, 0, obj.name, bold)

