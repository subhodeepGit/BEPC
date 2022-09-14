// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Theft Case record', {
	reason: function(frm) {
		if(frm.doc.reason === "Theft"){
			frm.refresh_field("reason");
			frm.set_value("covered_under_insurance","Yes");
		}
		else if(frm.doc.reason === "Burglary"){
			frm.refresh_field("reason");
			frm.refresh_field("covered_under_insurance");
			frm.set_value("covered_under_insurance","Yes");
		}
		else if(frm.doc.reason === "Natural Calamity"){
			frm.refresh_field("reason");
			frm.set_value("covered_under_insurance","No");
		}
		else if(frm.doc.reason === "Rodent Damage"){
			frm.refresh_field("reason");
			frm.set_value("covered_under_insurance","No");
		}
		else if (frm.doc.reason === "Physical Damage"){
			frm.refresh_field("reason");
			frm.set_value("covered_under_insurance","No");
		}
	}
});
