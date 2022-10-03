frappe.listview_settings['Internet consumption Record'] = {
	add_fields: ["date", "payment_date","last_payment_date"],
	get_indicator: function(doc) {
		if(doc.payment_date) {
			return [__("Paid"), "green", "payment_date,!=,NULL"];
		} else if (doc.date < doc.last_payment_date) {
            return [__("Unpaid"), "orange", "date,<,last_payment_date"];
        } else if (doc.date > doc.last_payment_date) {
            return [__("Overdue"), "red", "date,>,last_payment_date"];
        }
	}
};