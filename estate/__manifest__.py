{
    
    'name':'Real Estate',
    'version' : '1.1',
    'author' : 'bhargav',
    'summary' : 'Real Estate Project',
    'sequence' : 1,
    'category': 'project',
    'description' : 'this is new real estate project',
    
    'depends' : ['base', 'sale', 'mail', 'website'],
    
    'data' : {
        'security/ir.model.access.csv',
        
        # 'views/estate_menu.xml',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_offer_view.xml',
        'views/property_tag_view.xml',
        'views/user_property.xml',
        'views/saleorder_field.xml',
        
        'views/website_property_create_form.xml',
        
        #report template
        'report/report.xml',
        'report/report_tamplate.xml',
        
        #mail tamplates
        # 'data/mail_report_template.xml',
        'data/mail_offer_accept_template.xml',
        'data/mail_offer_reject_template.xml',
        'data/mail_property_created_template.xml',
        
        

        
    },
    
    "assets" :{
        "web.assets_frontend":[
            "estate/static/js/property_form.js",
        ]
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    }
