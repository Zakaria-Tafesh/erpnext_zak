import frappe


def on_submit(doc, method):
	if doc.material_request_type == 'Material Transfer':
		mat_req_type = doc.material_request_type
		mat_from_warehouse = doc.set_from_warehouse
		mat_to_warehouse = doc.set_warehouse

		doc_stock_entry = frappe.new_doc('Stock Entry')
		doc_stock_entry.stock_entry_type = mat_req_type
		doc_stock_entry.from_warehouse = mat_from_warehouse
		doc_stock_entry.to_warehouse = mat_to_warehouse

		for mat_item in doc.items:
			mat_item_code = mat_item.item_code
			mat_item_qty = mat_item.qty

			doc_stock_entry.append('items', {'item_code': mat_item_code,
												'qty': mat_item_qty,
												})

		doc_stock_entry.insert(ignore_permissions=True)
		doc_stock_entry.submit()
