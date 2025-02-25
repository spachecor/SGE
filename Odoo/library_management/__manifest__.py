# -*- coding: utf-8 -*-
{
    'name': "library_management",

    'summary': "Gestión de una biblioteca para registrar libros, autores, categorías, usuarios y préstamos",

    'description': """
        Este módulo permite gestionar una biblioteca. Con él podrás registrar y gestionar libros, 
        autores, categorías, usuarios y realizar el seguimiento de los préstamos.
    """,

    'website': "https://www.selene.com",

    'category': 'Administration',
    'version': '0.1',
    'author': 'Selene',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_author_views.xml',
        'views/library_category_views.xml',
        'views/library_user_views.xml',
        'views/library_loan_views.xml',
        'reports/action_books_available_report.xml',
        'views/report_books_available.xml',
        'reports/action_loans_active_report.xml',
        'views/report_loans_active.xml',
        'reports/action_loans_history_report.xml',
        'views/report_loans_history.xml',
        'reports/action_users_register_report.xml',
        'views/report_users_register.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}


