from odoo import models,fields,api
from odoo.exceptions import ValidationError

class  Registration(models.Model):
    _name = 'baamtu_academy.registration'
    _description = 'modele pour  les inscriptions'
    _log_access = True
    _order = 'registration_date asc'
    _sql_constraints = [
        ('unique_student_course', 'unique(student_id, course_id)', 'Cet étudiant est déjà inscrit à ce cours.')
    ]

    student_id = fields.Many2one('baamtu_academy.student',string=u"Étudiant",required=True)
    course_id = fields.Many2one('baamtu_academy.course',string="Cours",required=True)
    registration_date = fields.Date(string=u"Date d'inscription", default=fields.Date.context_today)
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('validated', 'Validé'),
        ('canceled', 'Annulé')],
        default='draft')
        
    @api.constrains('course_id')
    def _check_max_place(self):
        for registration in self:
            course = registration.course_id
            registered_students_count = self.search_count([('course_id', '=', course.id)])
        if registered_students_count > course.max_place:
                raise ValidationError("Le nombre maximal de places pour ce cours a été atteint.")

    
    def action_validated(self):
        self.state = 'validated'

    def action_canceled(self):
        self.state = 'canceled'
    
    def action_draft(self):
        self.state = 'draft'