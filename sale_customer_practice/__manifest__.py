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
        'views/contact_view.xml'
    ],
    'sequence': 1,
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}