# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.data import getdate
from datetime import datetime
from frappe.utils import date_diff

class EquipmentUptime(Document):
	def on_change(self):
		School_number_validation(self)
		
	def validate(self):
		date_format = "%Y-%m-%d"
		# delta = date_diff(self.from_date_and_time, self.to_date_and_time)
		delta = date_diff(self.to_date_and_time, self.from_date_and_time)
		print("\n\n\n\n\n\n")
		print(delta)
		self.total_downtime = delta

		delta1 = date_diff(self.to_time, self.from_time)
		total_uptime = delta1-delta
		self.total_uptime = total_uptime

def School_number_validation(self):
	if self.school_contact_number:
		if not (self.school_contact_number).isdigit():
			frappe.throw("Field <b>Asst. Contact Number</b> Accept Digits Only")
		if len(self.school_contact_number)>10:
			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")
		if len(self.school_contact_number)<10:
			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")
