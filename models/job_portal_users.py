# -*- coding: utf-8 -*-

from odoo import models, fields

class JobPortalUsers(models.Model):
    _name = "job.portal.users"
    _description = "This model contains all information about job portal users."
    
    name = fields.Char(string="Name", required=True)    
    age = fields.Integer(string="Age")
    phone_number = fields.Integer(string="Phone")
    email_address = fields.Char(string="Email")
    language = fields.Many2one("res.lang", string="Language")