# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SchoolSurveyForm(Document):
	pass
	# def on_change(doc):
	# 	asst_number_validation(doc)
	# 	incharge_mobile_number(doc)
	# 	deo_mobile_number(doc)
	# 	visiter_mobile_number(doc)
	# 	school_contact_person_other_than_above(doc)
		

@frappe.whitelist()
def get_user_role(doc):
	user_role=frappe.db.get_value("User",{"name":frappe.session.user},["role_profile_name"])
	return user_role

# def asst_number_validation(doc):
# 	if doc.asst_contact_no:
# 		if not (doc.asst_contact_no).isdigit():
# 			frappe.throw("Field <b>Asst. Contact Number</b> Accept Digits Only")
# 		if len(doc.asst_contact_no)>10:
# 			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")
# 		if len(doc.asst_contact_no)<10:
# 			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")

# def incharge_mobile_number(doc):
# 	if doc.incharge_contact_no:
# 		if not (doc.incharge_contact_no).isdigit():
# 			frappe.throw("Field <b>Incharge Contact Number</b> Accept Digits Only")
# 		if len(doc.incharge_contact_no)>10:
# 			frappe.throw("Field <b>Incharge Contact Number</b> must be 10 Digits")
# 		if len(doc.incharge_contact_no)<10:
# 			frappe.throw("Field <b>Incharge Contact Number</b> must be 10 Digits")

# def deo_mobile_number(doc):
# 	if doc.mob_no:
# 		if not (doc.mob_no).isdigit():
# 			frappe.throw("Field <b>Mobile Number</b> Accept Digits Only")
# 		if len(doc.mob_no)>10:
# 			frappe.throw("Field <b>Mobile Number</b> must be 10 Digits")
# 		if len(doc.mob_no)<10:
# 			frappe.throw("Field <b>Mobile Number</b> must be 10 Digits")

# def visiter_mobile_number(doc):
# 	if doc.visiter_mobile_number:
# 		if not (doc.visiter_mobile_number).isdigit():
# 			frappe.throw("Field <b>Visitor Mobile Number</b> Accept Digits Only")
# 		if len(doc.visiter_mobile_number)>10:
# 			frappe.throw("Field <b>Visitor Mobile Number</b> must be 10 Digits")
# 		if len(doc.visiter_mobile_number)<10:
# 			frappe.throw("Field <b>Visitor Mobile Number</b> must be 10 Digits")

# def school_contact_person_other_than_above(doc):
# 	if doc.school_contact_person_other_than_above:
# 		if not (doc.school_contact_person_other_than_above).isdigit():
# 			frappe.throw("Field <b>Other Contact Person Mobile Number</b> Accept Digits Only")
# 		if len(doc.school_contact_person_other_than_above)>10:
# 			frappe.throw("Field <b>Other Contact Person Mobile Number</b> must be 10 Digits")
# 		if len(doc.school_contact_person_other_than_above)<10:
# 			frappe.throw("Field <b>Other Contact Person Mobile Number</b> must be 10 Digits")
