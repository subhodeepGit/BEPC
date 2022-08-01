// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('School', {
	onload:function(frm)
    {
        frm.set_query("district", function() {
            return {
                filters: {
                    "state":frm.doc.state
                }
            };
        });
        frm.set_query("block", function() {
            return {
                filters: {
                    "district":frm.doc.state
                }
            };
        });
    }
});
