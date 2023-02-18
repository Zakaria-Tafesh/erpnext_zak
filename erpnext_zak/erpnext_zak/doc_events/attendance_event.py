import frappe
from frappe.utils import time_diff_in_hours


def validate(doc, method):
	if not doc.check_in or not doc.check_out:
		doc.status = 'Absent'

	else:
		diff = time_diff_in_hours(doc.check_out, doc.check_in)
		doc.hours = diff
		doc.status = 'Present'
