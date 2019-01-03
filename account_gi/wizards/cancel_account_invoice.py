# -*- coding: utf-8 -*-
# © <2016> <Juan Carlos Vazquez Beas (jcvazquez@grupoifaco.com.mx)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import logging
from odoo import fields, models, api

from odooIfacoModulos.proyectos_ifaco.invoice_import.models import account_invoice

_logger = logging.getLogger(__name__)

class cancel_account_invoice(models.TransientModel):
    _name = 'cancel.account.invoice'
    _description = "Motivo de cancelación"

    def act_cancel_invoice(self):
        return self.env.context.get('active_id', False)

    account_id = fields.Many2one(
        string='Factura',
        comodel_name='account.invoice',
        default='act_cancel_invoice'
    )

    commentary = fields.Html(
        string='Motivo de la cancelación',
    )

    @api.multi
    def action_invoice_cancel_gi(self):

        result = super(account_invoice.account_invoice_gi, self).action_invoice_cancel()
        print('2')
        if self.l10n_mx_edi_pac_status == "cancelled" and self.siagi_state == "SY":
            self.update_siagi_cancelled()
        else:
            self.siagi_state = 'ER'

        return result

