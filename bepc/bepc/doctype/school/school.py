# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime
from datetime import date, timedelta
from datetime import date, timedelta

class School(Document):
	pass
	# def validate(doc):
	# 	school_number_validation(doc)
	# 	principle_number_validation(doc)
	# 	president_number_validation(doc)
	# 	asst_number_validation(doc)
	# 	pincode(doc)
		
	# 	doc.school_code=doc.data_33
	# 	print("\n\n\n\n\n\n\n")
	# 	print(type(doc.go_live_date))	
	# 	d2=str(doc.go_live_date)
	# 	print(type(d2))
	# 	dt_obj = datetime.datetime.strptime(d2,"%Y-%m-%d")
	# 	print(type(dt_obj))
	# 	today_date =dt_obj.date()				
	# 	# today_date = datetime.datetime.strftime(dt_obj, "%Y-%m-%d")
	# 	# print(type(today_date))			//str
	# 	doc.project_end_date = today_date + timedelta(days=1800)


@frappe.whitelist()
def get_user_role(doc):
	user_role=frappe.db.get_value("User",{"name":frappe.session.user},["role_profile_name"])
	return user_role

# def pincode(doc):
# 	if doc.pin_code:
# 		if not (doc.pin_code).isdigit():
# 			frappe.throw("Field <b>Pin Code</b> Accept Digits Only")
# 		if len(doc.pin_code)>6:
# 			frappe.throw("Field <b>Pin Code</b> must be 6 Digits")
# 		if len(doc.pin_code)<6:
# 			frappe.throw("Field <b>Pin Code</b> must be 6 Digits")

# def school_number_validation(doc):
# 	if doc.school_contact_no:
# 		if not (doc.school_contact_no).isdigit():
# 			frappe.throw("Field <b>School Contact Number</b> Accept Digits Only")
# 		if len(doc.school_contact_no)>10:
# 			frappe.throw("Field <b>School Contact Number</b> must be 10 Digits")
# 		if len(doc.school_contact_no)<10:
# 			frappe.throw("Field <b>School Contact Number</b> must be 10 Digits")

# def principle_number_validation(doc):
# 	if doc.principle_mobile_number:
# 		if not (doc.principle_mobile_number).isdigit():
# 			frappe.throw("Field <b>Headmaster/Head Mistress Contact No</b> Accept Digits Only")
# 		if len(doc.principle_mobile_number)>10:
# 			frappe.throw("Field <b>Headmaster/Head Mistress Contact No</b> must be 10 Digits")
# 		if len(doc.principle_mobile_number)<10:
# 			frappe.throw("Field <b>Headmaster/Head Mistress Contact No</b> must be 10 Digits")

# def president_number_validation(doc):
# 	if doc.president_contact_no:
# 		if not (doc.president_contact_no).isdigit():
# 			frappe.throw("Field <b>President Contact Number</b> Accept Digits Only")
# 		if len(doc.president_contact_no)>10:
# 			frappe.throw("Field <b>President Contact Number</b> must be 10 Digits")
# 		if len(doc.president_contact_no)<10:
# 			frappe.throw("Field <b>President Contact Number</b> must be 10 Digits")

# def asst_number_validation(doc):
# 	if doc.asst_contact_number:
# 		if not (doc.asst_contact_number).isdigit():
# 			frappe.throw("Field <b>Asst Contact Number</b> Accept Digits Only")
# 		if len(doc.asst_contact_number)>10:
# 			frappe.throw("Field <b>Asst Contact Number</b> must be 10 Digits")
# 		if len(doc.asst_contact_number)<10:
# 			frappe.throw("Field <b>Asst Contact Number</b> must be 10 Digits")