from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date, timedelta, datetime
import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
import tempfile
from odoo.tools.misc import xlwt
import io
import base64
import time
from dateutil.relativedelta import relativedelta
from pytz import timezone
import xlsxwriter


class Expenditure_Ledger1(models.TransientModel):
    _name = "expenditure.ledger1"
    _description = "Expenditure_Ledger1"

    expenditure_ledger1 = fields.Char(string="Expenditure Ledger1")

    start_date = fields.Date("Start Date", default=fields.Date.context_today)
    end_date = fields.Date("End Date", default=fields.Date.context_today)


    def expenditure_excel_report(self):
        dt_start = datetime.datetime.strptime(str(self.start_date), DEFAULT_SERVER_DATE_FORMAT)
        date_start = dt_start.strftime('%d-%m-%Y')
        dt_end = datetime.datetime.strptime(str(self.end_date), DEFAULT_SERVER_DATE_FORMAT)
        date_end = dt_end.strftime('%d-%m-%Y')
        filename = 'Expenditure Ledger From ' + str(date_start) + ' To ' + str(date_end) + '.xls'
        workbook = xlwt.Workbook(encoding="UTF-8")

        worksheet = workbook.add_sheet('B2B')
        text_wrap = xlwt.easyxf('align: wrap on;')
        font = xlwt.Font()
        font.bold = True
        for_left = xlwt.easyxf(
            "font: bold 1, color black; borders: top double, bottom double, left double, right double; align: horiz center")
        for_left_not_bold = xlwt.easyxf("font: color black; align: horiz left")
        for_center_not_bold = xlwt.easyxf("font: color black; align: horiz center")
        for_center_bold = xlwt.easyxf(
            "font: bold 1, color black; align: horiz center")
        GREEN_TABLE_HEADER = xlwt.easyxf(
            'font: bold 1, name Tahoma, height 250;'
            'align: vertical center, horizontal center, wrap on;'
            'borders: top double, bottom double, left double, right double;'
        )
        style = xlwt.easyxf(
            'font:height 400, bold True, name Arial; align: horiz center, vert center;borders: top medium,right medium,bottom medium,left medium')



        alignment = xlwt.Alignment()  # Create Alignment
        alignment.horz = xlwt.Alignment.HORZ_RIGHT
        style = xlwt.easyxf('align: wrap yes')
        style.num_format_str = '0.00'

        worksheet.col(0).width = 6000
        worksheet.col(1).width = 5000
        worksheet.col(2).width = 5000
        worksheet.col(3).width = 5000
        worksheet.col(4).width = 5000
        worksheet.col(5).width = 5000
        worksheet.col(6).width = 5000
        worksheet.col(7).width = 6000
        worksheet.col(8).width = 6000
        worksheet.col(9).width = 5000
        worksheet.col(10).width = 5000

        worksheet.row(2).height = 50

        borders = xlwt.Borders()
        borders.bottom = xlwt.Borders.MEDIUM
        border_style = xlwt.XFStyle()  # Create Style
        border_style.borders = borders
        report_title = 'Expenditure Ledger  From ' + str(date_start) + ' To ' + str(date_end)
        worksheet.write_merge(0, 1, 0, 10, report_title, GREEN_TABLE_HEADER)

        inv_search_ids = self.env['land.expenditure'].search([])

        if not inv_search_ids:
            raise UserError(_('No Expenditure Ledger between Selected Dates.'))

        # worksheet.write_merge(
        #     0, 1, 0, 10, 'Summary For - B2B', GREEN_TABLE_HEADER)

        row = 2
        worksheet.write(row, 0, 'Value-1' or '', for_left)
        worksheet.write(row, 1, 'Value-2' or '', for_left)
        worksheet.write(row, 2, 'Value-3' or '', for_left)
        worksheet.write(row, 3, 'Value-4' or '', for_left)
        worksheet.write(row, 4, 'Value-5' or '', for_left)
        worksheet.write(row, 5, 'Value-6' or '', for_left)
        worksheet.write(row, 6, 'Value-7' or '', for_left)
        worksheet.write(row, 7, 'Value-8' or '', for_left)
        worksheet.write(row, 8, 'Value-9' or '', for_left)
        worksheet.write(row, 9, 'Value-10' or '', for_left)
        worksheet.write(row, 10, 'Value-11' or '', for_left)

        fp = io.BytesIO()
        workbook.save(fp)
        inv_detail_excel_id = self.env['expenditure.ledger.excel.extended1'].create(
            {'excel_file': base64.encodestring(fp.getvalue()), 'file_name': filename})
        fp.close()

        return {
            'view_mode': 'form',
            'res_id': inv_detail_excel_id.id,
            'res_model': 'expenditure.ledger.excel.extended1',
            'view_type': 'form',
            'type': 'ir.actions.act_window',
            'context': self._context,
            'target': 'new',
        }

    class Expenditure_LedgerExcelExtended1(models.Model):
        _name = 'expenditure.ledger.excel.extended1'
        _description = "Expenditure Ledger Excel Extended1"

        excel_file = fields.Binary('Download Report :- ')
        file_name = fields.Char('Excel File', size=64)