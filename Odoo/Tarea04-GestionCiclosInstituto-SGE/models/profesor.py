from odoo import models, fields

class profesor(models.Model):
    _name = 'gestion_ciclos_instituto.profesor'
    _description = 'Profesor impartiendo en el instituto'
    _rec_name = 'nombre'

    nombre = fields.Char(
        string='Nombre',
    )

    apellidos = fields.Char(
        string='Apellidos',
    )

    dni = fields.Char(
        string='DNI',
    )
    
    modulo_ids = fields.One2many(
        string='Modulos',
        comodel_name='gestion_ciclos_instituto.modulo',
        inverse_name='profesor_id',
    )
    
    

    