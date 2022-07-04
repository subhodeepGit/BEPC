// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt
frappe.ui.form.on('Survey Form', {
	kra_template: function(frm) {
		if(frm.doc.kra_template){
			frappe.call({
				method: "frappe.client.get",
				args: {
					doctype: "Survey Questionnaire Template",
					filters: {name: frm.doc.kra_template}
				},
				callback: function(r) {
					if(r.message){
						if(!r.message.electricity_consumption_reading){
							frm.set_df_property('electricity_consumption_reading', 'hidden', 1);
						}
						if(!r.message.internet_use){
							frm.set_df_property('internet_use', 'hidden', 1);
						}
					}
				}
			});
		}
	},
});