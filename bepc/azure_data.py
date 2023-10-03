import frappe
from frappe.model.document import Document
import requests
import json
from datetime import date
import mysql.connector
from mysql.connector import Error

try:
	def working_smartclass_hours():
	
		mydb = mysql.connector.connect(
				host="souliot.mariadb.database.azure.com",
				user="bepcpdf@souliot.mariadb.database.azure.com",
				password="bepc@arm01",
				database="bepcprod"
			)
		try:
			cursor = mydb.cursor()
			cursor.execute("""
			SELECT dailyaggregation.SerialNo, dailyaggregation.SystemDate, dailyaggregation.Duration, schooldata.school, schooldata.block, schooldata.district, schooldata.state, schooldata.computerName, schooldata.Lab 
			FROM dailyaggregation 
			INNER JOIN schooldata 
			ON dailyaggregation.SerialNo = schooldata.SerialNo
			WHERE dailyaggregation.SystemDate = CURDATE();""")
			
			SerialNo = None 
			SystemDate = None
			Duration = None
			school = None
			block = None
			district = None
			state = None
			computerName = None
			Lab = None

			for x in cursor:
				SerialNo = x[0]
				SystemDate = x[1]
				Duration = x[2]
				school = x[3]
				block = x[4]
				district = x[5]
				state = x[6]
				computerName = x[7]
				Lab = x[8]

				doc = frappe.new_doc("Smart Class Functional Time")
				doc.serialno = SerialNo
				doc.system_date = SystemDate
				doc.school = school
				doc.block = block
				doc.district = district
				doc.state = state
				doc.computer_name = computerName
				doc.lab = Lab
				doc.duration = Duration
				doc.save()

		except Error as e:
				print("Error in fetching data from schooldata, dailyaggregation table:", e)
		finally:
				if mydb.is_connected():
					mydb.close()

except mysql.connector.Error as e:
	print("Error connecting to the database:", e) 


try:
	def functional():
	
		mydb = mysql.connector.connect(
				host="souliot.mariadb.database.azure.com",
				user="bepcpdf@souliot.mariadb.database.azure.com",
				password="bepc@arm01",
				database="bepcprod"
			)
		try:
			cursor = mydb.cursor()
			cursor.execute("""
			SELECT lastdetails.SerialNo, lastdetails.Lastactivetime, schooldata.school, schooldata.block, schooldata.district, schooldata.state, schooldata.computerName, schooldata.Lab 
				  FROM lastdetails 
				  INNER JOIN schooldata 
				  ON lastdetails.SerialNo = schooldata.SerialNo 
				  WHERE date(lastdetails.Lastactivetime) = date(now());""")
			SerialNo = None 
			Lastactivetime = None
			school = None
			block = None
			district = None
			state = None
			computerName = None
			Lab = None

			for x in cursor:
				SerialNo = x[0]
				Lastactivetime = x[1]
				school = x[2]
				block = x[3]
				district = x[4]
				state = x[5]
				computerName = x[6]
				Lab = x[7]

				doc = frappe.new_doc("Functional Non Functional")
				doc.serialno = SerialNo
				doc.lastactivetime = Lastactivetime
				doc.school = school
				doc.block = block
				doc.district = district
				doc.state = state
				doc.computer_name = computerName
				doc.lab = Lab
				doc.status = "Functional"
				doc.save()

		except Error as e:
				print("Error in fetching data from lastdetails, schooldata table:", e)
		finally:
				if mydb.is_connected():
					mydb.close()

except mysql.connector.Error as e:
	print("Error connecting to the database:", e) 


try:
	def nonfunctional():
	
		mydb = mysql.connector.connect(
				host="souliot.mariadb.database.azure.com",
				user="bepcpdf@souliot.mariadb.database.azure.com",
				password="bepc@arm01",
				database="bepcprod"
			)
		try:
			cursor = mydb.cursor()
			cursor.execute("""
			SELECT schooldata.SerialNo, schooldata.school, schooldata.block, schooldata.district, schooldata.state, schooldata.computerName, schooldata.Lab 
				  FROM schooldata
				  LEFT JOIN (
					SELECT lastdetails.SerialNo, lastdetails.Lastactivetime, schooldata.school, schooldata.block, schooldata.district, schooldata.state, schooldata.computerName, schooldata.Lab 
					FROM lastdetails 
					INNER JOIN schooldata 
					ON lastdetails.SerialNo = schooldata.SerialNo 
					WHERE date(lastdetails.Lastactivetime) = date(now())
				  ) lastdetails_filtered
				  ON schooldata.SerialNo = lastdetails_filtered.SerialNo
				  WHERE lastdetails_filtered.SerialNo IS NULL;""")
			SerialNo = None 
			school = None
			block = None
			district = None
			state = None
			computerName = None
			Lab = None

			for x in cursor:
				SerialNo = x[0]
				school = x[1]
				block = x[2]
				district = x[3]
				state = x[4]
				computerName = x[5]
				Lab = x[6]

				doc = frappe.new_doc("Functional Non Functional")
				doc.serialno = SerialNo
				doc.lastactivetime = None
				doc.school = school
				doc.block = block
				doc.district = district
				doc.state = state
				doc.computer_name = computerName
				doc.lab = Lab
				doc.status = "Non-Functional"
				doc.save()

		except Error as e:
				print("Error in fetching data from lastdetails, schooldata table:", e)
		finally:
				if mydb.is_connected():
					mydb.close()

except mysql.connector.Error as e:
	print("Error connecting to the database:", e)