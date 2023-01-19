# -*- coding: utf-8 -*-

from odoo import models, fields, api

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
    
     # Functions
    
    def action_accept_btn(self):
        for record in self:
            record.status = 'accepted'
        return True

    def action_refuse_btn(self):
        for record in self:
            record.status = 'refused'
        return True