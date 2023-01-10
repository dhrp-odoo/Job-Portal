# -*- coding: utf-8 -*-

from odoo import models, fields

class JobPosition(models.Model):
    _name = "job.position"
    _description = "This model contains all information about available jobs."
    
    # company_name_id = fields.Many2one("", string="Company Name", required=True)
    experience_required = fields.Integer(string="Experience Required (Years)", required=True)
    job_position = fields.Char(string="Job Position", required=True)
    no_of_opening = fields.Integer(string="Openings")
    # job_applicant_ids = fields.Many2many("res.users", string="Job Applicants")
    ctc = fields.Integer(string="CTC (LPA)", required=True, copy=False)
    job_description = fields.Text(string="Job Description")
    job_benefit = fields.Text(string="Job Benefits")
    # industry_type_id = fields.Many2one("", string="Industry Type", required=True)
    # employment_type_id = fields.Many2one("", string="Employment Type", required=True)
    education_required = fields.Char(string="Education Required")
    # technical_skills_ids = fields.Many2many(string="Skills Required", required=True)
    company_address = fields.Text(string="Address", copy=False)
    company_email = fields.Char(string="Email Address", required=True, copy=False)
    company_contact_no = fields.Integer(string="Contact Number", required=True, copy=False)
    # company_recruiter_name_id = fields.Many2one("res.users", string="Recruiter Name")
    # soft_skills_ids = fields.Many2many("", string="Soft Skills Required")
    job_posted_date = fields.Date(string="Job Posted", default=lambda self: fields.Date.today(), copy=False)