# -*- coding: utf-8 -*-

from odoo import models, fields

class EmploymentType(models.Model):
    _name = "job.employment.type"
    _description = "This model contains information about job employment type"
    
    name = fields.Char(string="Name", required=True)
    position_ids = fields.One2many('job.position', 'employment_type_id')
    
    _sql_constraints = [('employment_type_unique', 'UNIQUE (name)', 'A employment type with the same name already exists.')]