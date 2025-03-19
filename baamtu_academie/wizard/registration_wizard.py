from odoo import models, fields, api


class RegistrationWizard(models.TransientModel):
    _name = 'baamtu_academy.registration.wizard'
    _description = 'Assistant d\'inscription en groupe aux cours'

    course_ids = fields.Many2many('baamtu_academy.course', string="Cours", required=True)
    student_ids = fields.Many2many('baamtu_academy.student', string=u"Étudiants", required=True)
    registration_date = fields.Date(string=u"Date d'inscription")

    def registration_wizard_action(self):
        Registration = self.env['baamtu_academy.registration']
        for student in self.student_ids:
            for course in self.course_ids:
                registration = Registration.create({
                    'student_id': student.id,
                    'course_id': course.id,
                    'registration_date': self.registration_date,
                })