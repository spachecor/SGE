from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Gestión de Autores'

    name = fields.Char(string='Nombre', required=True, index=True)
    biography = fields.Text(string='Biografía')
