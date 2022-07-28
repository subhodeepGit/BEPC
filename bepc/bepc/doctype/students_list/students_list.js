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
