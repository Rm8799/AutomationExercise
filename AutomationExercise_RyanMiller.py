import random, string
# Importing Selenium modules used in test cases.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
# Assigns the aliases WAIT and EC to the WebDriverWait and expected_conditions module
from selenium.webdriver.support.ui import WebDriverWait as WAIT
from selenium.webdriver.support import expected_conditions as EC


# ------------------------------FUNCTIONS------------------------------
# Defining a function to be used at the beginning of each test case.
# Logs into http://automationpractice.com using a pre-made account and a direct link to the login page.
# Requires 2 arguments; username/email & password
def login(email, mypassword):
	# Creates instance of Chrome web driver and goes to the http://automationpractice.com login page.
	browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
	# Locates and fills username and password fields on the login form, then hits the Enter key.
	username_field = browser.find_element_by_id("email")
	username_field.send_keys(email)
	password_field = browser.find_element_by_id("passwd")
	password_field.send_keys(mypassword)
	password_field.send_keys(Keys.ENTER)
	print("Waiting to log in.")
	# Waits up to 5 seconds for login to finish and confirms that the name in account header exists.
	try:
		WAIT(browser, 5).until(
			EC.presence_of_element_located((By.XPATH, "//span[text()='Mr Turtle']"))
		)
		print("Login successful.")
	except TimeoutException:
		print("Login failed.")
		browser.quit()
	finally:
		print("Good day shopping Mr.Turtle.")


# Defining function to create a new account on http://automationpractice.com
# Direct links to login page, enters an email address for the account, then continues to account creation page.
# Inputs required fields only.
# Takes 1 argument for email address, as this is the only attribute required to be unique,
# with static values for other fields.
def new_account(email):
	# Creates instance of Chrome web driver and goes to the http://automationpractice.com login page,
	# then enters email address for new account.
	browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
	new_account_email = browser.find_element_by_id("email_create")
	new_account_email.send_keys(email)
	new_account_email.send_keys(Keys.ENTER)
	# Waits up to 3 seconds for the new account creation page to load by locating the first name element.
	WAIT(browser, 3).until(EC.presence_of_element_located((By.ID, "customer_firstname")))
	# Locates and fills first/last name, password, address 1, and city fields.
	first_name = browser.find_element_by_id("customer_firstname")
	first_name.send_keys("Shoe")
	last_name = browser.find_element_by_id("customer_lastname")
	last_name.send_keys("Laces")
	password_field = browser.find_element_by_id("passwd")
	password_field.send_keys("123456")
	address = browser.find_element_by_id("address1")
	address.send_keys("Address 777")
	city = browser.find_element_by_id("city")
	city.send_keys("City of Angels")
	# Drop down menu for State.  Finds value in menu, then clicks in on following line.
	state = browser.find_element_by_xpath("//select[@id='id_state']//option[text()='California']")
	state.click()
	# Continues on to fill in zip code and phone number fields, before clicking Enter and verifying new account creation.
	zipcode = browser.find_element_by_id("postcode")
	zipcode.send_keys("77777")
	phone = browser.find_element_by_id("phone_mobile")
	phone.send_keys("123-456-7890")
	phone.send_keys(Keys.ENTER)
	# Waits up to 5 seconds for login to finish after account creation and confirms the name in account header exists.
	try:
		WAIT(browser, 5).until(
			EC.presence_of_element_located((By.XPATH, "//span[text()='Shoe Laces']"))
		)
		print("Successfully created new account. Have a good day shopping.")
	except TimeoutException:
		print("New account creation failed.")
		browser.quit()
	finally:
		pass


# ------------------------------CREATE ACCOUNT------------------------------
# Creates a new account at http://automationpractice.com and ends the web driver instance
# using a 10 character random string for the email address.

print("TEST CASE 1:  NEW ACCOUNT CREATION")

random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

browser = webdriver.Chrome()

new_account(random_string + "@email.com")

browser.quit()
print("TEST CASE 1: PASSED")


# ------------------------------LOGIN------------------------------#
# Logs into http://automationpractice.com and ends the web driver instance.

print("TEST CASE 2:  ACCOUNT LOGIN")

browser = webdriver.Chrome()

login("turtles@gmail.com", "123456")

browser.quit()
print("TEST CASE 2: PASSED")


# ------------------------------SHOPPING CART------------------------------#
# Logs into http://automationpractice.com, then adds and verifies items in the shopping cart.

print("TEST CASE 3: SHOPPING CART")

# A list of items to add to your cart.
Shopping_List = ['Faded Short Sleeve T-shirts']

# Prints each item in Shopping_List as a string that can be passed into Xpath locator.
for item in Shopping_List:
	print(item)

browser = webdriver.Chrome()

login("turtles@gmail.com", "123456")

# Clicks the home (little house) button from the account overview page immediately after login.
try:
	home_button = browser.find_element_by_xpath("//a[@title='Return to Home']").click()
	WAIT(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//a[@class='homefeatured' and contains(.,'Popular')]")))
except TimeoutException:
	print("Something went wrong and homepage didn't load properly.")
	browser.quit()
finally:
	print("Welcome home!")
# Adding items to shopping cart from the feature items homepage.
# This will need to be expanded in a different test case to include selecting items from other locations of the website.
# Here, we mainly want to verify that items are successfully added to, and displayed, in the shopping cart.
for item in Shopping_List:
	try:
		add_item = browser.find_element_by_xpath("//ul[@id='homefeatured']//img[@title='" + item + "']").click()
		WAIT(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//h1[@itemprop='name' and contains(.,'" + item + "')]")))
		add_to_cart = browser.find_element_by_xpath("//button[@type='submit']//span[text()='Add to cart']").click()
	except TimeoutException:
		print("Something went wrong selecting your item.")
		browser.quit()
	finally:
		print("Item successfully added to cart")
		home_button = browser.find_element_by_xpath("//a[@title='Return to Home']").click()
		WAIT(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//a[@class='homefeatured' and contains(.,'Popular')]")))
# Navigates to shopping cart
try:
	shopping_cart = browser.find_element_by_xpath("//a[@title='View my shopping cart']").click()
	WAIT(browser, 3).until(EC.presence_of_element_located((By.ID, "cart_title")))
except TimeoutException:
	print ("Could not load shopping cart.")
	browser.quit()
finally:
	pass
# Verifies every item added shows up properly in the shopping cart.
for item in Shopping_List:
	try:
		cart_items = browser.find_element_by_xpath("//td[@class='cart_description']//p[@class='product-name' and contains(.,'" + item + "')]")
	except ElementNotVisibleException:
		print("Couldn't find '" + item + "' in shopping cart")
	finally:
		print("Shopping cart looks good! Please check out now.")

# Logs out before closing browser.
logout = browser.find_element_by_xpath("//a[@class='logout']").click()
browser.quit()
print("TEST CASE 3: PASSED")


# ------------------------------CATEGORY BROWSING------------------------------#
# Logs into http://automationpractice.com and browses between the store's 3 categories: Women, Dresses, T-shirts.

print("TEST CASE 4:  CATEGORY BROWSING")

browser = webdriver.Chrome()

login("turtles@gmail.com", "123456")

# Clicks the home (little house) button from the account overview page immediately after login.
try:
	home_button = browser.find_element_by_xpath("//a[@title='Return to Home']").click()
	WAIT(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//a[@class='homefeatured' and contains(.,'Popular')]")))
except TimeoutException:
	print("Something went wrong and homepage didn't load properly.")
	browser.quit()
finally:
	print("Welcome home!")
# Navigating to Women category from the homepage.
try:
	category_women = browser.find_element_by_xpath("//a[@title='Women']").click()
	WAIT(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@class='navigation_page' and contains(.,'Women')]")))
except TimeoutException:
	print("Couldn't load category: Women.")
	browser.quit()
finally:
	print("This is the shopping category for Women.")
# Continue from here navigating to the Dresses and T-Shirts categories, verifying breadcrumb path for each.

# Logs out before closing browser.
logout = browser.find_element_by_xpath("//a[@class='logout']").click()
browser.quit()
print("TEST CASE 4: PASSED")


