from odoo import models,fields
import logging
logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'product.template'

    product_variant_count = fields.Integer(string="Product Variant")