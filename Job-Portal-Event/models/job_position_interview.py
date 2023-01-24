# -*- coding: utf-8 -*-

from odoo import models, fields, api

class JobPositionInterview(models.Model):
    _inherit = "job.seeker.offer"
    
    # When user apply for specific position, Interview will be scheduled in Calender module.
    @api.model
    def create(self, vals):
        print("----------------- 000 -------------------")
        return super(JobPositionInterview, self).create(vals)
