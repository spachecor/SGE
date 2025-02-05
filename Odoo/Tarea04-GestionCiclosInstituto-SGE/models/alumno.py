from odoo import models, fields

class alumno(models.Model):
    _name = 'gestion_ciclos_instituto.alumno'
    _description = 'Alumno matriculado en el instituto'
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
    
    modulo_ids = fields.Many2many(
        string='Modulos',
        comodel_name='gestion_ciclos_instituto.modulo',
        relation='modulos_alumnos_rel',
        column1='alumno_id',
        column2='modulo_id',
    )
 
    profesores = fields.Many2one(
        string='profesores',
        comodel_name='gestion_ciclos_instituto.profesor',
        related='modulo_ids.profesor_id',
        readonly=True,
    )
    
    
    
    
    
    

    