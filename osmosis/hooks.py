# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "osmosis"
app_title = "osmosis"
app_publisher = "osmosis"
app_description = "osmosis"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "makarand.b@indictranstech.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/osmosis/css/osmosis.css"
# app_include_js = "/assets/osmosis/js/osmosis.js"

# include js, css files in header of web template
# web_include_css = "/assets/osmosis/css/osmosis.css"
# web_include_js = "/assets/osmosis/js/osmosis.js"

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

# before_install = "osmosis.install.before_install"
# after_install = "osmosis.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "osmosis.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"osmosis.tasks.all"
# 	],
# 	"daily": [
# 		"osmosis.tasks.daily"
# 	],
# 	"hourly": [
# 		"osmosis.tasks.hourly"
# 	],
# 	"weekly": [
# 		"osmosis.tasks.weekly"
# 	]
# 	"monthly": [
# 		"osmosis.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "osmosis.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "osmosis.event.get_events"
# }

fixtures = ["Custom Field"]