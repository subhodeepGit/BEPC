frappe.views.calendar["Survey Form"] = {
	field_map: {
		"start": "actual_end_date",
		"end": "time_to_complete",
		"id": "name",
		"title": "title_of_the_document",
		"allDay": "allDay",
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
	// get_events_method: "erpnext.education.api.get_course_schedule_events"
}