# -*- coding: utf-8 -*-
# © <2017> <Omar Torres Silva (otorres@grupoifaco.com.mx)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models

class product_lgsa229(models.Model):
    _name = 'product.lgsa229'
    _description = 'PRODUCT LGSA229'

    name = fields.Char(
        string='Nombre',
        required=True
    )