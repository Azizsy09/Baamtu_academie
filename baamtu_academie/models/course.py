from odoo import models,fields,api


class  Course(models.Model):
    _name = 'baamtu_academy.course'
    _log_access = True
    _order = 'name asc'
    _sql_constraints = [
        ('course_unique_code', 'UNIQUE(code)', 'le code doit être unique'),
        ('course_max_place', 'CHECK(max_place > 5 AND max_place <= 45)', 'Un cours doit avoir 5 place au minimum et 45 maximum'),
        ('course_unique_name', 'UNIQUE(name)', 'Ce cours existe déja')
    ]
    _auto = True

    name = fields.Char(string=u"Libellé",required=True)
    code = fields.Integer(string="Code")
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Actif",required=True,default=True)
    max_place = fields.Integer(string="Nombre maximum de places")
    start_date = fields.Date(string=u"Date de début",required=True)
    end_date = fields.Date(string="Date de fin",required=True)
    category = fields.Selection([('language', u'Langue étrangère'), ('computer_science','Informatique')], string=u"Catégorie de cours",default='language')
    professor_id = fields.Many2one('baamtu_academy.professor',string="Professeur",ondelete='cascade',required=True, index=True)
    classroom_id  = fields.Many2one('baamtu_academy.classroom',string="Salle",required=True)
    has_student = fields.Boolean(compute='_compute_has_students',string=u"A des inscrits")
    remaining_registrations = fields.Integer(compute='_compute_remaining_registrations',string=u"Nombres de places restantes")

    def _compute_has_students(self):
        for course in self:
            has_students = self.env['baamtu_academy.registration'].search([('course_id', '=', course.id)])
            course.has_student = bool(has_students)
    
    def _compute_remaining_registrations(self):
        for course in self:
            registration_count = self.env['baamtu_academy.registration'].search_count([('course_id', '=', course.id)])
            course.remaining_registrations = course.max_place -  registration_count
            
   