# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

from os import dup
from warnings import filters
import frappe
from frappe.model.db_query import get_date_range
from frappe.model.document import Document
from frappe.utils.data import getdate
from datetime import datetime
from frappe.utils import date_diff

class SurveyForm(Document):
	def validate(self):
		if (self.planned_start_date >= self.planned_end_date):
			frappe.throw("Planned Start date should be less Planned End date")
		
		if (self.actual_start_date >= self.actual_end_date):
			frappe.throw("Actual Start date should be less than Actual End date")

		date_format = "%Y-%m-%d"
		delta = date_diff(self.actual_start_date, self.planned_start_date)
		# a = datetime.strptime(self.planned_start_date, date_format)
		# b = datetime.strptime(self.actual_start_date, date_format)
		# delta = b - a
		# frappe.db.set_value("Survey Form",self.name,"time_to_complete",delta)

		print("\n\n\n\n\n\n")
		print(delta)
		self.time_to_complete = delta