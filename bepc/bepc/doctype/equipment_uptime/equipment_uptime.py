# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils.data import getdate
from datetime import datetime
from frappe.utils import date_diff

class EquipmentUptime(Document):
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
