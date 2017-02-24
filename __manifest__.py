# -*- coding: utf-8 -*-
{
    'name': "Feature Expiration",

    'summary': """
        Set expiration dates for your modules""",

    'description': """
        This module will give you (the developer) the opportunity to set expiration dates on your modules.
    """,

    'author': "George Daramouskas",
    'website': "https://gr.linkedin.com/in/georgedaramouskas",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/settings.xml',
        'data/cron_jobs.xml',
    ],
    'application':True,
    
}