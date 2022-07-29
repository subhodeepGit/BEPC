# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ElectricityConsumptionRecord(Document):
	def validate(self):
		self.cal()	
	
	def cal(self):
		a = self.meter_reading
		b = self.previous_meter_reading
		c = a-b
		self.total_billable_unit=c
