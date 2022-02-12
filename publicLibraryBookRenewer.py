# -------TO DO LIST---------------------------------
# Catch Exceptions
# Print If Book Was On Hold And Could Not Be Renewed
# Print If Book Exceeded Max Renewal Limit
# Make GUI
# --------------------------------------------------

# Imports
import time
from selenium import webdriver

# Initialize Browser
chromedriver = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(executable_path=chromedriver, options=options)
browser.get('https://catalog.wakegov.com/MyAccount/Home')

# Login
cardNumberField = browser.find_element_by_id('username')
cardNumberField.send_keys('')  # Library Card Number
pinNumberField = browser.find_element_by_id('password')
pinNumberField.send_keys('')  # Pin
loginButton = browser.find_element_by_id('loginFormSubmit')
loginButton.click()

browser.save_screenshot('screenshot.png')
print(browser.title)


# Renew Books
renewButton = browser.find_element_by_css_selector('.btn.btn-sm.btn-default')
renewButton.click()
browser.switch_to.alert.accept()
browser.switch_to.alert.accept()
time.sleep(5)

# Get Book Data
books = browser.find_elements_by_css_selector('.col-xs-9.col-sm-8.col-md-9')
bookData = []
for book in books:
    bookData.append({
        'Title': book.find_element_by_class_name('result-title').text,
        'Author': book.find_elements_by_css_selector('.result-value.col-tn-8.col-lg-9')[0].text,
        'Format': book.find_elements_by_css_selector('.result-value.col-tn-8.col-lg-9')[2].text,
        'Times Renewed': book.find_elements_by_css_selector('.result-value.col-tn-8.col-lg-9')[6].text,
        'Date Checked Out': book.find_elements_by_css_selector('.result-value.col-tn-8.col-lg-9')[1].text,
        'Date Due': book.find_elements_by_css_selector('.result-value.col-tn-8.col-lg-9')[5].text
    })

# Print Book Data
print('-'*39)
for book in bookData:
    for datum in book:
        print(datum + ': ' + book.get(datum))
    print('-'*39)

# Cleanup
browser.quit()
