from odoo import models,fields,api
import logging
logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.partner'

    count_sale_order = fields.Integer(string="Count Sale Order", compute="_compute_count_sale_order")
    
    @api.depends('sale_order_ids')
    def _compute_count_sale_order(self):
        for rec in self:
            rec.count_sale_order = len(rec.sale_order_ids)

    custom = fields.Char(string="Custom", default='New', readonly=True)

    @api.model
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('custom', 'New') == 'New':
                vals['custom'] = self.env['ir.sequence'].next_by_code('res.partner') or 'New'
            result = super(ResUsers, self).create(vals)
            logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",result)
            return result