# -*- coding: utf-8 -*-

from odoo import models, fields, api


class charges(models.Model):
    _name = 'hotel.charges'
    _description = 'hotel charges master list'

    name = fields.Char("Charge Name")
    description = fields.Char("Charge Description")
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

