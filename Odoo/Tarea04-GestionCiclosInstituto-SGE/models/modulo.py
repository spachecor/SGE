from odoo import models, fields

class modulo(models.Model):
    _name = 'gestion_ciclos_instituto.modulo'
    _description = 'Modulo de un ciclo formativo'
    _rec_name = 'modulo'

    modulo = fields.Char(
        string='Modulo',
    )
    
    ciclo_id = fields.Many2one(
        string='Ciclo',
        comodel_name='gestion_ciclos_instituto.ciclo',
        ondelete='cascade',
    )
    
    alumno_ids = fields.Many2many(
        string='Alumnos',
        comodel_name='gestion_ciclos_instituto.alumno',
        relation='modulos_alumnos_rel',
        column1='modulo_id',
        column2='alumno_id',
    )
    
    profesor_id = fields.Many2one(
        string='Profesor',
        comodel_name='gestion_ciclos_instituto.profesor',
        ondelete='restrict',
    )
    
    
    
    
    