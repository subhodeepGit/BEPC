# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
import datetime
from dateutil import relativedelta
from datetime import date
from datetime import timedelta

class ElectricityConsumptionRecord(Document):
	# def form_valid(self):
	# 	d1=self.go_live_date
	# 	d2=self.date
	# 	d3=self.project_end_date
	# 	start_date = d1.strftime("%Y-%m-%d")
	# 	dt_obj = datetime.datetime.strptime(d2,"%Y-%m-%d")
	# 	today_date = datetime.datetime.strftime(dt_obj, "%Y-%m-%d")
	# 	end_date = d3.strftime("%Y-%m-%d")
	# 	if (today_date >= start_date) and (end_date >= today_date):
	# 		pass
	# 	else:
	# 		frappe.throw("Project Date Expired")

	def on_change(self):
		School_number_validation(self)

	def validate(self):
		# self.last_payment_date = self.date + timedelta(days=5)
		self.cal()
		self.total_price()
		self.mainmeter()
		# self.form_valid()
		# self.quarter_calculation()
		# posting_date = datetime.datetime.strptime(self.date, "%Y-%m-%d")
		# self.last_payment_date = posting_date + datetime.timedelta(days=5)

	
	def cal(self):
		a = self.meter_reading
		b = self.previous_meter_reading
		c = a-b
		self.total_billable_unit=c

	def mainmeter(self):
		self.total_consumed_unit = self.main_meter_current_reading - self.main_meter_previous_reading

	def total_price(self):
		self.total_bill_amount = self.total_billable_unit * self.price_per_unit

	def quarter_calculation(self):
		start_date = self.go_live_date
		end_date = self.date
		print("\n\n\n\n\n")
		dt_obj = datetime.datetime.strptime(end_date,"%Y-%m-%d")
		# today_date = datetime.datetime.strftime(dt_obj, "%Y-%m-%d")
		# print("Today's date: ")
		# print(type(today_date))
		r = relativedelta.relativedelta(dt_obj, start_date)
		month = r.months + (12*r.years)
		if month>=0 and month<=3 :
			self.quarter="Quarter-1"
		elif month>=4 and month<=6 :
			self.quarter="Quarter-2"
		elif month>=7 and month<=9 :
			self.quarter="Quarter-3"
		elif month>=10 and month<=12 :
			self.quarter="Quarter-4"
		elif month>=13 and month<=15 :
			self.quarter="Quarter-5"
		elif month>=16 and month<=18 :
			self.quarter="Quarter-6"
		elif month>=19 and month<=21 :
			self.quarter="Quarter-7"
		elif month>=22 and month<=24 :
			self.quarter="Quarter-8"
		elif month>=25 and month<=27 :
			self.quarter="Quarter-9"
		elif month>=28 and month<=30 :
			self.quarter="Quarter-10"
		elif month>=31 and month<=33 :
			self.quarter="Quarter-11"
		elif month>=34 and month<=36 :
			self.quarter="Quarter-12"
		elif month>=37 and month<=39 :
			self.quarter="Quarter-13"
		elif month>=40 and month<=42 :
			self.quarter="Quarter-14"
		elif month>=43 and month<=45 :
			self.quarter="Quarter-15"
		elif month>=46 and month<=48 :
			self.quarter="Quarter-16"
		elif month>=49 and month<=51 :
			self.quarter="Quarter-17"
		elif month>=52 and month<=54 :
			self.quarter="Quarter-18"
		elif month>=55 and month<=57 :
			self.quarter="Quarter-19"
		elif month>=58 and month<=60 :
			self.quarter="Quarter-20"
		else:
			frappe.throw("Invalid date")


def School_number_validation(self):
	if self.school_contact_number:
		if not (self.school_contact_number).isdigit():
			frappe.throw("Field <b>Asst. Contact Number</b> Accept Digits Only")
		if len(self.school_contact_number)>10:
			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")
		if len(self.school_contact_number)<10:
			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")