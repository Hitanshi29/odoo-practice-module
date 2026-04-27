from odoo import models,fields,api
import logging
logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'sale.order'

    # quantity_count_order = fields.Integer(string="Quantity",compute="_compute_quantity_count",store=True)

    # @api.depends('order_line.product_uom_qty')
    # def _compute_quantity_count(self):
    #     self.quantity_count_order = 0
    #     for data in self:
    #         logger.info(">>>>>>>>>>>",data.read())
    #         for order in data.order_line:
    #             logger.info(">>>>>>>>>>>>>>>>>>>>>>",order.product_uom_qty)
    #             self.quantity_count_order += int(order.product_uom_qty)
    #             logger.info(">>>>>>>>>>>>>>>>>>>>>>",self.quantity_count_order)