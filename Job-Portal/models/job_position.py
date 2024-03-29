# -*- coding: utf-8 -*-

from odoo import models, fields

class JobPosition(models.Model):
    _name = "job.position"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "This model contains all information about available jobs."
    _rec_name = "company_name_id"

    company_name_id = fields.Many2one("job.portal.company", string="Company Name", required=True)
    industry_type_id = fields.Many2one("company.industry.type", string="Industry Type", required=True)
    ctc = fields.Integer(string="CTC (LPA)", required=True, copy=False)
    experience_required = fields.Integer(string="Experience (Years)", required=True)
    job_position = fields.Char(string="Job Position", required=True)
    no_of_opening = fields.Integer(string="Openings")
    job_posted_date = fields.Date(string="Job Posted", default=lambda self: fields.Date.today(), copy=False)
    job_description = fields.Text(string="Job Description")
    job_benefit = fields.Text(string="Job Benefits")
    employment_type_id = fields.Many2one("job.employment.type", string="Employment Type", required=True)
    education_required = fields.Char(string="Education Required")
    website = fields.Char(string="Website")
    company_address = fields.Text(string="Company's Location", copy=False)
    company_email = fields.Char(string="Recruiter's Email", copy=False)
    company_contact_no = fields.Integer(string=" Recruiter's Phone No.", copy=False)
    company_recruiter_name_id = fields.Many2one("job.portal.users", string="Recruiter Name")
    soft_skills_ids = fields.Many2many("soft.skill.tags", string="Soft Skills")
    technical_skills_ids = fields.Many2many("technical.skill.tags", string="Technical Skills")
    image = fields.Binary("Image", attachment=True, store=True)
    offer_ids = fields.One2many('job.position.offer', 'job_position_id', string="Offers", tracking=True)  
    state = fields.Selection(string="State", readonly=True, required=True, copy=False, selection=[('new', 'New'), ('on_process', 'On Process'), ('recruitment_accomplished', 'Recruitment Accomplished')], default="new", tracking=True)
    