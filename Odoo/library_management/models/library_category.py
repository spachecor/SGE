from odoo import models, fields

class LibraryCategory(models.Model):
    _name = 'library.category'
    _description = 'Gestión de Categorías'
    _order = 'name'

    name = fields.Char(string='Nombre de la Categoría', required=True, unique=True)
    description = fields.Text(string='Descripción', help="Breve descripción de la categoría.")
