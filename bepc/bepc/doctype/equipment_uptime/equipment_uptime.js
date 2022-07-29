// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Equipment Uptime', {
	onload:function(frm)
    {
        frm.set_query("equipment", function() {
            return {
                filters: {
                    "item_group":frm.doc.equipment_type
                }
            };
        });
    }
});
