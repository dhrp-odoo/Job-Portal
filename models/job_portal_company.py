# -*- coding: utf-8 -*-

from odoo import models, fields

class JobPortalCompany(models.Model):
    _name = "job.portal.company"
    _description = "This model contains all information about companies."
    
    name = fields.Char(string="Name", required=True)
    industry_type_id = fields.Many2one("company.industry.type", string="Industry Type")
    description = fields.Text(string="Description")
    founded = fields.Date(string="Founded")
    no_of_employees = fields.Integer(string="Number of Employees", required=True)
    headquarter = fields.Many2one("res.country", string="Headquarter")
    company_ceo = fields.Many2one("job.portal.users", string="CEO")
    company_founders = fields.Many2many("job.portal.users", string="Founders")
    our_offices = fields.Many2many("res.country", string="Our Offices")
    image = fields.Binary("Image", attachment=True, store=True)
    
    # Company's all openings //TODO
    # List of all applicants