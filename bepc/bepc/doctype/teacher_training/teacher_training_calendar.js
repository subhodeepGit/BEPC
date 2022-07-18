frappe.views.calendar["Survey Form"] = {
	field_map: {
		"start": "date",
		"end": "end_date",
		"id": "name",
		"title": "training_on",
		"allDay": "allDay",
		"color": "color"
	},
	gantt: false,
	order_by: "schedule_date",
	filters: [
		{
			"fieldtype": "Link",
			"fieldname": "trainer",
			"options": "Instructor",
			"label": __("Instructor")
		}
	],
}