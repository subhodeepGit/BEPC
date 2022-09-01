# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class School(Document):
	pass

@frappe.whitelist()
def get_user_role(doc):
	user_role=frappe.db.get_value("User",{"name":frappe.session.user},["role_profile_name"])
	return user_role
	# def validate(doc):
	# 	mobile_number_validation(doc)
	# 	mobile_number(doc)
	# 	number_validation(doc)
	# 	pincode(doc)

# def pincode(doc):
# 	if doc.pin_code:
# 		# if not (doc.pin_code).isdigit():
# 		# 	frappe.throw("Field <b>Pin Code</b> Accept Digits Only")
# 		if len(doc.pin_code)>6:
# 			frappe.throw("Field <b>Pin Code</b> must be 6 Digits")
# 		if len(doc.pin_code)<6:
# 			frappe.throw("Field <b>Pin Code</b> must be 6 Digits")

# def mobile_number_validation(doc):
# 	if doc.school_contact_no:
# 		# if not (doc.school_contact_no).isdigit():
# 		# 	frappe.throw("Field <b>School Contact Number</b> Accept Digits Only")
# 		if len(doc.school_contact_no)>10:
# 			frappe.throw("Field <b>School Contact Number</b> must be 10 Digits")
# 		if len(doc.school_contact_no)<10:
# 			frappe.throw("Field <b>School Contact Number</b> must be 10 Digits")

# def mobile_number(doc):
# 	if doc.principle_mobile_number:
# 		if not (doc.principle_mobile_number).isdigit():
# 			frappe.throw("Field <b>Headmaster/Head Mistress Contact No</b> Accept Digits Only")
# 		if len(doc.principle_mobile_number)>10:
# 			frappe.throw("Field <b>Headmaster/Head Mistress Contact No</b> must be 10 Digits")
# 		if len(doc.principle_mobile_number)<10:
# 			frappe.throw("Field <b>Headmaster/Head Mistress Contact No</b> must be 10 Digits")

# def number_validation(doc):
# 	if doc.president_contact_no:
# 		if not (doc.president_contact_no).isdigit():
# 			frappe.throw("Field <b>President Contact Number</b> Accept Digits Only")
# 		if len(doc.president_contact_no)>10:
# 			frappe.throw("Field <b>President Contact Number</b> must be 10 Digits")
# 		if len(doc.president_contact_no)<10:
# 			frappe.throw("Field <b>President Contact Number</b> must be 10 Digits")