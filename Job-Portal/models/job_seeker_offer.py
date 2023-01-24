# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class JobSeekerOffer(models.Model):
    _name = "job.seeker.offer"
    _description = "This model contains all the offers for a particular user."
    
    company_name_id = fields.Many2one("job.portal.company", string="Company Name", required=True)
    ctc_offer = fields.Integer(string="CTC Offers (LPA)", required=True, copy=False)
    job_position_id = fields.Many2one("job.seeker", string="Name",required=True)
    job_position = fields.Char(string="Job Position", required=True)
    industry_type_id = fields.Many2one("company.industry.type", string="Industry Type", required=True)
    employment_type_id = fields.Many2one("job.employment.type", string="Employment Type", required=True)
    offer_date = fields.Date(string="Offer Date", default=lambda self: fields.Date.today(), readonly=True)
    status = fields.Selection(string="Status", selection=[('accepted','Accepted'), ('refused','Refused')], copy=False, readonly=True)
    
    # Extended functionality of create function
    @api.model
    def create(self, value):
        
        company_name = self.env['job.portal.company'].browse(value['company_name_id'])
        company_id = self.env['job.seeker'].browse(value['job_position_id'])
        offer_list = company_id.mapped('offer_ids.company_name_id.name')
        
        # print("---------------------------------------------------------------------")
        # print(company_name.name)
        # print(offer_list)
        
        if company_name.name in offer_list:
            raise UserError("You have already offered to this User, you cannot offer again!!!")
        
        return super().create(value)
    
     # Functions
    
    def action_accept_btn(self):
        
        offer_status_list = self.job_position_id.mapped('offer_ids.status')
        # print(offer_status_list)
        
        if 'accepted' in offer_status_list:
            raise UserError("You have already accepted the offer. You cannot accept multiple offers.")
        
        for record in self:
            record.status = 'accepted'
        return True

    def action_refuse_btn(self):
        for record in self:
            record.status = 'refused'
        return True