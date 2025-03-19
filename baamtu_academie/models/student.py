from odoo import models,fields,_,api

class  Student(models.Model):
    _name = 'baamtu_academy.student'
    _description = 'modele pour  les étudiants'
    _order = 'name asc'
    _inherits = {
        'res.partner' : 'partner_id'
    }

    partner_id = fields.Many2one('res.partner', required=True)
    last_name = fields.Char(string=u'Prénom',required=True)
    date_of_birth = fields.Date(string="Date de naissance")
    course_ids = fields.Many2many('baamtu_academy.course', 'baamtu_academy_registration', 'student_id', 'course_id', string='Cours suivis')
    code = fields.Char(string="Code", required=True, copy=False, readonly=True, default= lambda self: _('New'))

    

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            vals['name'] = 'Nouvel étudiant'
        if vals.get ('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('baamtu_academy.student') or _('New')
        res = super (Student, self).create(vals)
        return res 