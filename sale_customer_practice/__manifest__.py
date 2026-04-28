# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Bizople Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.
{
    'name': 'Sale Customer Practice',
    'version': '1.0',
    'author': 'Bizople Solutions Pvt. Ltd.',
    'website': 'https://www.bizople.com',
    'summary': '',
    'description': "",
    'depends': ['sale_management','contacts'],
    'data': [
        'data/sequence.xml',
        'Report/account_inherit.xml',
        'Report/sale_order_invoice.xml',
        'views/contact_view.xml',
        'views/product_view.xml',
        'views/sale_order_line_view.xml',
        'views/res_config_settings_inherited_view.xml',
        'views/menu.xml',
    ],
    'sequence': 1,
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}