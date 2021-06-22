##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api


class AccountFinancingPlan(models.Model):
    _name = 'account.financing.plan'
    _description = 'account.financing_plan'
    _order = 'sequence asc'

    sequence = fields.Integer(
        'Sequence',
        default=10,
    )
    name = fields.Char(required=True)
    surcharge_coefficient = fields.Integer(
        'Surcharge coefficient',
        required=True,
    )