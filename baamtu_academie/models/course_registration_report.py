from odoo import models, fields


class CourseRegistrationReport(models.Model):
    _name = 'baamtu_academy.course_registration_report'
    _auto = False

    course_id = fields.Many2one('baamtu_academy.course', string="Cours", required=True)
    registration_count = fields.Integer("Nombre d'inscrits", required=True)

    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW baamtu_academy_course_registration_report AS
            SELECT
                c.id AS id,
                c.id AS course_id,
                COUNT(r.student_id) AS registration_count
            FROM
                baamtu_academy_course c
            LEFT JOIN
                baamtu_academy_registration r ON c.id = r.course_id
            GROUP BY
                c.id
        """)
