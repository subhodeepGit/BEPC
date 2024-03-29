import requests
import json
import frappe
from datetime import date
import mysql.connector
from mysql.connector import Error

#Accessing data from Azure database
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
                tot_sclass_est_systemcount = x[0]  # Assign the value to the variable
            tot_sclass_est = tot_sclass_est_systemcount
            
            tot_sclass_not_est = - (1232 - tot_sclass_est)

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


    def smart_class_functional():
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
            return tot_sclass_fun_hrs
        
        except Error as e:
            print("Error in fetching data from lastdetails, dailyaggregation table:", e)
        finally:
            # Close the connection
            if mydb.is_connected():
                mydb.close()

except mysql.connector.Error as e:
    print("Error connecting to the database:", e)
    
#Auth Token Generation    
def generate_auth_token():
    api_url = "https://mappeshikshakosh.bihar.gov.in/api/getToken"
    # api_url = "http://150.230.143.55/esk-mobile-api/api/getToken"
    api_key = "U0F0T2NxYnVoNFVUeU8xd25MZmJuWUlFNGlxNWZwT2JKMisya2R6VEZpaGMxUEwwY0w5cjJjT0dmeUtjZm83SEcxTkxlTElCb0hoSDF5M2Z2S2xNNEE9PQ=="
    headers = {
        "api-key": api_key
    }
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        auth_token1 = response.json()
        auth_token = auth_token1['result']['auth_token']
        if auth_token:
            return auth_token
        else:
            print("Failed to retrieve auth token from the API response.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")    
    
#Posting data
def generateICTDataApi():
    url = "https://mappeshikshakosh.bihar.gov.in/api/console/generateICTDataApi"
    # url = "http://150.230.143.55/esk-mobile-api/api/console/generateICTDataApi"

    # Student record
    total_enrolled_boy_dict=frappe.db.sql("""SELECT CONVERT (sum(boys) , INT) as Total_Enr_Boy FROM `tabSchool Survey Form`""", as_dict=True)
    total_enrolled_boy_list = [i['Total_Enr_Boy'] for i in total_enrolled_boy_dict]
    s = [str(i)for i in total_enrolled_boy_list]
    total_enrolled_boy = int("".join(s))
    
    total_enrolled_girl_dict = frappe.db.sql("""SELECT CONVERT (sum(girls) , INT) as "Tot_Enr_Girl" FROM `tabSchool Survey Form`""",as_dict=True)
    total_enrolled_girl_list = [i['Tot_Enr_Girl'] for i in total_enrolled_girl_dict]
    s = [str(i)for i in total_enrolled_girl_list]
    total_enrolled_girl = int("".join(s))
    
    total_enrolled_stu_dict  = frappe.db.sql("""SELECT CONVERT (sum(total_students) , INT) as "Tot_Enr_Stud" FROM `tabSchool Survey Form`""",as_dict=True)
    total_enrolled_stu_list = [i['Tot_Enr_Stud'] for i in total_enrolled_stu_dict]
    s = [str(i)for i in total_enrolled_stu_list]
    total_enrolled_stud = int("".join(s))

    # Theft Log
    tot_sclass_theft_dict  = frappe.db.sql(""" SELECT count(name) as "Tot_SClass_Theft" FROM `tabTheft Case record`; """, as_dict=True)
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

    ## Calling Functions to fetch data from Azure Database
    #  Internet_Services
    tot_net_not_work_tuple = internet_service()
    tot_net_not_work = tot_net_not_work_tuple[0]
    # int(''.join(map(str, tot_net_not_work_tuple)))
    
    tot_net_work_tuple = internet_service()
    tot_net_work = tot_net_not_work_tuple[1]
    # int(''.join(map(str, tot_net_work_tuple)))
    
    tot_net_deploy_tuple = internet_service()
    tot_net_deploy = tot_net_not_work_tuple[2]
    # int(''.join(map(str, tot_net_deploy_tuple)))
    
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

    #Auth Token Calling
    auth_token = generate_auth_token()

    payload = json.dumps({
    "method": "generateICTDataApi",
    "Rpt_Type": "2",
    "Vendor_Code": "V004",
    "Rpt_Dt": "%s"%(today),
    "Tot_SClass_Est": tot_sclass_est,
    "Tot_SClass_Not_Est": tot_sclass_not_est,
    "Tot_Fun_Sclass": tot_fun_sclass,
    "Tot_Not_Fun_Sclass": tot_not_fun_sclass,
    "Tot_Enr_Stud": total_enrolled_stud,
    "Tot_Enr_Boy": total_enrolled_boy,
    "Tot_Enr_Girl": total_enrolled_girl,
    "Tot_SClass_Work_Hrs": tot_sclass_fun_hrs,
    "Tot_SClass_Theft": tot_sclass_theft,
    "Tot_Fir_Log": tot_fir_log,
    "Tot_Rec": tot_rec,
    "Tot_Rep": tot_rep,
    "Tot_Claim": tot_claim,
    "Tot_to_be_Claim": tot_to_be_claim,
    "Tot_Comp_Log": tot_comp_log,
    "Tot_Comp_Open": tot_comp_open,
    "Tot_Comp_Close": tot_comp_close,
    "Tod_Comp_Log": tod_comp_log,
    "Tod_Comp_Close": tod_comp_close,
    "Tot_Net_deploy": tot_net_deploy,
    "Tot_Net_Work": tot_net_work,
    "Tot_Net_Not_Work": tot_net_not_work
    })
      
    headers = {
    'Accept': 'application/json',
    'api-key': 'U0F0T2NxYnVoNFVUeU8xd25MZmJuWUlFNGlxNWZwT2JKMisya2R6VEZpaGMxUEwwY0w5cjJjT0dmeUtjZm83SEcxTkxlTElCb0hoSDF5M2Z2S2xNNEE9PQ==',
    'auth-token' : auth_token,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)    