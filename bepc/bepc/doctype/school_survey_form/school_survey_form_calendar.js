frappe.views.calendar["Survey Form"] = {
	field_map: {
		"start": "survey_start_date",
		"end": "survey_end_date",
		"id": "name",
		"title": "title_of_the_document",
		"allDay": "allDay",
		"color": "colour_for_calendar_event"
	},
	gantt: false,
	order_by: "schedule_date"
	// filters: [
	// 	{
	// 		"fieldtype": "Link",
	// 		"fieldname": "kra_template",
	// 		"options": "Survey Questionnaire Template",
	// 		"label": __("Survey Questionnaire Template")
	// 	},
	// 	{
	// 		"fieldtype": "Link",
	// 		"fieldname": "site_name",
	// 		"options": "Site",
	// 		"label": __("Site")
	// 	}
	// ],
}