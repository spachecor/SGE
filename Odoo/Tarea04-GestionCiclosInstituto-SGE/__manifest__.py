# -*- coding: utf-8 -*-
{
    'name': "Gestion Ciclos Instituto",

    'summary': "Gestion de ciclos, modulos, alumnos y profesores",

    'description': """
        Modulo para la gestion de ciclos, modulos, alumnos y profesores de un instituto
    """,

    'author': "Alejandro Rebagliato García",
    'website': "https://github.com/Zarcam/Tarea04-GestionCiclosInstituto-SGE",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/view_ciclo.xml',
        'views/view_modulo.xml',
        'views/view_alumno.xml',
        'views/view_profesor.xml',
        'views/view_menuitems.xml',
    ],
}

