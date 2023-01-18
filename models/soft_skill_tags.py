# -*- coding: utf-8 -*-

from odoo import models, fields

class SoftSkillTags(models.Model):
    _name = "soft.skill.tags"
    _description = "This model contains all soft skills tags."
    
    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color Index")
    
    _sql_constraints = [('soft_skill_unique', 'UNIQUE (name)', 'A soft skill with the same name already exists.')]