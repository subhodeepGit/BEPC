# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ElectricityConsumptionRecord(Document):
	def validate(self):
		self.cal()

		if(self.meter_reading != self.submeter_total_current_unit):
			frappe.throw("<b>Mainmeter Current reading</b> not Maching with <b>SubMeter Total Current reading</b>")	
	
	def cal(self):
		a = self.meter_reading
		print("\n\n\n\n\n")
		print(a)
		b = self.previous_meter_reading
		print(b)
		c = a-b
		print(c)
		self.total_billable_unit=c
