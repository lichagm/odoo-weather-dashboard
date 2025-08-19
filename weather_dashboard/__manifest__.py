# -*- coding: utf-8 -*-
{
    'name': "Weather Dashboard",

    'summary': "Consulta y guarda información del clima usando la API de OpenWeather",

    'author': "Lisa",
    'website': "https://github.com/lichagm",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '18.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/weather_record_views.xml',
    ],
}

