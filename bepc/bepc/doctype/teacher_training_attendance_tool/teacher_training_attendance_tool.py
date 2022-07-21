# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class TeacherTrainingAttendanceTool(Document):
# 	pass
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import json

import frappe
from frappe.model.document import Document
from frappe.utils import getdate


class TeacherTrainingAttendanceTool(Document):
	pass


@frappe.whitelist()
# def get_employees(date, department = None, branch = None, company = None):
def get_employees(date=None,department=None):	
	attendance_not_marked = []
	attendance_marked = []
	list_emp=frappe.get_all("Teachers List",{"parent":department},["employee_id"])
	list_emp_no=[]
	for t in list_emp:
		list_emp_no.append(t['employee_id'])
	list_emp=frappe.get_all("Instructor",filters=[["employee","in",tuple(list_emp_no)],["status","=","Active"],["date_of_joining","<=", date]],fields=['employee',"instructor_name"])
	marked_employee = {}
	for emp in frappe.get_list("Teacher Training Attendance", fields=["employee", "status"],filters={"attendance_date": date}):
		marked_employee[emp['employee']] = emp['status']

	for employee in list_emp:
		employee['status'] = marked_employee.get(employee['employee'])
		if employee['employee'] not in marked_employee:
			attendance_not_marked.append(employee)
		else:
			attendance_marked.append(employee)
	return {
		"marked": attendance_marked,
		"unmarked": attendance_not_marked
	}


@frappe.whitelist()
def mark_employee_attendance(employee_list, status, date, leave_type=None, company=None):

	employee_list = json.loads(employee_list)
	for employee in employee_list:

		if status == "On Leave" and leave_type:
			leave_type = leave_type
		else:
			leave_type = None

		company = frappe.db.get_value("Employee", employee['employee'], "Company", cache=True)

		attendance=frappe.get_doc(dict(
			doctype='Teacher Training Attendance',
			employee=employee.get('employee'),
			employee_name=employee.get('employee_name'),
			attendance_date=getdate(date),
			status=status,
			leave_type=leave_type,
			company=company
		))
		attendance.insert()
		attendance.submit()