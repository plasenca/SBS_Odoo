# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class smart_binary_solutions(models.Model):
#     _name = 'smart_binary_solutions.smart_binary_solutions'
#     _description = 'smart_binary_solutions.smart_binary_solutions'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
