# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Teacher(Document):
	def validate(doc):
		mobile_number_validation(doc)

def mobile_number_validation(doc):
	if doc.contact_number:
		if not (doc.contact_number).isdigit():
			frappe.throw("Field <b>Asst. Contact Number</b> Accept Digits Only")
		if len(doc.contact_number)>10:
			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")
		if len(doc.contact_number)<10:
			frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")
