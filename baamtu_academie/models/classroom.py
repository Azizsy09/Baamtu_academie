from odoo import models,fields

class  Classroom(models.Model):
    _name = 'baamtu_academy.classroom'
    _log_access = True
    _order = 'name asc'
    _sql_constraints = [
        ('classroom_unique_code', 'UNIQUE(code)', 'le code doit être unique'),
    ]

    name = fields.Char(string="Nom",required=True)
    code = fields.Integer(string="Code")
   
   