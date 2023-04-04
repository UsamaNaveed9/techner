# Copyright (c) 2023, Techner and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint
from frappe.model.document import Document

class MonthlyTimeSheetAndInvoice(Document):
	def before_save(self):
		if frappe.db.exists("Monthly Time Sheet And Invoice", {"employee": self.employee,"month":self.month,"docstatus":1}):
			frappe.throw(_("{0} TimeSheet and Invoice is submitted already. First Cancelled existing record then save new record").format(self.month))

	def before_submit(self):
		if frappe.db.exists("Monthly Time Sheet And Invoice", {"employee": self.employee,"month":self.month,"docstatus":1}):
			frappe.throw(_("{0} TimeSheet and Invoice is submitted already. First Cancelled existing record then save new record").format(self.month))

