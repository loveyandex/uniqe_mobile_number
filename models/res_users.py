# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    dd=fields.Char("dd")
    
    _sql_constraints = [
        ('cne_unique', 'unique(mobile)', 'mobile number already exists!')
    ]


