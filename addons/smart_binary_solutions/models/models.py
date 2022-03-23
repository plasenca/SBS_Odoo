# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductsIn(models.Model):
    _name = "products.sbs.db"  # Nombre en base de datos: products_sbs_db
    _description = "Productos de Smart Binary Solutions"
    _inherit = "mail.thread" # Para que se pueda usar el método de seguimiento de Odoo

    
    # Valores del Cliente
    name_client = fields.Char(string="Razón Social", required=True)
    ruc_dni = fields.Char(string="RUC/DNI", required=True)
    contact = fields.Char(string="Contacto")
    address = fields.Char(string="Dirección", required=True)
    number_phone = fields.Char(string="Número de Teléfono")
    email = fields.Char(string="Correo Electrónico") 
    
    # Valores del Producto
    name = fields.Char(string="Modelo", required=True)
    brand = fields.Selection(
        [
            ('Acer', 'Acer'),
            ('Apple', 'Apple'),
            ('Asus', 'Asus'),
            ('Dell', 'Dell'),
            ('HP', 'HP'),
            ('Lenovo', 'Lenovo'),
            ('MSI', 'MSI'),
            ('Samsung', 'Samsung'),
            ('Sony', 'Sony'),
            ('Toshiba', 'Toshiba'),
            ('Epson', 'Epson'),
            ('Canon', 'Canon'),
            ('Wester Digital', 'Wester Digital'),
            ('Segeate', 'Segeate'),
            ('Philips', 'Philips'),
            ('AOC', 'AOC'),
            ('Varios', 'Varios'),
        ]
        , string="Marca", required=True)
    serie = fields.Char(string="Serie", required=True)
    date = fields.Date(string="Fecha", required=True)
    producto_flaw = fields.Html(string="Fallas")
    observation = fields.Html(string="Observaciones")
    # Referencias
    user_id = fields.Many2one('res.users', string="Usuario", default=lambda self: self.env.user.id)
    category_id = fields.Many2one("sa.category", string="Categoría")
    
    # @api.model
    # def action_salida(self):
    #     for rec in self:
    #         rec.write({'state': 'done'})
    
    
class Users(models.Model):
    _inherit = "res.users"
    
    products_id_user = fields.One2many("products.sbs.db", "user_id")    
    
    def mi_cuenta(self):
        return{
            "type": "ir.actions.act_window",
            "name": "Mi Cuenta",
            "res_model": "res.users",
            "res_id": self.env.user.id,
            "target": "self",
            "views":[(False,"form")]
        }

class Category(models.Model):
    _name = "sa.category"
    _description = "Categoria"
    
    name = fields.Char("Nombre")
    

