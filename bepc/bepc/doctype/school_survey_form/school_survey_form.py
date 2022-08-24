# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SchoolSurveyForm(Document):
    pass
	# def validate(doc):
		# mobile_number_validation(doc)
		# mobile_number(doc)
		# mobile(doc)
        
		# contact(doc)
		# contact2(doc)
		# contact3(doc)

# def mobile_number_validation(doc):
#     if doc.asst_contact_no:
#         if not (doc.asst_contact_no).isdigit():
#             frappe.throw("Field <b>Asst. Contact Number</b> Accept Digits Only")
#         if len(doc.asst_contact_no)>10:
#             frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")
#         if len(doc.asst_contact_no)<10:
#             frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")

# def mobile_number(doc):
#     if doc.incharge_contact_no:
#         if not (doc.incharge_contact_no).isdigit():
#             frappe.throw("Field <b>Incharge Contact Number</b> Accept Digits Only")
#         if len(doc.incharge_contact_no)>10:
#             frappe.throw("Field <b>Incharge Contact Number</b> must be 10 Digits")
#         if len(doc.incharge_contact_no)<10:
#             frappe.throw("Field <b>Incharge Contact Number</b> must be 10 Digits")

# def mobile(doc):
#     if doc.mob_no:
#         if not (doc.mob_no).isdigit():
#             frappe.throw("Field <b>Mobile Number</b> Accept Digits Only")
#         if len(doc.mob_no)>10:
#             frappe.throw("Field <b>Mobile Number</b> must be 10 Digits")
#         if len(doc.mob_no)<10:
#             frappe.throw("Field <b>Mobile Number</b> must be 10 Digits")

# def contact(doc):
#     if doc.contact_no1:
#         if not (doc.contact_no1).isdigit():
#             frappe.throw("Field <b>Contact Number</b> Accept Digits Only")
#         if len(doc.contact_no1)>10:
#             frappe.throw("Field <b>Contact Number</b> must be 10 Digits")
#         if len(doc.contact_no1)<10:
#             frappe.throw("Field <b>Contact Number</b> must be 10 Digits")

# def contact2(doc):
#     if doc.contact_no11:
#         if not (doc.contact_no11).isdigit():
#             frappe.throw("Field <b>Contact Number</b> Accept Digits Only")
#         if len(doc.contact_no11)>10:
#             frappe.throw("Field <b>Contact Number</b> must be 10 Digits")
#         if len(doc.contact_no11)<10:
#             frappe.throw("Field <b>Contact Number</b> must be 10 Digits")

# def contact3(doc):
#     if doc.contact_no111:
#         if not (doc.contact_no111).isdigit():
#             frappe.throw("Field <b>Contact Number</b> Accept Digits Only")
#         if len(doc.contact_no111)>10:
#             frappe.throw("Field <b>Contact Number</b> must be 10 Digits")
#         if len(doc.contact_no111)<10:
#             frappe.throw("Field <b>Contact Number</b> must be 10 Digits")