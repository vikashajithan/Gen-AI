from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://realpython.github.io/fake-jobs/")

wait = WebDriverWait(driver, 15)

jobs = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "card-content"))
)

with open("job_vacancies.txt", "w", encoding="utf-8") as f:
    count = 0
    for job in jobs:
        title = job.find_element(By.TAG_NAME, "h2").text
        company = job.find_element(By.CLASS_NAME, "company").text
        location = job.find_element(By.CLASS_NAME, "location").text

        count += 1
        f.write(f"{count}. {title}\n")
        f.write(f"   Company : {company}\n")
        f.write(f"   Location: {location}\n")
        f.write("-" * 40 + "\n")

print("Job vacancies collected successfully.")
print("Total jobs saved:", count)

driver.quit()
