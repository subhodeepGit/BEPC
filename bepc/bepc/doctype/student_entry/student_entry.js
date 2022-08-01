// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Entry', {
		final_score:function(frm, cdt, cdn){
		print("hello")
		var d = locals[cdt][cdn];
		var total = 0;
		let a= parseInt(total)
		frm.doc.total_student.forEach(function(d)  { a = a+ d.final_score; });
		frm.set_value("total_student_per_school", a);
		refresh_field("total_student_per_school");
	  },
});
frappe.ui.form.on('Class', {
	total_student:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.class.forEach(function(d)  { a = a+ d.total_student; });
	frm.set_value("total_student_per_school", a);
	refresh_field("total_student_per_school");
  },
  class_remove:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.class.forEach(function(d) { a += d.total_student; });
	frm.set_value("total_student_per_school", a);
	refresh_field("total_student_per_school");
		}
	});