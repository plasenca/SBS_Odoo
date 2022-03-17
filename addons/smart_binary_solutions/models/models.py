# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductsIn(models.Model):
    _name = "products.sbs.db"  # Nombre en base de datos: products_sbs_db
    _description = "Productos de Smart Binary Solutions"

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
    serie = fields.Char(string="Serie", required=True)
    date = fields.Date(string="Fecha", required=True)
    producto_flaw = fields.Text(string="Fallas")
    observation = fields.Text(string="Observaciones")
    client_id = fields.Many2one("client.sbs.db", string="Cliente")
    
class Client(models.Model):
    _name = "client.sbs.db"
    _description = "Clientes de Smart Binary Solutions"
    
    name = fields.Char(string="Razón Social", required=True)
    ruc_dni = fields.Integer(string="RUC/DNI", required=True)
    contact = fields.Char(string="Contacto")
    address = fields.Char(string="Dirección")
    number_phone = fields.Integer(string="Número de Teléfono")
    email = fields.Char(string="Correo Electrónico")
    
    

