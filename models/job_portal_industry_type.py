# -*- coding: utf-8 -*-

from odoo import models, fields

class IndustryType(models.Model):
    _name = "company.industry.type"
    _description = "This model contains information about industry type"
    
    name = fields.Char(string="Name", required=True)
    company_ids = fields.One2many('job.portal.company', 'industry_type_id')
    
    _sql_constraints = [('industry_type_unique', 'UNIQUE (name)', 'A type with the same name already exists.')]