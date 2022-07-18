frappe.views.calendar["Survey Form"] = {
	field_map: {
		"start": "actual_start_date",
		"end": "actual_end_date",
		"id": "name",
		"title": "title_of_the_document",
		"allDay": "allDay",
		"color": "color"
	},
	gantt: false,
	order_by: "schedule_date",
	filters: [
		{
			"fieldtype": "Link",
			"fieldname": "kra_template",
			"options": "Survey Questionnaire Template",
			"label": __("Survey Questionnaire Template")
		},
		{
			"fieldtype": "Link",
			"fieldname": "site_name",
			"options": "Site",
			"label": __("Site")
		}
	],
}
