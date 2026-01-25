from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open quotes website
driver.get("https://quotes.toscrape.com")

wait = WebDriverWait(driver, 15)

# Collect all quote blocks
quotes = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
)

with open("quotes.txt", "w", encoding="utf-8") as f:
    count = 0
    for q in quotes:
        text = q.find_element(By.CLASS_NAME, "text").text
        author = q.find_element(By.CLASS_NAME, "author").text

        count += 1
        f.write(f"{count}. {text}\n")
        f.write(f"   — {author}\n")
        f.write("-" * 50 + "\n")

print("Quotes collected successfully.")
print("Total quotes saved:", count)
print("File created: quotes.txt")

driver.quit()
