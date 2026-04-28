

from odoo import models,fields

class resconfigsettings(models.TransientModel):
    _inherit = 'res.config.settings'

    name_company = fields.Boolean(string="Company name",related='company_id.check_company',readonly=False)
