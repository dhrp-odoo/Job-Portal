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
        'views/job_portal_user_views.xml',
        'views/technical_skill_tags_views.xml',
        'views/soft_skill_tags_views.xml',
        'views/job_portal_industry_type_views.xml',
        'views/job_portal_employment_type_views.xml',
        'views/job_portal_company_views.xml',
        'views/job_position_views.xml',
        'views/job_seeker_views.xml',
        'views/job_portal_menus.xml',
    ],
    'demo': [
        'demo/job_portal_industry_type_demo.xml',
        'demo/job_portal_employment_type_demo.xml',
        'demo/technical_skill_tags_demo.xml',
        'demo/soft_skill_tags_demo.xml',
        'demo/job_portal_users_demo.xml',
        'demo/job_portal_companies_demo.xml',
        'demo/job_seeker_demo.xml',
        'demo/job_position_demo.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}