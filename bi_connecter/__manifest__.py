# -*- coding: utf-8 -*-
{
    'name': "bi_connecter",

    'summary': """
       	power bi 
       """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Techneith",
    'website': "https://www.techneith.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base',],
    'images': ['static/description/icon.png'],
    "external_dependencies": {"python" : ["pip"]},

    # always loaded
    'data': [
        'views/settings.xml',
        # 'views/resources.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,
    "installable": True,
    "post_init_hook":"bi_post_init_hook",
    "uninstall_hook":"bi_uninstall_hook"
}
