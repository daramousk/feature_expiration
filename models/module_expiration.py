# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime
from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT
import logging

logger = logging.getLogger(__name__)

class module_expiration(models.Model):
    _name = 'module.expiration'
    
    module_name = fields.Many2one(comodel_name='ir.module.module', string='Module Name', domain=[('state', '=', 'installed')], required=True)
    expiration_date = fields.Datetime(string='Expiration Date', required=True)





    def check_expired_modules(self):
        for module in self:
            if datetime.strptime(module.expiration_date, DEFAULT_SERVER_DATETIME_FORMAT) > datetime.strptime(fields.Datetime.now(), DEFAULT_SERVER_DATETIME_FORMAT):
                logger.debug('Module ' + module.name + ' has expired. Marking it as readonly.')
                self.mark_module_readonly(module)
        return True
    
    
    def mark_module_readonly(self, module):
        # find all the views declared by this module, make them readonly
        ir_model_data_obj = self.env['ir.model.data']
        model_datas = ir_model_data_obj.search([('module', '=', module.name)])
        
        for model_data in model_datas:
            if model_data.model == 'ir.model.fields':
                self.env[model_data.model].browse(model_data.res_id).readonly = True
    
    
    
