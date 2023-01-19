# -*- coding: utf-8 -*-

from odoo import models, fields, api

class JobPositionOffer(models.Model):
    _name = "job.position.offer"
    _description = "This model contains all the offers in a particular job."
    
    name = fields.Many2one("job.portal.users", string="Applicant Name")
    expected_ctc = fields.Integer(string="Expected CTC (LPA)", required=True, copy=False)
    experience = fields.Integer(string="Experience (Years)")
    technical_skills_ids = fields.Many2many("technical.skill.tags", string="Technical Skills")
    job_position_id = fields.Many2one("job.position", string="Company Name",required=True)
    date_applied = fields.Date(string="Application Date", default=lambda self: fields.Date.today(), readonly=True)
    status = fields.Selection(string="Status", selection=[('accepted','Accepted'), ('on_process','On Process'), ('refused','Refused')], copy=False, readonly=True)
    
     # Functions
    
    def action_accept_btn(self):
        for record in self:
            record.status = 'accepted' # Then, This will accept offer where user clicked.
            record.job_position_id.state = 'selected'
        return True

    def action_onprocess_btn(self):
        for record in self:
            record.status = 'on_process'
            record.job_position_id.state = 'on_process'
        return True
    
    def action_refuse_btn(self):
        for record in self:
            record.status = 'refused'
        return True
