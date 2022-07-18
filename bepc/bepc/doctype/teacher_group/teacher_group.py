# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TeacherGroup(Document):
    pass

	# @frappe.whitelist()
	# def get_teachers(academic_year, group_based_on, program=None, course=None):

    # 	enrolled_teachers = get_teacher_enrollment(academic_year,program)

    #     if enrolled_teachers:
    #     teacher_list = []
    #     for s in enrolled_teachers:
    #         if frappe.db.get_value("Teacher", s.name1, "enabled"):
    #             s.update({"active": 1})
    #         else:
    #             s.update({"active": 0})
    #         teacher_list.append(s)
    #     return teacher_list
    # else:
    #     frappe.msgprint("No teacher found")
    #     return []

	# def get_teacher_enrollment(academic_year,program=None):
    # condition1 = " "
    # condition2 = " "
    # if academic_year:
    #     condition1 += " and pe.academic_year = %(academic_year)s"
    # if program:
    #     condition1 += " and pe.program = %(program)s"
    
    # return frappe.db.sql('''
    #     select
    #         pe.name1
    #     from
    #         `tabTeacher ` pe {condition2}
    #     where
    #         (pe.is_provisional_admission IS NULL or pe.is_provisional_admission="No") and
    #         pe.academic_year = %(academic_year)s  {condition1}
    #     order by
    #         pe.name1 asc
    #     '''.format(condition1=condition1, condition2=condition2),
    #             ({"academic_year": academic_year, "program": program}), as_dict=1)
	

	# @frappe.whitelist()
    # def get_students(self):
    #     students = []
    #     if not self.program:
    #         frappe.throw(_("Mandatory field - Program"))
    #     elif not self.academic_year:
    #         frappe.throw(_("Mandatory field - Academic Year"))
    #     else:
    #         condition = 'and academic_term=%(academic_term)s' if self.academic_term else " "
    #         self.get_students_from = "Program Enrollment"
    #         condition2 = 'and student_batch_name=%(student_batch)s' if self.student_batch else " "
    #         students = frappe.db.sql('''select student, student_name, student_batch_name, roll_no,permanant_registration_number, student_category from `tabProgram Enrollment`   
    #             where program=%(program)s and academic_year=%(academic_year)s {0} {1} and docstatus != 2'''
    #             .format(condition, condition2), self.as_dict(), as_dict=1)          

    #         student_list = [d.student for d in students]
    #         if student_list:
    #             inactive_students = frappe.db.sql('''
    #                 select name as student, title as student_name from `tabStudent` where name in (%s) and enabled = 0''' %
    #                 ', '.join(['%s']*len(student_list)), tuple(student_list), as_dict=1)

    #             for student in students:
    #                 if student.student in [d.student for d in inactive_students]:
    #                     students.remove(student)

    #     if students:
    #         return students
    #     else:
    #         frappe.throw(_("No students Found"))
    	
