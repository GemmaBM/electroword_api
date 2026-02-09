{
    'name': 'ElectroWord API',
    'version': '1.0',
    'summary': 'API REST para obtener productos y clientes en Odoo',
    'author': 'TU NOMBRE Y APELLIDOS',
    'category': 'API',
    'depends': ['base', 'sale', 'product', 'website'],
    'data': [
        'views/products_template.xml',
        'views/customers_template.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'icon': 'electroword_api/static/description/icon59.png',
}