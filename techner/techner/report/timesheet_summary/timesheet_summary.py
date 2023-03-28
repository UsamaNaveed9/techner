# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe
from frappe import _, msgprint


def execute(filters=None):

	columns = get_columns(filters)
	data = get_entries(filters)

	for rec in data:
		if rec.timesheet:
			rec["u_timesheet"] = frappe.db.get_value("File", {"attached_to_doctype":"Monthly Time Sheet And Invoice", "attached_to_name":rec.t_name, "attached_to_field":"timesheet", "file_url":rec.timesheet}, "name")

		if rec.invoice:
			rec["u_invoice"] = frappe.db.get_value("File", {"attached_to_doctype":"Monthly Time Sheet And Invoice", "attached_to_name":rec.t_name, "attached_to_field":"invoice","file_url":rec.invoice}, "name")

	return columns, data


def get_columns(filters):

	columns = [
		{
			"label": _("Employee"),
			"options": "Employee",
			"fieldname": "name",
			"fieldtype": "Link",
			"width": 140,
		},
		{
			"label": _("Employee Name"),
			"fieldname": "employee_name",
			"fieldtype": "Data",
			"width": 140,
		},
		{
			"label": _("Month"),
			"fieldname": "month",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"label": _("Date"),
		 	"fieldname": "date",
			"fieldtype": "Date",
			"width": 100
		},
		{
			"label": _("Number of Days"),
			"fieldname": "number_of_days",
			"fieldtype": "Float",
			"width": 140,
		},
		{
			"label": _("Timesheet PDF"),
			"fieldname": "u_timesheet",
			"fieldtype": "Link",
			"options": "File",
			"width": 160,
		},
		{
			"label": _("Invoice PDF"),
			"fieldname": "u_invoice",
			"fieldtype": "Link",
			"options": "File",
			"width": 160,
		}
	]

	return columns


def get_entries(filters):

	# conditions = get_conditions(filters)
	entries = frappe.db.sql(
		"""
		SELECT
			e.name, e.employee_name, m.month, m.date, m.number_of_days, m.timesheet, m.invoice, m.name as t_name
		FROM
			`tabEmployee` e 
		LEFT JOIN `tabMonthly Time Sheet And Invoice` m	
		ON e.name = m.employee and m.month = %(month)s and m.docstatus = 1 
		WHERE e.status = 'Active'
		""".format(filters.get("month")
		),
		filters,
		as_dict=1,
	)

	return entries
