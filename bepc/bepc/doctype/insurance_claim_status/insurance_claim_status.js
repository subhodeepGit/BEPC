// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Insurance Claim Status', {
	refresh: function(frm) {
		if (frm.doc.docstatus==1 && frm.doc.isurance_claim_status!="Received") {
			frm.add_custom_button(__("Approve"), function() {
				frm.set_value("isurance_claim_status", "Received");
				frm.save_or_update();

			}, 'Actions');

			frm.add_custom_button(__("Reject"), function() {
				frm.set_value("isurance_claim_status", "Not Received");
				frm.save_or_update();
			}, 'Actions');
		}
	}
});
