# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
import datetime

class ElectricityConsumptionRecord(Document):
	def form_valid(self):
		d1=self.go_live_date
		d2=self.date
		d3=self.project_end_date
		start_date = d1.strftime("%Y-%m-%d")
		dt_obj = datetime.datetime.strptime(d2,"%Y-%m-%d")
		today_date = datetime.datetime.strftime(dt_obj, "%Y-%m-%d")
		end_date = d3.strftime("%Y-%m-%d")
		if (today_date >= start_date) and (end_date >= today_date):
			pass
		else:
			frappe.throw("Project Date Expired")

	def on_change(self):
		School_number_validation(self)

	def validate(self):
		self.cal()
		self.total_price()
		self.mainmeter()
		self.form_valid()


		# if(self.meter_reading != self.submeter_total_current_unit):
		# 	frappe.throw("<b>Mainmeter Current reading</b> not Maching with <b>SubMeter Total Current reading</b>")	
	
	def cal(self):
		a = self.meter_reading
		print("\n\n\n\n\n")
		b = self.previous_meter_reading
		c = a-b
		self.total_billable_unit=c

	def mainmeter(self):
		self.total_consumed_unit = self.main_meter_current_reading - self.main_meter_previous_reading

	def total_price(self):
		self.total_bill_amount = self.total_billable_unit * self.price_per_unit

def School_number_validation(self):
	if self.school_contact_number:
		if not (self.school_contact_number).isdigit():
			frappe.throw("Field <b>Asst. Contact Number</b> Accept Digits Only")
		if len(self.school_contact_number)>10:
			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")
		if len(self.school_contact_number)<10:
			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")