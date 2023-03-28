// Copyright (c) 2023, Techner and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Timesheet Summary"] = {
	"filters": [
		{
			fieldname: "month",
			label: __("Month"),
			fieldtype: "Select",
			options: "January\nFebruary\nMarch\nApril\nMay\nJune\nJuly\nAugust\nSeptember\nOctober\nNovember\nDecember",
			default: "January"
		}
	]
};


  