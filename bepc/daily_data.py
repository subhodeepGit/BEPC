# Copyright (c) 2023, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests
import json
from datetime import date
import mysql.connector
from mysql.connector import Error

try:
	def internet_service():
		mydb = mysql.connector.connect(
			host="souliot.mariadb.database.azure.com",
			user="bepcpdf@souliot.mariadb.database.azure.com",
			password="bepc@arm01",
			database="bepcprod"
		)

		try:
			cursor = mydb.cursor()
			cursor.execute("select count(SerialNo) as Tot_SClass_Est from schooldata")
			tot_net_deploy = None  # Initialize a variable to store the first count
			for x in cursor:
				tot_net_deploy = x[0]  # Assign the value to the variable

			# cursor1 = mydb.cursor()
			# cursor1.execute("select count(distinct SerialNo) as Tot_Fun_SClass from lastdetails")
			# tot_net_work = None  # Initialize a variable to store the second count
			# for y in cursor1:
			#     tot_net_work = y[0]  # Assign the value to the variable
			
			# tot_net_not_work = tot_net_deploy - tot_net_work

			return tot_net_deploy 
			# return tot_net_not_work, tot_net_work, tot_net_deploy  # Return the values as a tuple
		
		except mysql.connector.Error as e:
			print("Error in fetching data from lastdetails table", e)
		finally:
			# Close the connection
			if mydb.is_connected():
				mydb.close()


	def smart_class_established():
		mydb = mysql.connector.connect(
			host="souliot.mariadb.database.azure.com",
			user="bepcpdf@souliot.mariadb.database.azure.com",
			password="bepc@arm01",
			database="bepcprod"
		)

		try:
			cursor = mydb.cursor()
			cursor.execute("select count(SerialNo) as Tot_SClass_Est from schooldata")
			tot_sclass_est = None  # Initialize a variable to store the first count
			for x in cursor:
				tot_sclass_est_systemcount = x[0]  # Assign the value to the variable
			tot_sclass_est = tot_sclass_est_systemcount
			
			tot_sclass_not_est = (2464 - tot_sclass_est)

			cursor1 = mydb.cursor()
			cursor1.execute("select count(distinct SerialNo) as Tot_Fun_SClass from lastdetails where date(Lastactivetime) = date(now())")
			tot_fun_sclass = None  # Initialize a variable to store the second count
			for y in cursor1:
				tot_fun_sclass = y[0]  # Assign the value to the variable
				
			if tot_fun_sclass is None:
				tot_fun_sclass = 0

			# cursor2 = mydb.cursor()
			# cursor2.execute("select count(distinct SerialNo) as Tot_Not_Fun_SClass from lastdetails where date(Lastactivetime) != date(now())")
			# tot_not_fun_sclass = None  # Initialize a variable to store the second count
			# for z in cursor2:
			#     tot_not_fun_sclass = z[0]  # Assign the value to the variable
			
			tot_not_fun_sclass = tot_sclass_est - tot_fun_sclass
			
			# print(tot_sclass_est, tot_sclass_not_est, tot_fun_sclass, tot_not_fun_sclass)
			return tot_sclass_est, tot_sclass_not_est, tot_fun_sclass, tot_not_fun_sclass
		
		except mysql.connector.Error as e:
			print("Error in fetching data from lastdetails table", e)
		finally:
			# Close the connection
			if mydb.is_connected():
				mydb.close()

	#round(area, 2)
	def smart_class_functional():
		mydb = mysql.connector.connect(
			host="souliot.mariadb.database.azure.com",
			user="bepcpdf@souliot.mariadb.database.azure.com",
			password="bepc@arm01",
			database="bepcprod"
		)

		# tot_fun_sclass_tuple = smart_class_established()
		# tot_fun_sclass = tot_fun_sclass_tuple[2]

		tot_fun_sclass_tuple = smart_class_established()
		tot_fun_sclass = tot_fun_sclass_tuple[2]
	
		try:
			cursor = mydb.cursor()
			cursor.execute("SELECT sum(Duration/60) as tot_sclass_fun_hrs from dailyaggregation where SystemDate = CURDATE()")
			tot_sclass_fun_hrs = None  # Initialize a variable to store the second count
			for x in cursor:
				tot_sclass_fun = x[0]  # Assign the value to the variable
				# print(tot_sclass_fun)
				if tot_fun_sclass == 0:
					total_sclass_fun_hrs = 0
				else:
					total_sclass_fun_hrs = tot_sclass_fun/tot_fun_sclass
				# print(total_sclass_fun_hrs)
				for_total_sclass_fun = ("{:.2f}".format(total_sclass_fun_hrs))
				# print(float(total_sclass_fun_hrs))
				return float(for_total_sclass_fun)
		
		except Error as e:
			print("Error in fetching data from lastdetails, dailyaggregation table:", e)
		finally:
			# Close the connection
			if mydb.is_connected():
				mydb.close()

except mysql.connector.Error as e:
	print("Error connecting to the database:", e)

def update_daily_data():
	
# Student record
	total_enrolled_boy_dict=frappe.db.sql("""SELECT CONVERT (sum(boys) , INT) as Total_Enr_Boy FROM `tabSchool Survey Form`""", as_dict=True)
	total_enrolled_boy_list = [i['Total_Enr_Boy'] for i in total_enrolled_boy_dict]
	s = [str(i)for i in total_enrolled_boy_list]
	total_enrolled_boy = int("".join(s))
	
	total_enrolled_girl_dict = frappe.db.sql("""SELECT CONVERT (sum(girls) , INT) as "Tot_Enr_Girl" FROM `tabSchool Survey Form`""",as_dict=True)
	total_enrolled_girl_list = [i['Tot_Enr_Girl'] for i in total_enrolled_girl_dict]
	s = [str(i)for i in total_enrolled_girl_list]
	total_enrolled_girl = int("".join(s))

	total_enrolled_stud = total_enrolled_boy+total_enrolled_girl

	# Theft Log
	tot_sclass_theft_dict  = frappe.db.sql(""" SELECT count(DISTINCT item) as Tot_SClass_Theft FROM `tabTheft Case record`; """, as_dict=True)
	tot_sclass_theft_list = [i['Tot_SClass_Theft'] for i in tot_sclass_theft_dict]
	s = [str(i)for i in tot_sclass_theft_list]
	tot_sclass_theft = int("".join(s))
	
	tot_fir_log_dict  = frappe.db.sql(""" SELECT count(name) as "Tot_Fir_Log" FROM `tabTheft Case record` where fir_copy IS NOT NULL; """, as_dict=True)
	tot_fir_log_list = [i['Tot_Fir_Log'] for i in tot_fir_log_dict]
	s = [str(i)for i in tot_fir_log_list]
	tot_fir_log = int("".join(s))
	
	tot_rec_dict  = frappe.db.sql(""" SELECT count(name) as "Tot_Rec" FROM `tabTheft Case record` where insurance_claim_receipt IS NOT NULL; """, as_dict=True)
	tot_rec_list = [i['Tot_Rec'] for i in tot_rec_dict]
	s = [str(i)for i in tot_rec_list]
	tot_rec = int("".join(s))
	
	tot_rep_dict  = frappe.db.sql(""" SELECT count(name) as "Tot_Rep" FROM `tabTheft Case record` where delivery_challan_receipt IS NOT NULL; """, as_dict=True)
	tot_rep_list = [i['Tot_Rep'] for i in tot_rep_dict]
	s = [str(i)for i in tot_rep_list]
	tot_rep = int("".join(s))
	
	tot_claim_dict  = frappe.db.sql(""" SELECT count(name) as "Tot_Claim" FROM `tabTheft Case record` where status = "Settled"; """, as_dict=True)
	tot_claim_list = [i['Tot_Claim'] for i in tot_claim_dict]
	s = [str(i)for i in tot_claim_list]
	tot_claim = int("".join(s))
	
	tot_to_be_claim_dict  = frappe.db.sql(""" SELECT count(name) as "Tot_to_be_Claim" FROM `tabTheft Case record` where status = "Not Settled"; """, as_dict=True)
	tot_to_be_claim_list = [i['Tot_to_be_Claim'] for i in tot_to_be_claim_dict]
	s = [str(i)for i in tot_to_be_claim_list]
	tot_to_be_claim = int("".join(s))

	# Complaint Log
	today = date.today()
	tot_comp_log_dict  = frappe.db.sql(""" SELECT count(name) as "Tot_Comp_Log" FROM `tabissues`; """, as_dict=True)
	tot_comp_log_list = [i['Tot_Comp_Log'] for i in tot_comp_log_dict]
	s = [str(i)for i in tot_comp_log_list]
	tot_comp_log = int("".join(s))
	
	tot_comp_open_dict  = frappe.db.sql(""" SELECT count(name) as "Tot_Comp_Open" FROM `tabissues` where status = "Open"; """, as_dict=True)
	tot_comp_open_list = [i['Tot_Comp_Open'] for i in tot_comp_open_dict]
	s = [str(i)for i in tot_comp_open_list]
	tot_comp_open = int("".join(s))
	
	tot_comp_close_dict  = frappe.db.sql(""" SELECT count(name) as "Tot_Comp_Close" FROM `tabissues` where status = "Closed"; """, as_dict=True)
	tot_comp_close_list = [i['Tot_Comp_Close'] for i in tot_comp_close_dict]
	s = [str(i)for i in tot_comp_close_list]
	tot_comp_close = int("".join(s))
	
	tod_comp_log_dict  =  frappe.db.sql(""" SELECT count(name) as "Tod_Comp_Log" FROM `tabissues` where opening_date=%s; """, today, as_dict=True)
	tod_comp_log_list = [i['Tod_Comp_Log'] for i in tod_comp_log_dict]
	s = [str(i)for i in tod_comp_log_list]
	tod_comp_log = int("".join(s))
	
	tod_comp_close_dict  = frappe.db.sql(""" SELECT count(name) as "Tod_Comp_Close" FROM `tabissues` where status = "Closed" AND opening_date = %s; """, today, as_dict=True)
	tod_comp_close_list = [i['Tod_Comp_Close'] for i in tod_comp_close_dict]
	s = [str(i)for i in tod_comp_close_list]
	tod_comp_close = int("".join(s))
		

	# Internet deploy
	# tot_net_not_work, tot_net_work

	tot_net_work_dict = frappe.db.sql("""SELECT count(name)*2 as "Tot_Net_Work" from `tabSchool` where lab_1_sim_number IS NOT NULL AND lab_2_sim_number IS NOT NULL;""", as_dict=True)
	tot_net_work_list = [i['Tot_Net_Work'] for i in tot_net_work_dict]
	s = [str(i)for i in tot_net_work_list]
	tot_net_work = int("".join(s))

	tot_net_not_work_dict = frappe.db.sql("""SELECT count(name)*2 as "Tot_Net_Not_Work" from `tabSchool` where lab_1_sim_number IS NULL AND lab_2_sim_number IS NULL;""", as_dict=True)
	tot_net_not_work_list = [i['Tot_Net_Not_Work'] for i in tot_net_not_work_dict]
	s = [str(i)for i in tot_net_not_work_list]
	tot_net_not_work = int("".join(s))  

	## Calling Functions to fetch data from Azure Database
	#  Internet_Services
	tot_net_deploy = internet_service()
	
	# smart_class_established
	tot_sclass_est_tuple = smart_class_established()
	# tot_sclass_est = int(''.join(map(str, tot_sclass_est_tuple))) 
	tot_sclass_est = tot_sclass_est_tuple[0]

	
	tot_sclass_not_est_tuple = smart_class_established()
	tot_sclass_not_est = tot_sclass_not_est_tuple[1]
	# tot_sclass_not_est = int(''.join(map(str, tot_sclass_not_est_tuple)))
	
	tot_fun_sclass_tuple = smart_class_established()
	tot_fun_sclass = tot_fun_sclass_tuple[2]
	# tot_fun_sclass = int(''.join(map(str, tot_fun_sclass_tuple)))
	
	tot_not_fun_sclass_tuple = smart_class_established()
	tot_not_fun_sclass = tot_not_fun_sclass_tuple[3]
	# tot_not_fun_sclass = int(''.join(map(str, tot_not_fun_sclass_tuple)))
	
	# smart_class_functional
	tot_sclass_fun_hrs = smart_class_functional()

	#data_save_to_doctype
	daily_data = frappe.new_doc("Daily data sent from API")
	daily_data.method = "generateICTDataApi"
	daily_data.rpt_type = "2"
	daily_data.vendor_code = "V004"
	daily_data.rpt_dt = "%s"%(today)
	daily_data.tot_sclass_est = tot_sclass_est
	daily_data.tot_sclass_not_est = tot_sclass_not_est
	daily_data.tot_fun_sclass = tot_fun_sclass
	daily_data.tot_not_fun_sclass = tot_not_fun_sclass
	daily_data.tot_enr_stud = total_enrolled_stud
	daily_data.tot_enr_boy = total_enrolled_boy
	daily_data.tot_enr_girl = total_enrolled_girl
	daily_data.tot_sclass_work_hrs = tot_sclass_fun_hrs
	daily_data.tot_sclass_theft = tot_sclass_theft
	daily_data.tot_fir_log = tot_fir_log
	daily_data.tot_rec = tot_rec
	daily_data.tot_rep = tot_rep
	daily_data.tot_claim = tot_claim
	daily_data.tot_to_be_claim = tot_to_be_claim
	daily_data.tot_comp_log = tot_comp_log
	daily_data.tot_comp_open = tot_comp_open
	daily_data.tot_comp_close = tot_comp_close
	daily_data.tod_comp_log = tod_comp_log
	daily_data.tod_comp_close = tod_comp_close
	daily_data.tot_net_deploy = tot_net_deploy
	daily_data.tot_net_work = tot_net_work
	daily_data.tot_net_not_work = tot_net_not_work
	daily_data.save()