// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('School wise Equipment List', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on('School wise Equipment List', {
    site: function(frm) {
        frappe.call({
            method: 'bepc.bepc.doctype.school_wise_equipment_list.school_wise_equipment_list.item_fetch',
            args: {
                site:frm.doc.site
            },
           callback: function(r) {
                if(r.message){
                    frappe.model.clear_table(frm.doc, 'table_9');
                    (r.message).forEach(element => {
                        var c = frm.add_child("table_9")
						c.item_code=element.item_code
						c.item_name=element.item_name
						c.vendor=element.manufacturer
						c.mac_id=element.manufacturer_email
						c.serial_number=element.serial_number
                        c.lab=element.lab
                    });
                }
                frm.refresh();
                frm.refresh_field("table_9")
            }
        })
    }
});