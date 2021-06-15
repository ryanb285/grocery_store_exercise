import os
import operator
import dotenv
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TAX_RATE = os.getenv("TAX")
STORE_NAME = os.getenv("STORE")
STORE_SITE = os.getenv("WEBSITE")



products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


print("Please input a product ID or type 'DONE' ")


now = datetime.now()
date_time = now.strftime("%Y-%m-%d, %H:%M")
#adapted from - https://www.programiz.com/python-programming/datetime/strftime

#allowed_ids = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#to do email you need to add sendgrid package

total_price = 0
selected_ids = []

while True:
    selected_id = input("Please select a valid product ID: ")
    if selected_id.upper() == "DONE":
        break
    else:
        selected_ids.append(selected_id)

print("-------------------")
print(STORE_NAME)
print(STORE_SITE)
print("-------------------")

print("CHECKOUT AT: " + date_time)

print("-------------------")
print("SELECTED PRODUCTS: ")
try:
    for selected_id in selected_ids:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0]
        total_price = total_price + matching_product["price"]
        print("..." + matching_product["name"] + " " + "("+str(to_usd((matching_product["price"])))+")")
except IndexError:
    print("INVALID PRODUCT ID, PLEASE RE-ENTER THE ITEM")


            

print("-------------------")

print("SUBTOTAL: " + str(to_usd(total_price)))
tax = float(total_price) * float(TAX_RATE)
print("TAX: " + str(to_usd(tax)))
overall_cost = float(total_price) + float(tax)
print("TOTAL: " + str(to_usd(overall_cost)))
print("-------------------")
print("THANKS, SEE YOU AGAIN SOON!")

#import os
#import dotenv import load_dotenv
#import sendgrid
#from sendgrid.helpers.mail import Mail, Email, To, Content

#load_dotenv()

#EMAIL_KEY = os.getenv("API_KEY")
#MY_EMAIL = os.getenv("SENDER_EMAIL")

#sg = sendgrid.SendGridAPIClient(EMAIL_KEY)
#from_email = Email(MY_EMAIL)  
#their_email = input("If you'd like an email receipt, please type your email address here: ")
#to_email = To(their_email)  
#subject = "Receipt from today's purchase"
#content = Content( "TEST")


#mail = Mail(from_email, to_email, subject, content)
#mail_json = mail.get()
#response = sg.client.mail.send.post(request_body=mail_json)
#print(response.status_code)
#print(response.headers)
