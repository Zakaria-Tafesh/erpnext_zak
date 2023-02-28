import frappe


def execute():
	frappe.db.sql(""" update `tabBom` set department = 'Accounts - ZC' where deparment is not null """)
