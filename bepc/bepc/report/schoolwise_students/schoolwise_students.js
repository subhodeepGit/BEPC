// Copyright (c) 2023, SOUL and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["SchoolWise Students"] = {
	"filters": [
		
		
		// {
		// 	"fieldname": "school_code",
		// 	"label": __("PIMPL/TCIL code"),
		// 	"fieldtype": "Link",
		// 	"options": "School",
		// 	"width": 150,
		// 	"reqd": 0,		
		// },
		{
			"fieldname": "district",
			"label": __("District"),
			"fieldtype": "Link",
			"options": "Districts",
			"width": 150,
			"reqd": 0,
			"default":"AURANGABAD"
	
		},
		// {
		// 	"fieldname": "block",
		// 	"label": __("Block"),
		// 	"fieldtype": "Link",
		// 	"options": "Block",
		// 	"get_query": function() {
		// 		return {
		// 			filters: {
		// 				'district': frappe.query_report.get_filter_value('district')
		// 			}
		// 		}
		// 	}
		// },
	]
};