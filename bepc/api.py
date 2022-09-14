from os import stat
import frappe

# SUCESS = 200
# NOT_FOUND = 400

# @frappe.whitelist(allow_guest=True)
# def get_api(group):

#     # group = 'Products'

#     items = frappe.db.sql(f"""
#     SELECT name, item_name FROM `tabItem` 
#     WHERE item_group='{group}';""",
#     as_dict=True)
    
#     if(items):
#         status_code = SUCESS
#         body = items
#     else:
#         status_code = NOT_FOUND
#         body = "Item not found"

#     response = dict(
#         status_code = status_code,
#         body = body
#     )

#     return response
#     # print(f"\n\n\n{items}\n\n\n")

# @frappe.whitelist()
# def add_item(code, name, group, uom):
#     add_item = frappe.get_doc({"doctype": "Item",
#         "item_code": code,
#         "item_name": name,
#         "item_group": group,
#         "stoc_uom": uom
#     })

#     add_item.insert()
#     frappe.db.commit()