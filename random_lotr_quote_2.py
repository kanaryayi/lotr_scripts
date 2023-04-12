from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.
# Set up the Chrome driver
service = Service('/snap/bin/chromium.chromedriver')  # replace with the path to your chromedriver

driver = webdriver.Chrome(service=service, options= options)

# Navigate to the page
driver.get('https://www.happycow.org.uk/inspiration/quotes_tolkien_random.shtml')

# Find the quote box element using its class name
quote_box = driver.find_element(By.CSS_SELECTOR,"p.randomQuote.quotelarge")
# Extract the text of the quote
quote_text = quote_box.text

# Print the quote text
print("------------------------------")
print(quote_text)
print("------------------------------")

# Close the browser window
driver.quit()

