# -*- coding: utf-8 -*-
{
    'name': "Fancy LiveChat",

    'summary': """
        Improve Odoo default livechat""",

    'description': """
        Improve visual of Odoo default livechat for Clients and Suppliers
    """,

    'author': "Moldeo Interactive",
    'website': "https://www.moldeointeractive.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'im_livechat'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
