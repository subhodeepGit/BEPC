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
			"fieldname": "from_date",
			"label": __("From date"),
			"fieldtype": "Datetime",
			"width": 150,	
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Datetime",
			"width": 150,	
		},
	]
};