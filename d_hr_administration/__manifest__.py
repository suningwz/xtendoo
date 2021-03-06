{
    'name': 'D & HR Administrator',
    'summary': """Administration settings for Discafé and Huelva Regalos""",
    'version': '12.0.1.0.0', 
    'description': """Administration settings foR Discafé and Huelva Regalos""",
    'author': 'DDL',
    'company': 'Xtendoo',
    'website': 'http://www.xtendoo.com',
    'category': 'Extra Tools',
    'depends': [
        'base',
    ],
    'license': 'AGPL-3',
    'data': [
        'views/view_users_form_create_invoice.xml',
        'views/account_payment.xml',
        'views/sale_order_views.xml',
        'views/account_invoice_views.xml',
        'views/product_template_view.xml',
    ],
    "depends": [
        'sale',
    ],
    'installable': True,
    'auto_install': True,
}
