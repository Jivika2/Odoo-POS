# -*- coding: utf-8 -*-
{
    'name': "Restrict",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'xml/view.xml',

       
    ],
    'assets':{
        'point_of_sale.assets':[
            "pos_restrict/static/src/js/sample_button.js",
            "pos_restrict/static/src/xml/sample_button.xml"
        ],
    }
    # only loaded in demonstration mode
#     'demo': [
#         'demo/demo.xml',
#     ],
}
