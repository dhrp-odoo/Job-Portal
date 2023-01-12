# -*- coding: utf-8 -*-

from odoo import models, fields

class JobSeeker(models.Model):
    _name = "job.seeker"
    _description = "This model contains all information about job seekers."
    
    name = fields.Many2one("job.portal.users", string="Applicant Name", required=True)
    current_ctc = fields.Integer(string="Current CTC (LPA)", required=True, copy=False)
    expected_ctc = fields.Integer(string="Expected CTC (LPA)", required=True, copy=False)
    phone_number = fields.Integer(string="Phone Number", copy=False)
    email = fields.Char(string="Email Address", copy=False)
    age = fields.Integer(string="Age")
    date_of_birth = fields.Date(string="Date of Birth")
    experience = fields.Integer(string="Experience (Years)")
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')])
    city = fields.Char(string="City")
    country = fields.Many2one("res.country", string="Country")
    postcode = fields.Integer(string="Postcode")
    soft_skills_ids = fields.Many2many("soft.skill.tags", string="Soft Skills")
    technical_skills_ids = fields.Many2many("technical.skill.tags", string="Technical Skills")
    education = fields.Text(string="Education")
    description = fields.Text(string="Description")
    last_job_details = fields.Text(string="Last Job Detail")
    