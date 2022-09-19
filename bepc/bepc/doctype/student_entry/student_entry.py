# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StudentEntry(Document):
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

