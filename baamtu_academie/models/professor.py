from odoo import models,fields

class  Professor(models.Model):
    _name = 'baamtu_academy.professor'
    _description = "Professeur model"
    _table = "professeur"
    _inherits = {
        'res.partner' : 'partner_id'
    }

    partner_id = fields.Many2one('res.partner', required=True)
    last_name = fields.Char(string=u'Prénom',required=True)
    year_of_experience = fields.Integer(string=u"Nombre d'année d'expérience")
    course_ids = fields.One2many('baamtu_academy.course', 'professor_id', string=u"Cours dispensé")
   
    