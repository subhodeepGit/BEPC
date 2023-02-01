# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
import datetime

class SchoolwiseEquipmentList(Document):
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
	
	def validate(self):
		School_number_validation(self)
		# self.form_valid()

def School_number_validation(self):
	if self.school_contact_number:
		if not (self.school_contact_number).isdigit():
			frappe.throw("Field <b>Asst. Contact Number</b> Accept Digits Only")
		if len(self.school_contact_number)>10:
			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")
		if len(self.school_contact_number)<10:
			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")

@frappe.whitelist()
def item_fetch(site):
	data = frappe.get_all('Items',{"tcil_code":site},["item_code","item_name","lab","manufacturer","manufacturer_email","serial_number"])
	for t in  data:
		if t:
			return data