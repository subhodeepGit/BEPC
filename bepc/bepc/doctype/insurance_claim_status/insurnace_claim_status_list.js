frappe.listview_settings['Insurance Claim Status'] = {
	add_fields: [ "isurance_claim_status"],
	get_indicator: function(doc) {
		if(flt(doc.isurance_claim_status)=="Received") {
			return [__("Received"), "orange", "isurance_claim_status,=,'Received'"];
		}
		else if(flt(doc.isurance_claim_status)=="Not Received") {
			return [__("Not Received"), "green", "isurance_claim_status,=,Not Received"];
		}
	}
};

