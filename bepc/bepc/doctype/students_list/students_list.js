// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Students List', {
	onload:function(frm)
    {
        frm.set_query("section", function() {
            return {
                filters: {
                    "program":frm.doc.program
                }
            };
        });
    }
});
frappe.ui.form.on('Students List', {
    refresh:function(frm){
        a=0;
        a=frm.doc.student_list.length;
        frm.set_value("total_student", a);
        refresh_field("total_student");
    }
});