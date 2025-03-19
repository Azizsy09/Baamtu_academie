from odoo import http
from odoo.http import request

class WebStudentCoursePortal(http.Controller):

    @http.route('/my/menu', auth='user', website=True)
    def menu_course(self, **kw):
        return request.redirect('/my/course')

    @http.route('/my/course', auth='user', website=True)
    def student_course_page(self, **kw):
        user = request.env.user
        student = request.env['baamtu_academy.student'].sudo().search([('partner_id', '=', user.partner_id.id)], limit=1)
        courses = student.course_ids

        return request.render('baamtu_academie.student_course_template', {
            'courses': courses,
        })
