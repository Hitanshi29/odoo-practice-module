from odoo import models,fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    sale_order_count = fields.Integer()
    customer_code = fields.Integer()