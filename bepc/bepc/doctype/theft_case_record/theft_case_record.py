# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
import datetime
from datetime import date, timedelta

class TheftCaserecord(Document):
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

	def validate(self):
		self.project_end_date = self.go_live_date + timedelta(days=1920)
		self.form_valid()

	def on_change(doc):
		School_number_validation(doc)

def School_number_validation(doc):
	if doc.school_contact_number:
		if not (doc.school_contact_number).isdigit():
			frappe.throw("Field <b>Asst. Contact Number</b> Accept Digits Only")
		if len(doc.school_contact_number)>10:
			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")
		if len(doc.school_contact_number)<10:
			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")