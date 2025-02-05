
from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Gestión de Libros'

    title = fields.Char(string='Título', required=True)
    isbn = fields.Char(string='ISBN', required=True, unique=True)
    author_id = fields.Many2one('library.author', string='Autor', required=True)
    category_id = fields.Many2one('library.category', string='Categoría')
    available_copies = fields.Integer(
        string='Copias disponibles',
        default=0,
        help="Número de copias disponibles para préstamo."
    )
