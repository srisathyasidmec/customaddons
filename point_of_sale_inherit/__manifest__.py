{
    "name": "POS Modification",
    "author": "Sri Sathya",
    "version": "18.0",
    "depends": ["point_of_sale",],
    # 'license': 'LGPL-3',
    'assets': {
        'point_of_sale._assets_pos': [
            "point_of_sale_inherit/static/src/js/product_card.js",
            "point_of_sale_inherit/static/src/js/receipt_screen_changes.js",
            "point_of_sale_inherit/static/src/js/control_buttons_new.js",
            "point_of_sale_inherit/static/src/xml/receipt_screen_changes.xml",
            "point_of_sale_inherit/static/src/xml/product_card.xml",
            "point_of_sale_inherit/static/src/xml/product_screen.xml",
            "point_of_sale_inherit/static/src/xml/control_buttons_new.xml",
        ],
    },
    # "data" : [
    #     "report/report_recipt_screen.xml",
    # ],
}