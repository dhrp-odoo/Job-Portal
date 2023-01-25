# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class JobPositionOffer(models.Model):
    _name = "job.position.offer"
    _description = "This model contains all the offers in a particular job."
    
    name = fields.Many2one("job.portal.users", string="Applicant Name")
    expected_ctc = fields.Integer(string="Expected CTC (LPA)", required=True, copy=False)
    experience = fields.Integer(string="Experience (Years)")
    technical_skills_ids = fields.Many2many("technical.skill.tags", string="Technical Skills")
    job_position_id = fields.Many2one("job.position", string="Company Name")
    date_applied = fields.Date(string="Application Date", default=lambda self: fields.Date.today(), readonly=True)
    status = fields.Selection(string="Status", selection=[('accepted','Accepted'), ('on_process','On Process'), ('refused','Refused')], copy=False, readonly=True)
    
    # Extended functionality of create function
    @api.model
    def create(self, value):
        company_id = self.env['job.position'].browse(value['job_position_id'])
        offer_list = company_id.mapped('offer_ids.name.name')
        name_id = self.env['job.portal.users'].browse(value['name'])
        
        # print('----------')
        # print(company_id)
        # print(offer_list)
        # print(name_id.name)
        
        if name_id.name in offer_list:
            raise UserError("You have already applied to this company, you cannot apply again!!!")
        
        for record in self:
            if 'on_process' in offer_list:
                record.job_position_id.state = 'on_process'

        return super().create(value)
        
     # Functions
    
    def action_accept_btn(self):
        offer_status_list = self.job_position_id.mapped('offer_ids.status')
        
        # print('------------------------------')
        # print(self.job_position_id.no_of_opening)
        # print(offer_status_list.count('accepted'))
        
        if offer_status_list.count('accepted') + 1 == self.job_position_id.no_of_opening:
            for record in self:
                record.job_position_id.state = 'recruitment_accomplished'
                
        if offer_status_list.count('accepted') > self.job_position_id.no_of_opening - 1:
            raise UserError("Openings Requirement Fulfilled.")
         
        for record in self:
            record.status = 'accepted' # Then, This will accept offer where user clicked.
        return True

    def action_onprocess_btn(self):
        for record in self:
            record.status = 'on_process'
            record.job_position_id.state = "on_process"
        return True
    
    def action_refuse_btn(self):
        for record in self:
            record.status = 'refused'
        return True
