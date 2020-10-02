# -*- coding: utf-8 -*-
from datetime import datetime as dt, timedelta
from odoo import models, fields, api

class Person(models.Model):
    _name = 'testmodule.person'
    _description = 'Custom persons model'

    first_name = fields.Char(required=True, string='First Name')
    last_name = fields.Char(required=True, string='Last Name')
    full_name = fields.Text(compute='_get_full_name')
    birthday = fields.Date(string='Birth Date')
    age = fields.Integer(compute='_get_age', string='Age')
    sex = fields.Selection([('m', 'male'), ('f', 'female')], string='Sex')
    company_id = fields.Many2one(required=True, comodel_name='res.company',
                                 ondelete='cascade', string='Working company')

    @api.depends('first_name', 'last_name')
    def _get_full_name(self):
        if self.first_name is not False and self.last_name is not False:
            self.full_name = f'{self.first_name} {self.last_name}'
        else:
            self.full_name = ''

    @api.depends('birthday')
    def _get_age(self):
        if self.birthday is not False:
            self.age = (dt.today().date() - dt.strptime(str(self.birthday), '%Y-%m-%d').date()) // timedelta(days=365)
        else:
            self.age = 0

# class testmodule(models.Model):
#     _name = 'testmodule.testmodule'
#     _description = 'testmodule.testmodule'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
