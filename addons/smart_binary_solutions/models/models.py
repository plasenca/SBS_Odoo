# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductsIn(models.Model):
    _name = "products.sbs.db"  # Nombre en base de datos: products_sbs_db
    _description = "Productos de Smart Binary Solutions"

    _id = fields.id(string="Orden de Entrada")
    name = fields.Char(string="Modelo", required=True)
    brand = fields.Selection(
        [
            ('acer', 'Acer'),
            ('apple', 'Apple'),
            ('asus', 'Asus'),
            ('dell', 'Dell'),
            ('hp', 'HP'),
            ('lenovo', 'Lenovo'),
            ('msi', 'MSI'),
            ('samsung', 'Samsung'),
            ('sony', 'Sony'),
            ('toshiba', 'Toshiba')
        ]
        , string="Marca", required=True)
    product_model = fields.Char(string="Modelo", required=True)
    serie = fields.Char(string="Serie", required=True)
    producto_flaw = fields.Html(string="Fallas")
    observation = fields.Html(string="Observaciones")

class OrderProductIn(models.Models):
    _name = "order.product.sbs.db"
    _description = "Orden de Productos de Smart Binary Solutions"
    
    order_pedido = fields.Integer(string="Orden de pedido", )
    date_order = fields.Date(string="Fecha de pedido")

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
