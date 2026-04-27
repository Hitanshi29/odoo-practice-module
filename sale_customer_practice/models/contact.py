from odoo import models,fields,api
import logging
logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.partner'

    # sale_order_count = fields.Integer()
    custom = fields.Integer()

    # @api.model
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>",vals)
    #         if vals.get('customer_code', 'New') == 'New':
    #             logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>",vals)
    #             vals['customer_code'] = self.env['ir.sequence'].next_by_code(
    #                 'res.partner.customer.code'
    #             ) or 'New'
    #     return super().create(vals)