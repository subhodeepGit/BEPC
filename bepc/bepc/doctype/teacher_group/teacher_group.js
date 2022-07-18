// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Teacher Group', {
	
	onload:function(frm)
	{
		frm.set_query('teacher','teacher_list',function() {
			return {
				filters: {
					"academic_year":frm.doc.academic_year,
					"department":frm.doc.department,
					"program":frm.doc.program
				}
			};
		});
	}

	// refresh: function(frm) {

	// }

	// get_teachers_from: function(frm) {
	// 	if (frm.doc.get_students_from == "Student Applicant") {
	// 		frm.dashboard.add_comment(__('Only the Student Applicant with the status "Approved" will be selected in the table below.'));
	// 	}
	// },

	// get_teachers: function(frm) {
    //     frm.clear_table('Teacher')
	// 	if (frm.doc.group_based_on == 'Batch' || frm.doc.group_based_on == 'Course') {
	// 		var teacher_list = [];
	// 		var max_roll_no = 0;
	// 		$.each(frm.doc.name1, function(_i,d) {
	// 			teacher_list.push(d.name1);
	// 			if (d.group_roll_number>max_roll_no) {
	// 				max_roll_no = d.group_roll_number;
	// 			}
	// 		});

	// 		if (frm.doc.academic_year) {
	// 			frappe.call({
	// 				method: 'bepc.bepc.doctype.teacher_group.get_teachers',
	// 				args: {
	// 					'academic_year': frm.doc.academic_year,
	// 				    'group_based_on': frm.doc.group_based_on,
	// 					'program': frm.doc.program,
	// 					'course': frm.doc.course
	// 				},
	// 				callback: function(r) {
	// 					if (r.message) {
	// 						$.each(r.message, function(i, d) {
	// 							if(!in_list(student_list, d.student)) {
	// 								var s = frm.add_child('teachers');
								
	// 								s.name1 = d.name1;
	// 								if (d.active === 0) {
	// 									s.active = 0;
	// 								}
	// 								s.group_roll_number = ++max_roll_no;
	// 							}
	// 						});
	// 						refresh_field('teachers');
	// 						frm.save();
	// 					} else {
	// 						frappe.msgprint(__('Student Group is already updated.'))
	// 					}
	// 				}
	// 			})
	// 		}
	// 	}
		
           


        
    //     else {
	// 		frappe.msgprint(__('Select students manually for the Activity based Group'));
	// 	}
	// },
	
});


