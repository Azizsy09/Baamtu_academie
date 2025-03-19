from odoo import http
from odoo.http import request

class Registration(http.Controller):

    @http.route('/student_webform',auth='public', website=True)
    def student_webform(self,**kw):
        return request.render("baamtu_academie.create_student",{})

    
    @http.route('/create/webstudent_registration_form', auth='user', website=True)
    def registration_student(self, **kw):
        student = request.env['baamtu_academy.student'].sudo().create(kw)

        user_vals = {
            'name': kw.get('name'),
            'login': kw.get('email'),
            'email': kw.get('email'),
            'password': 'mot_de_passe', 
           
            'partner_id': student.partner_id.id, 
           
        }
        user = request.env['res.users'].sudo().create(user_vals)
        user.action_reset_password()
        student.user_id = user.id
        group_portal = request.env.ref('base.group_portal')
        user.write({'groups_id': [(5, 0, 0), (4, group_portal.id)]})

        return request.render("baamtu_academie.student_thank", {})
