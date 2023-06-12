# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
import datetime
from dateutil import relativedelta
from datetime import date, timedelta
from datetime import datetime

class InternetconsumptionRecord(Document):
    # def form_valid(self):
    # 	d1=self.go_live_date
    # 	d2=self.date
    # 	d3=self.project_end_date
    # 	start_date = d1.strftime("%Y-%m-%d")
    # 	dt_obj = datetime.datetime.strptime(d2,"%Y-%m-%d")
    # 	today_date = datetime.datetime.strftime(dt_obj, "%Y-%m-%d")
    # 	end_date = d3.strftime("%Y-%m-%d")
    # 	if (today_date >= start_date) and (end_date >= today_date):
    # 		pass
    # 	else:
    # 		frappe.throw("Project Date Expired")
    
    def validate(self):
        if self.payment_date == None:
            frappe.throw("Payment date cannot be Empty")
        School_number_validation(self)
        monthly_bill_calculate(self)
        
        if self.from_date == None:
            frappe.throw("Start date cannot be Empty")
        if self.to_date == None:
            frappe.throw("To date cannot be Empty")
            
        if self.from_date > self.to_date:
            frappe.throw("From date cannot be greater than to date")
         
        if self.monthly_bill_amount_lab_1 < 0:
            frappe.throw("Bill amount should be greater than 0")
            
        if self.monthly_bill_amount_lab_2 < 0:
            frappe.throw("Bill amount should be greater than 0")
   
        posting_date = datetime.strptime(self.date, "%Y-%m-%d")
        self.last_payment_date = posting_date + timedelta(days=5)
        today = date.today()
        payment_date = datetime.strptime(self.payment_date, "%Y-%m-%d").date()
        print(type(payment_date))
        if payment_date > today:
            frappe.throw("Payment date cannot be greater than todays date")
           

          # self.form_valid()
        # self.quarter_calculation()

    def quarter_calculation(self):
        start_date = self.go_live_date
        end_date = self.date
        print("\n\n\n\n\n")
        print("End date: ")
        print(type(end_date))
        dt_obj = datetime.datetime.strptime(end_date,"%Y-%m-%d")
        print("dt_obj date: ")
        print(type(dt_obj))
        # today_date = datetime.datetime.strftime(dt_obj, "%Y-%m-%d")
        # print("Today's date: ")
        # print(type(today_date))
        r = relativedelta.relativedelta(dt_obj, start_date)
        month = r.months + (12*r.years)
        print(month)
        if month>=0 and month<=3 :
            print("1")
            self.quarter="Quarter-1"
        elif month>=4 and month<=6 :
            print("2")
            self.quarter="Quarter-2"
        elif month>=7 and month<=9 :
            self.quarter="Quarter-3"
        elif month>=10 and month<=12 :
            self.quarter="Quarter-4"
        elif month>=13 and month<=15 :
            self.quarter="Quarter-5"
        elif month>=16 and month<=18 :
            self.quarter="Quarter-6"
        elif month>=19 and month<=21 :
            self.quarter="Quarter-7"
        elif month>=22 and month<=24 :
            self.quarter="Quarter-8"
        elif month>=25 and month<=27 :
            self.quarter="Quarter-9"
        elif month>=28 and month<=30 :
            self.quarter="Quarter-10"
        elif month>=31 and month<=33 :
            self.quarter="Quarter-11"
        elif month>=34 and month<=36 :
            self.quarter="Quarter-12"
        elif month>=37 and month<=39 :
            self.quarter="Quarter-13"
        elif month>=40 and month<=42 :
            self.quarter="Quarter-14"
        elif month>=43 and month<=45 :
            self.quarter="Quarter-15"
        elif month>=46 and month<=48 :
            self.quarter="Quarter-16"
        elif month>=49 and month<=51 :
            self.quarter="Quarter-17"
        elif month>=52 and month<=54 :
            self.quarter="Quarter-18"
        elif month>=55 and month<=57 :
            self.quarter="Quarter-19"
        elif month>=58 and month<=60 :
            self.quarter="Quarter-20"
        else:
            frappe.throw("Invalid date")

def School_number_validation(self):
    if self.school_contact_number:
        if not (self.school_contact_number).isdigit():
            frappe.throw("Field <b>Asst. Contact Number</b> Accept Digits Only")
        if len(self.school_contact_number)>10:
            frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")
        if len(self.school_contact_number)<10:
            frappe.throw("Field <b>Asst. Contact Number</b> must be 10 Digits")

def monthly_bill_calculate(self):
    self.total_bill_amount = self.monthly_bill_amount_lab_1 + self.monthly_bill_amount_lab_2