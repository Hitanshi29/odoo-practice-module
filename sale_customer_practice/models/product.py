from odoo import models,fields
import logging
logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'product.template'

    count_product_variant = fields.Integer(string="Product Variant",compute="action_count_product_variant")

    def action_count_product_variant(self):
        for record in self:
            record.count_product_variant = len(record.product_variant_ids)