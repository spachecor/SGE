from odoo import models, fields

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Gestión de Préstamos'
    _order = 'loan_date desc'

    user_id = fields.Many2one('library.user', string='Usuario', required=True, index=True)
    book_id = fields.Many2one('library.book', string='Libro', required=True, index=True)
    loan_date = fields.Date(string='Fecha de Préstamo', default=fields.Date.today)
    return_date = fields.Date(string='Fecha de Devolución')
    status = fields.Selection([
        ('pending', 'Pendiente'),
        ('returned', 'Devuelto'),
        ('overdue', 'Atrasado'),
    ], string='Estado', default='pending')

