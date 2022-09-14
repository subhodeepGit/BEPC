# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime
from frappe.model.document import Document
import datetime

class TeacherTraining(Document):
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
		self.form_valid()
