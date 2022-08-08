// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('School Survey Form', "validate", function(frm) {
        if (frm.doc.year_of_start__project > get_today()) {
            frappe.msgprint(__("You can not select future date in Year of Start Project"));
            frappe.validated = false;
        }
});
