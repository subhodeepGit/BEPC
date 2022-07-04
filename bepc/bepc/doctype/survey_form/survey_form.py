# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

from os import dup
from warnings import filters
import frappe
from frappe.model.db_query import get_date_range
from frappe.model.document import Document
from frappe.utils.data import getdate

class SurveyForm(Document):
	def validate(self):
		self.validate_dates()
		
	def validate_dates(self):
		if self.date_of_upload and getdate(self.date_of_upload) > getdate():
			frappe.throw(frappe._("Date of Upload cannot be greater than today's date."))

	print("\n\n\n\n\n\n")
	print(frappe.session.user)

    