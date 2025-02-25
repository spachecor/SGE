from odoo import models, fields

class LibraryUser(models.Model):
    _name = 'library.user'
    _description = 'Gestión de Usuarios de la Biblioteca'
    _order = 'registration_date desc'
    _rec_name = 'full_name'  # Esto hace que Odoo use 'full_name' en lugar de 'name'

    full_name = fields.Char(string='Nombre Completo', required=True)
    email = fields.Char(string='Correo Electrónico', index=True)
    phone = fields.Char(string='Teléfono', index=True)
    registration_date = fields.Date(string='Fecha de Registro', default=fields.Date.today)
