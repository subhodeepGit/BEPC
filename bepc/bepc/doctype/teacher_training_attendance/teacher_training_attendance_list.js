frappe.listview_settings['Teacher Training Attendance'] = {
	add_fields: ["status", "attendance_date"],
	get_indicator: function (doc) {
		if (["Present"].includes(doc.status)) {
			return [__(doc.status), "green", "status,=," + doc.status];
		} else if (["Absent"].includes(doc.status)) {
			return [__(doc.status), "red", "status,=," + doc.status];
		}
	},
};