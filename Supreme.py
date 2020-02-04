import time
import selenium
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#GUI main
# window = TK()
#window.title("Supreme Bot")
#photoHype = PhotoImage(file="hypebeast.jpg")
#Label(window, image=photoHype, bg="white").grid(row=0, column=0, sticky=W)

# Drop Info:
item = "Hanes Tee Shirt"
item_id = "Y7f86dljlaa"
color = "Brown"
color2 = "White"
size = "Medium"

# Personal info

Name = "James Woyevodsky"
Email = "testemail@gmail.com"
Telephone = 2345678910
Address = '123 address lane'
Apt = '5D'
state = 'NY'
Zipcode = 12312
City = 'New York'
Card_Numb = [5,6,2,8,9,0,1,0,4,8,1,4,6,2,7] #fake number you scammers
exp_month = '09'
exp_year = '2023'
CVV = 546


chromedriver = '/Users/michaelwoyevodsky/Desktop/chromedriver'
phantomdriver = '/Users/michaelwoyevodsky/Desktop/phantomjs'
browser = webdriver.Chrome(chromedriver)
browser.get('https://supremenewyork.com/shop/all')
browser.find_element_by_css_selector("img[alt = "+"'"+item_id+"'"+"]").click()
print('Item found')
time.sleep(1)
try:
    try: # color 1
        try: # select size choice 1
            select = Select(browser.find_element_by_css_selector("select[name = 's']"))
            select.select_by_visible_text(size)
            print('Size selected!')
            time.sleep(1)
            browser.find_element_by_css_selector("input[type = 'submit']").click()
            print("Added: "+ color+" in "+size)
        except: # will select and add default size if not completely OOS
            print(size + ' unavailable, selecting current size')
            time.sleep(1)
            browser.find_element_by_css_selector("input[type = 'submit']").click()
            print("Added: "+ color+" in default size")
    except: # select color 2
        print('Color unavailable: Selecting '+color2)
        browser.find_element_by_css_selector("a[data-style-name = "+"'"+color2+"'"+"]").click()
        print(color2+" found!")
        try: # select size choice 1
            time.sleep(1)
            select = Select(browser.find_element_by_css_selector("select[name = 's']"))
            select.select_by_visible_text(size)
            print('Size selected!')
            time.sleep(1)
            browser.find_element_by_css_selector("input[type = 'submit']").click()
            print("Added: "+ color2+" in "+size)
        except:
            # will select and add default size if not completely OOS
            print(size+' unavailable for '+ color2 + ". Default size selected")
            time.sleep(1)
            browser.find_element_by_css_selector("input[type = 'submit']").click()
    print('Item in cart. Going to checkout...')
    # moving to checkout
    time.sleep(.5)
except:
    print('Sold out!')
browser.get('https://www.supremenewyork.com/checkout')    
# Entering Checkout info
print('Entering checkout fields. Prepare for captcha..')
time.sleep(1)


form1 = browser.find_element_by_tag_name('fieldset')
name = browser.find_element_by_name("order[billing_name]")
name.send_keys('James Woyevodsky')

email = browser.find_element_by_id('order_email')
email.click()
email.send_keys(Email)

telephone = browser.find_element_by_id('order_tel')
telephone.send_keys(Telephone)

address = browser.find_element_by_id('bo')
address.send_keys(Address)

apt = browser.find_element_by_id('oba3')
apt.send_keys(Apt)

zipcode = browser.find_element_by_id('order_billing_zip')
zipcode.send_keys(Zipcode)

city = browser.find_element_by_id('order_billing_city')
city.send_keys(City)

# select state 
select2 = Select(browser.find_element_by_css_selector('order_billing_state'))
select2.select_by_visible_text(state)

#move to cc panel
browser.switch_to.default_content()
card_panel = browser.find_element_by_id('cart-cc')
# CC #
card_numb = browser.find_element_by_css_selector("input[placeholder = 'number']")
i = 0
while i < len(Card_Numb):
    card_numb.send_keys(Card_Numb[i])
    i++

# select exp month
select3 = Select(browser.find_element_by_id('credit_card_month'))
select3.select_by_visible_text(exp_month)
# select exp year
select3 = Select(browser.find_element_by_id('credit_card_year'))
select3.select_by_visible_text(exp_year)
#CVV
cvv = bowser.find_element_by_css_selector("input[placeholder = 'CVV']")
cvv.send_keys(CVV)

#window.mainloop()
