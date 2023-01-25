# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class JobPositionInterview(models.Model):
    _inherit = "job.position.offer"
    
    # When company will click on On-Process btn, Interview will be scheduled in Calender module.

    def action_onprocess_btn(self):
        print('------------------------------------')
        # print(self.name.read())
        company_name = self.env['job.portal.users'].browse(self.name.id)
        # print(self.env['job.portal.users'])
        # print(company_name.name)
        
        print('Interview:' )
        calendar_event = self.env['calendar.event'].create({
            'name': 'Interview: '+ company_name.name,
            'start': fields.Datetime.today() + relativedelta(days=+2, hours=+5),
            'stop': fields.Datetime.today() + relativedelta(days=+2, hours=+8),
            'location': '401 & 402, Floor 4, IT Tower 3 InfoCity Gate, 1, Gandhinagar, Gujarat 382007'
        })
        
        return super().action_onprocess_btn()
