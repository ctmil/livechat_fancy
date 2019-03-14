# -*- coding: utf-8 -*-

from odoo import models, fields, api

class livechat_fancy(models.Model):
	_inherit = 'im_livechat.channel'

	online = fields.Char('Online message', default='We are online')
	offline = fields.Char('Offline message', default='We are offline')
	btn_message = fields.Char('Button message', default='Chat with Operator')

