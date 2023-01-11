# -*- coding: utf-8 -*-

{
    'name': 'Job Portal',
    'description': 'Job Portal : Create A Better Future For Yourself',
    'version': '1.0',
    'category': 'Services',
    'author': 'Dhrutik Patel (dhrp)',
    'website': 'https://www.odoo.com/',
    'summary': 'Job Portal : Create A Better Future For Yourself',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/job_position_views.xml',
        'views/job_seeker_views.xml',
        'views/job_portal_menus.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}