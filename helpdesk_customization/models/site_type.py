
from odoo import models, fields, api, _


class AlarmType(models.Model):
    _name = 'site.type'

    name = fields.Char(string='Name')
