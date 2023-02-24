import frappe
from frappe.utils import time_diff_in_hours, flt


def validate(doc, method):
	validate_pos_payments(doc)
	update_sales_invoice_remarks(doc)
	check_discounts(doc)


def validate_pos_payments(doc):
	if doc.is_pos == 0 or (doc.is_pos == 1 and flt(doc.grand_total) <= 0):
		return
	if len(doc.payments) <= 0:
		frappe.throw("Please add at least one payment")
	for payment in doc.payments:
		if flt(payment.amount) <= 0:
			frappe.throw("Payment amount must be greater than 0")


def update_sales_invoice_remarks(doc):
	invoice_notes = []
	for item in doc.items:
		if item.notes and len(item.notes) > 0:
			item.notes = get_clean_notes(item.notes)
			invoice_notes.append(item.notes)
	if len(invoice_notes) <= 0:
		return
	invoice_notes = "\n".join(invoice_notes)
	if len(invoice_notes) > 0:
		doc.remarks = invoice_notes


def get_clean_notes(notes):
	return "\n".join(
		[
			line
			for line in " ".join(notes.split()).split("\n")
			if notes and len(notes) > 0
		]
	)


def check_discounts(doc):
	allow_discount = frappe.get_value("Customer", doc.customer, "allow_discount")
	if allow_discount == 1:
		return
	if doc.discount_amount > 0 or doc.additional_discount_percentage > 0:
		frappe.msgprint("Customer {0} does not allow discount".format(doc.customer))
		doc.is_cash_or_non_trade_discount = 0
		doc.additional_discount_percentage = 0
		doc.discount_amount = 0
