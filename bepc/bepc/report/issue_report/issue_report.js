// Copyright (c) 2023, SOUL and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Issue report"] = {
	"filters": [	
		{
			"fieldname": "district",
			"label": __("District"),
			"fieldtype": "Link",
			"options": "Districts",
			"width": 150,
			"reqd": 0,
			"default":"ARARIA"
	
		},
		{
			"fieldname": "issue_creation_date_and_time",
			"label": __("Issue creation date and Time"),
			"fieldtype": "Datetime",
			"width": 150,	
		},
		{
			"fieldname": "resolution_date",
			"label": __("Resolution Date"),
			"fieldtype": "Datetime",
			"width": 150,	
		},
	]
};