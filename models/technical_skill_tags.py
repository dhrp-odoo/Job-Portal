# -*- coding: utf-8 -*-

from odoo import models, fields

class TechnicalSkillTags(models.Model):
    _name = "technical.skill.tags"
    _description = "This model contains all technical languages tags."
    
    name = fields.Char(string="Name", required=True)
    
    _sql_constraints = [('technical_language_unique', 'UNIQUE (name)', 'A language with the same name already exists.')]