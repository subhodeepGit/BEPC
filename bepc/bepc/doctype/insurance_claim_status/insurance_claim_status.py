# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class InsuranceClaimStatus(Document):
	def set_indicator(self):
		"""Set indicator for portal"""
		print(self.isurance_claim_status)
		if self.isurance_claim_status == "Received":
			self.indicator_color = "orange"
			self.indicator_title = ("Received")
		else:
			self.indicator_color = "green"
			self.indicator_title = ("Not Received")

	# def on_change(doc):

	# 	if doc.isurance_claim_status=="Received" and doc.docstatus==1:
	# 		mm = frappe.new_doc("Material Request")
	# 		mm.schedule_date = frappe.utils.nowdate()
	# 		mm.material_request_type = "Purchase"
	# 		mm.set_warehouse= doc.target_warehouse
	# 		mm.append("items",{
	# 			'item_code' : doc.item_code,
	# 			'qty' : doc.quantity,
	# 			'uom' : "Nos"
	# 		})
	# 		mm.save()