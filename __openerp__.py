##############  __openerp__.py ##############

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2016 MARLON FALCON HDEZ (<http://www.marlonfalcon.cl>).
# contact: contacto@marlonfalcon.cl

######################################################################

{
    'name': 'rio2016',
    'version': '1.0',
    'author': 'Adrián Oliva Del Río',
    'category': 'Deportes',
    'summary': 'Ejemplo de un módulo de Odoo',
    'website': 'https://www.marlonfalcon.cl',
    'description': """
Es un módulo de ejemplo
======================
Con este modulo haremos nuestra primera aplicación en Odoo.

Nota: Necesita Ventas.
    """,
    'license' : 'AGPL-3',
    'depends': ['sale'],
    'update_xml': [
        'rio2016_view.xml',
    ],
    'installable': True,
    'active': False,
}