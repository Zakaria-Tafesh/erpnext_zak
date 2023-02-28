from . import __version__ as app_version

app_name = "erpnext_zak"
app_title = "Erpnext Zak"
app_publisher = "Zakaria"
app_description = "ERPNext For Zakaria"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "zak@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_zak/css/erpnext_zak.css"
# app_include_js = "/assets/erpnext_zak/js/erpnext_zak.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_zak/css/erpnext_zak.css"
# web_include_js = "/assets/erpnext_zak/js/erpnext_zak.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erpnext_zak/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Purchase Order": "public/js/purchase.js",
              "Quotation": "public/js/quotation.js",
              "Sales Invoice": "public/js/sales_invoice.js",
              "Item": "public/js/item.js",
              }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_zak.install.before_install"
# after_install = "erpnext_zak.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "erpnext_zak.uninstall.before_uninstall"
# after_uninstall = "erpnext_zak.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_zak.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Purchase Order": "erpnext_custom.overrides.CustomPurchaseOrder"
}
# Document Events
# ---------------
# Hook on document methods and events


doc_events = {
	"Attendance": {
		"validate": "erpnext_zak.erpnext_zak.doc_events.attendance_event.validate"
	},
	"Sales Invoice": {
		"validate": "erpnext_zak.erpnext_zak.doc_events.sales_invoice.validate"
	},
	"Material Request": {
		"on_submit": "erpnext_zak.erpnext_zak.doc_events.material_request.on_submit"
	},
}
# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"erpnext_zak.tasks.all"
#	],
#	"daily": [
#		"erpnext_zak.tasks.daily"
#	],
#	"hourly": [
#		"erpnext_zak.tasks.hourly"
#	],
#	"weekly": [
#		"erpnext_zak.tasks.weekly"
#	]
#	"monthly": [
#		"erpnext_zak.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "erpnext_zak.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "erpnext_zak.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "erpnext_zak.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"erpnext_zak.auth.validate"
# ]
