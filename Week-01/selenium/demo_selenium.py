from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# CHANGE THIS PATH to where your chromedriver.exe is located
service = Service("C:/selenium/chromedriver.exe")

product_name = "iphone 15"

# ---------------- AMAZON ----------------
driver = webdriver.Chrome(service=service)
driver.get("https://www.amazon.in")
time.sleep(3)

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys(product_name)
search_box.submit()
time.sleep(5)

price_amazon = driver.find_element(By.CLASS_NAME, "a-price-whole").text
print("Amazon Price:", price_amazon)

driver.quit()

# ---------------- FLIPKART ----------------
driver = webdriver.Chrome(service=service)
driver.get("https://www.flipkart.com")
time.sleep(3)

# Close login popup if it appears
try:
    close_btn = driver.find_element(By.XPATH, "//button[text()='✕']")
    close_btn.click()
except:
    pass

time.sleep(2)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(product_name)
search_box.send_keys(Keys.ENTER)
time.sleep(5)

price_flipkart = driver.find_element(By.CLASS_NAME, "_30jeq3").text
print("Flipkart Price:", price_flipkart)

driver.quit()

# ---------------- COMPARE PRICES ----------------

# Clean and convert to numbers
a_price = int(price_amazon.replace(",", "").strip())
f_price = int(price_flipkart.replace("₹", "").replace(",", "").strip())

print("\n--- Price Comparison Result ---")

if a_price < f_price:
    print("Amazon is cheaper")
elif f_price < a_price:
    print("Flipkart is cheaper")
else:
    print("Both prices are same")
