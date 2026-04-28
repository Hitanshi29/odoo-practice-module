from odoo import models,fields
import logging
logger = logging.getLogger(__name__)

class rescompany(models.Model):
    _inherit = 'res.company'

    check_company = fields.Boolean(string="Company name")

    # logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",check_company)