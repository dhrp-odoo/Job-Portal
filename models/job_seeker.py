# -*- coding: utf-8 -*-

from odoo import models, fields

class JobSeeker(models.Model):
    _name = "job.seeker"
    _description = "This model contains all information about job seekers."
    
    # name = fields.Many2one("res.users", string="Name")
    phone_number = fields.Integer(string="Phone Number")
    email = fields.Char(string="Email Address")
    age = fields.Integer(string="Age")
    date_of_birth = fields.Date(string="Date of Birth")
    experience = fields.Integer(string="Experience (Years)")
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')])
    city = fields.Char(string="City")
    # country = fields.Many2one("res.country", string="Country")
    postcode = fields.Integer(string="Postcode")
    # technical_skills_ids = fields.Many2many(string="Skills Required", required=True)
    # soft_skills_ids = fields.Many2many("", string="Soft Skills Required")
    education = fields.Text(string="Education")
    description = fields.Text(string="Description")
    last_job_details = fields.Text(string="Last Job Detail")