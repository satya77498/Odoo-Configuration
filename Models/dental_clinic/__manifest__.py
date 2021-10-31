{
    "name": "Dental Clinic",
    "version": '14.0',
    "author": "Me",
    "website": "",
    "images": [],
    "summary": "This Module Helps You To Book Appointment",
    "category": "Human Resources",
    "depends": ['crm'],
    "license": "LGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "data/enter_data.xml",
        "wizards/reschedule_appointment.xml",
        "views/dental_clinic.xml",
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
