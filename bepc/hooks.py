from . import __version__ as app_version

app_name = "bepc"
app_title = "Bepc"
app_publisher = "SOUL"
app_description = "Survey Management System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "soul@soulunileaders.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bepc/css/bepc.css"
# app_include_js = "/assets/bepc/js/bepc.js"

# include js, css files in header of web template
# web_include_css = "/assets/bepc/css/bepc.css"
# web_include_js = "/assets/bepc/js/bepc.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bepc/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	           "issues" : "public/js/issues.js"
			#    "File" : "public/js/file.js"
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

# before_install = "bepc.install.before_install"
# after_install = "bepc.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bepc.uninstall.before_uninstall"
# after_uninstall = "bepc.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bepc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"File": "bepc.bepc.doctype.file.File"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"issues": {
		"validate": "bepc.bepc.doctype.issues.validate",
		"before_save":"bepc.bepc.doctype.issues.before_save"
	},
 	"Service Level Agreement": {
		"validate": "bepc.bepc.doctype.service_level_agreement.validate"
	}
	
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	"cron": {
		"0 16 * * *": [
			"bepc.tasks.post_data",
            "bepc.daily_data.update_daily_data"
		],
        "30 12 * * *":[
            "bepc.azure_data.working_smartclass_hours",
            "bepc.azure_data.functional",
            "bepc.azure_data.nonfunctional"
		]
	}
}
# 	"all": [
# 		"bepc.tasks.all"
# 	],
# 	"daily": [
# 		"bepc.tasks.daily"
# 	],
# 	"hourly": [
# 		"bepc.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bepc.tasks.weekly"
# 	],
# 	"monthly": [
# 		"bepc.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "bepc.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bepc.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "bepc.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


after_migrate = [
        'bepc.patches.migrate_patch.add_roles',
		'bepc.patches.migrate_patch.add_module_profile',
		'bepc.patches.migrate_patch.set_custom_role_permission',
 		'bepc.security.execute',
]

# fixtures = [
# 		{"dt": "Custom DocPerm", "filters": [
# 		[
# 			"parent", "not in", [
# 				"DocType"
# 			]
# 		]
# 	]}
# 	{"dt" : "Workflow"},
	# {"dt": "Workflow Action Master"},
	# {"dt" : "Workflow State"}
	# {"dt" : "Role"},
	# {"dt" : "Module Profile"},
# 	{"dt" : "Role Profile"}
# ]

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