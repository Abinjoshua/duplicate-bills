# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"


    @api.constrains('amount_total', 'partner_id', 'partner_ref')
    def _check_unique_vendor_bill(self):

        duplicate = self.search_count([('partner_id', '=', self.partner_id),
                                       ('amount_total', '=', self.amount_total),
                                       ('partner_ref', '=', self.partner_ref)])

        if duplicate > 1:
            raise ValidationError("Duplicate vendor bill found")
