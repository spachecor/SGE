from odoo import models, fields

class ciclo(models.Model):
    _name = 'gestion_ciclos_instituto.ciclo'
    _description = 'Ciclo formativo'
    _rec_name = 'ciclo'

    ciclo = fields.Char(
        string='Ciclo'
    )

    modulo_ids = fields.One2many(
        string='Modulo',
        comodel_name='gestion_ciclos_instituto.modulo',
        inverse_name='ciclo_id',
    )
    
    