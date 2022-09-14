// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('School Consent form for Teacher Training', {
	onload:function(frm)
    {
        frm.set_query('teacher', 'teacher_to_be_trained', function() {
            return {
                filters: {
                    "school_name":frm.doc.school_name
                }
            };
        });
    }
});
