import base64
from odoo import http 
from odoo.http import request

class RealEstate(http.Controller):
    
    @http.route('/property_form', type='http', auth='user', website=True)
    def property_form(self, **kw):
        #property tag value search
        PropertyTag = http.request.env['property.tags']
        property_tags = PropertyTag.search([])
        
        #property types value search
        PropertyType = http.request.env['property.type']
        property_types = PropertyType.search([])
        
        #state value search
        State = http.request.env['res.country.state']
        states = State.search([])
        
        #country value search
        Country = http.request.env['res.country']
        countries = Country.search([])
        
        # property_image = None
        # if 'property_image' in request.httprequest.files:
        #     property_images = request.httprequest.files.get('property_image')
        #     # property_images = property_images.read()
        #     property_image = property_images.encode('base64')
        #     property_image = base64.b64encode(property_image)
            
        
        garden_orientations = request.env['real.estate'].fields_get(allfields=['garden_orientation'])['garden_orientation']['selection']
        
        return http.request.render('estate.create_property',{'property_types': property_types,
                                                            'property_tags': property_tags,
                                                            'garden_orientations': garden_orientations,
                                                            'states':states,
                                                            'countries':countries,
                                                            # 'property_image': property_image,
                                                            })
    
    @http.route('/create/property', type='http', auth='public', website=True)
    def create_property(self,**kw):
        request.env['real.estate'].sudo().create(kw)
        return request.render('estate.user_thanks',{})
    
    