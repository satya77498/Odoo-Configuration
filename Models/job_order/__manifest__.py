# -*- coding: utf-8 -*-

{
    "name": "Job order",
    'version': '14.0',
    "author": "BizzmanWeb",
    "website": "",
    'images': [],
    'summary': "Module helps us to check BOM product quantity before ordering sales",
    'category': 'Manufacturing',
    "depends": ['sale', 'stock', 'account', 'report_xlsx'],
    "license": "LGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/job_order.xml",
        "views/conversion_unit.xml",
        "wizard/expenditure_ledger.xml",
        "wizard/message1.xml",
        "report/report.xml",
        "report/report_excel.xml",
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}