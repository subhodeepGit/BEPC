import frappe

def validate(self, method):
    if self.start_date >= self.end_date:
        frappe.throw("SLA Start date cannot be greater than SLA End date")