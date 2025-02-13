from odoo import models, fields, api, exceptions
from datetime import timedelta, date

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Gestión de Préstamos'
    _order = 'loan_date desc'

    user_id = fields.Many2one('library.user', string='Usuario', required=True, index=True)
    book_id = fields.Many2one('library.book', string='Libro', required=True, index=True)
    loan_date = fields.Date(string='Fecha de Préstamo', default=fields.Date.today)
    return_date = fields.Date(
        string='Fecha de Devolución',
        default=lambda self: fields.Date.today() + timedelta(days=7)
    )
    status = fields.Selection([
        ('pending', 'Pendiente'),
        ('returned', 'Devuelto'),
        ('overdue', 'Atrasado'),
    ], string='Estado', default='pending')

    @api.model
    def create(self, vals):
        # 1. Verificar si hay copias disponibles
        book = self.env['library.book'].browse(vals['book_id'])
        if book.available_copies < 1:
            raise exceptions.ValidationError('No hay copias disponibles de este libro.')
        
        # 2. Bloquear al usuario si tiene más de 3 libros prestados
        user = self.env['library.user'].browse(vals['user_id'])
        active_loans = self.search_count([
            ('user_id', '=', user.id),
            ('status', '=', 'pending')
        ])
        if active_loans >= 3:
            raise exceptions.ValidationError('El usuario ya tiene 3 libros prestados y no puede pedir más.')

        # 3. Automatizar la fecha de devolución (7 días)
        if not vals.get('return_date'):
            loan_date = date.today()
            return_date = loan_date + timedelta(days=7)
            # Convertir la fecha a string en formato YYYY-MM-DD
            vals['return_date'] = fields.Date.to_string(return_date)
        
        # 4. Reducir copias disponibles
        book.available_copies -= 1
        
        # 5. Crear el registro
        record = super(LibraryLoan, self).create(vals)
        
        # 6. Forzar la escritura para asegurar que se guarde el campo
        record.write({'return_date': vals['return_date']})
        
        return record

    def action_registrar_devolucion(self):
        for record in self:
            if record.status != 'pending':
                raise exceptions.ValidationError('El préstamo ya fue devuelto o está atrasado.')

            # Aumentar copias disponibles
            record.book_id.available_copies += 1
            record.status = 'returned'
