// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Block', {
	onload:function(frm)
    {
        frm.set_query("district", function() {
            return {
                filters: {
                    "state":frm.doc.state
                }
            };
        });
    }
});
