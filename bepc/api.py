from os import stat
from datetime import date
import mysql.connector
import frappe
from mysql.connector import Error

@frappe.whitelist()
def total_enrolled_children():

    total_enrolled_children = frappe.db.sql("""

    SELECT CONVERT (sum(boys) , INT) as "Tot_Enr_Boy", CONVERT (sum(girls) , INT) as "Tot_Enr_Girl", CONVERT (sum(total_students) , INT) as "Tot_Enr_Stud"
    FROM `tabSchool Survey Form`;
    
   """,
    as_dict=True)

    return total_enrolled_children

@frappe.whitelist()
def theft():
    tot_sclass_theft = frappe.db.sql("""
    SELECT count(name) as "Tot_SClass_Theft" FROM `tabTheft Case record`;
    """, as_dict=True)

    tot_fir_log = frappe.db.sql("""
    SELECT count(name) as "Tot_Fir_Log" FROM `tabTheft Case record` where fir_copy IS NOT NULL;
    """, as_dict=True)

    tot_rec = frappe.db.sql(""" 
    SELECT count(name) as "Tot_Rec" FROM `tabTheft Case record` where insurance_claim_receipt IS NOT NULL;
    """, as_dict=True)

    tot_rep = frappe.db.sql("""
    SELECT count(name) as "Tot_Rep" FROM `tabTheft Case record` where delivery_challan_receipt IS NOT NULL;
    """, as_dict=True)

    tot_claim = frappe.db.sql("""
    SELECT count(name) as "Tot_Claim" FROM `tabTheft Case record` where status = "Settled";
    """, as_dict=True)

    tot_to_be_claimed = frappe.db.sql("""
    SELECT count(name) as "Tot_to_be_Claimed" FROM `tabTheft Case record` where status = "Not Settled";
    """, as_dict=True)

    return tot_sclass_theft, tot_fir_log, tot_rec, tot_rep, tot_claim, tot_to_be_claimed

@frappe.whitelist()
def complaint_log():

    today=date.today()

    tot_comp_log = frappe.db.sql("""
    SELECT count(name) as "Tot_Comp_Log" FROM `tabissues`;
    """, as_dict=True)

    tot_comp_open = frappe.db.sql("""
    SELECT count(name) as "Tot_Comp_Open" FROM `tabissues` where status = "Open";
    """, as_dict=True)

    tot_comp_close = frappe.db.sql("""
    SELECT count(name) as "Tot_Comp_Close" FROM `tabissues` where status = "Closed";
    """, as_dict=True)

    tod_comp_log =  frappe.db.sql("""
    SELECT count(name) as "Tod_Comp_Log" FROM `tabissues` where opening_date=%s;
    """, today, as_dict=True)

    tod_comp_close = frappe.db.sql("""
    SELECT count(name) as "Tod_Comp_Close" FROM `tabissues` where status = "Closed" AND opening_date = %s;
    """, today, as_dict=True)
    
    return tot_comp_log, tot_comp_open, tot_comp_close, tod_comp_log, tod_comp_close


try:
    @frappe.whitelist()
    def internet_service():
        mydb = mysql.connector.connect(
            host="souliot.mariadb.database.azure.com",
            user="bepcpdf@souliot.mariadb.database.azure.com",
            password="bepc@arm01",
            database="bepcprod"
        )

        try:
            cursor = mydb.cursor()
            cursor.execute("SELECT COUNT(DISTINCT SerialNo) AS tot_net_not_work FROM schooldata WHERE SerialNo NOT IN (SELECT DISTINCT SerialNo FROM lastdetails);")
            tot_net_not_work = None  # Initialize a variable to store the first count
            for x in cursor:
                tot_net_not_work = x[0]  # Assign the value to the variable

            cursor1 = mydb.cursor()
            cursor1.execute("SELECT COUNT(DISTINCT SerialNo) AS Tot_Net_Work FROM lastdetails;")
            tot_net_work = None  # Initialize a variable to store the second count
            for y in cursor1:
                tot_net_work = y[0]  # Assign the value to the variable

            tot_net_deploy = tot_net_work + tot_net_not_work

            return tot_net_not_work, tot_net_work, tot_net_deploy  # Return the values as a tuple
        except mysql.connector.Error as e:
            print("Error in fetching data from lastdetails table", e)
        finally:
            # Close the connection
            if mydb.is_connected():
                mydb.close()
                print("MySQL connection closed")

    @frappe.whitelist()
    def smart_class_established():
        mydb = mysql.connector.connect(
            host="souliot.mariadb.database.azure.com",
            user="bepcpdf@souliot.mariadb.database.azure.com",
            password="bepc@arm01",
            database="bepcprod"
        )

        try:
            cursor = mydb.cursor()
            cursor.execute("select count(distinct SerialNo) as Tot_SClass_Est from lastdetails")
            tot_sclass_est = None  # Initialize a variable to store the first count
            for x in cursor:
                tot_sclass_est = x[0]  # Assign the value to the variable

            tot_sclass_not_est = 1232 - tot_sclass_est

            cursor1 = mydb.cursor()
            cursor1.execute("select count(distinct SerialNo) as Tot_Fun_SClass from lastdetails where date(Lastactivetime) = date(now())")
            tot_fun_sclass = None  # Initialize a variable to store the second count
            for y in cursor1:
                tot_fun_sclass = y[0]  # Assign the value to the variable

            cursor2 = mydb.cursor()
            cursor2.execute("select count(distinct SerialNo) as Tot_Not_Fun_SClass from lastdetails where date(Lastactivetime) != date(now())")
            tot_not_fun_sclass = None  # Initialize a variable to store the second count
            for z in cursor2:
                tot_not_fun_sclass = z[0]  # Assign the value to the variable
            return tot_sclass_est, tot_sclass_not_est, tot_fun_sclass, tot_not_fun_sclass
        except mysql.connector.Error as e:
            print("Error in fetching data from lastdetails table", e)
        finally:
            # Close the connection
            if mydb.is_connected():
                mydb.close()
                print("MySQL connection closed")

    @frappe.whitelist()
    def smart_class_functional_nonfunctional():
        mydb = mysql.connector.connect(
            host="souliot.mariadb.database.azure.com",
            user="bepcpdf@souliot.mariadb.database.azure.com",
            password="bepc@arm01",
            database="bepcprod"
        )

        try:
            cursor = mydb.cursor()
            cursor.execute("SELECT sum(Duration/60) as tot_sclass_fun_hrs from dailyaggregation where SystemDate = CURDATE()")
            tot_sclass_fun_hrs = None  # Initialize a variable to store the second count
            for x in cursor:
                tot_sclass_fun_hrs = x[0]  # Assign the value to the variable

            cursor1 = mydb.cursor()
            cursor1.execute("SELECT count(distinct SerialNo)*4 as tot_sclass_not_fun_hrs from schooldata where SerialNo not in(select distinct SerialNo from lastdetails)")
            tot_sclass_not_fun_hrs = None  # Initialize a variable to store the second count
            for y in cursor1:
                tot_sclass_not_fun_hrs = y[0]  # Assign the value to the variable
                print(type(y[0]))

            if tot_sclass_fun_hrs is None:
                tot_sclass_fun_hrs = 0
            elif tot_sclass_not_fun_hrs is None:
                tot_sclass_not_fun_hrs = 0
            tot_sclass_work_hrs = tot_sclass_fun_hrs+tot_sclass_not_fun_hrs

            return tot_sclass_fun_hrs, tot_sclass_not_fun_hrs, tot_sclass_work_hrs
        except Error as e:
            print("Error in fetching data from lastdetails, dailyaggregation table:", e)
        finally:
            # Close the connection
            if mydb.is_connected():
                mydb.close()
                print("MySQL connection closed")

except mysql.connector.Error as e:
    print("Error connecting to the database:", e)
