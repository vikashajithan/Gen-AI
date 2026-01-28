# Week 01 – Python Foundations & Automation Projects

This week focuses on building strong foundations in Python and learning different automation and web application tools through hands-on projects.

## Technologies Used

- Python  
- Flask  
- Playwright  
- Selenium  
- PyAutoGUI  
- Streamlit  

---

## Projects Overview

### 1. YouTube Automation with Flask

**Description:**  
A Flask web application that triggers a desktop automation script to open YouTube and search for a specific query when a button is clicked.

**What It Does:**
- Starts a Flask web server  
- Provides a simple web page with a button  
- On button click:
  - Opens Chrome  
  - Opens YouTube  
  - Types a search query  
  - Clicks the first video  

**Key Learning:**
- Integrating Flask with desktop automation  
- Triggering automation from a web interface  

---

### 2. Wikipedia Scraper using Playwright

**Description:**  
An automation script that searches for an actor on Wikipedia, extracts the page content, and saves it into a text file.

**What It Does:**
- Opens Chromium browser  
- Searches for "Vijay actor"  
- Opens the first result  
- Extracts all main paragraphs  
- Saves data into `vijay_wikipedia.txt`  

**Key Learning:**
- Browser automation using Playwright  
- Async programming in Python  
- Web scraping and file handling  

---

### 3. YouTube Automation using PyAutoGUI

**Description:**  
A desktop automation script that opens Chrome, goes to YouTube, searches for a query, and opens the first video result.

**What It Does:**
- Opens Windows Run dialog  
- Launches Chrome  
- Opens YouTube  
- Types search query  
- Clicks the first video  

**Key Learning:**
- Mouse and keyboard automation  
- Coordinate-based screen automation  
- Desktop task automation  

---

### 4. Quotes Scraper using Selenium

**Description:**  
A web scraping script that collects quotes and author names from a website and saves them into a text file.

**What It Does:**
- Opens quotes.toscrape.com  
- Extracts quote text and authors  
- Saves all data into `quotes.txt`  

**Key Learning:**
- Locating elements using Selenium  
- Extracting structured data  
- Writing scraped data to files  

---

### 5. Job Vacancies Scraper using Selenium

**Description:**  
A web scraping project that extracts job vacancy details from a job portal and stores them in a text file.

**What It Does:**
- Opens fake job portal  
- Extracts job title, company, and location  
- Saves results into `job_vacancies.txt`  

**Key Learning:**
- Scraping multiple data fields  
- Handling multiple elements on a page  
- Real-world data extraction workflow  

---

### 6. Product Price Comparison using Selenium

**Description:**  
An automation script that compares the price of a product between Amazon and Flipkart.

**What It Does:**
- Searches product on Amazon  
- Extracts product price  
- Searches same product on Flipkart  
- Extracts product price  
- Compares both prices and prints the cheaper platform  

**Key Learning:**
- Multi-website automation  
- Form submission and key events  
- Data cleaning and comparison logic  

---

### 7. Online Quiz Application using Streamlit

**Description:**  
An interactive online quiz application with multiple-choice questions, scoring system, and result summary.

**What It Does:**
- Displays one question at a time  
- Allows user to select answers  
- Tracks score using session state  
- Shows final score and percentage  
- Displays correct answers  
- Allows quiz restart  

**Key Learning:**
- Building interactive UI with Streamlit  
- Managing session state  
- Creating a complete mini application  

---

## Overall Learning Outcome of Week 01

By the end of Week 01, I gained hands-on experience in:

- Writing clean Python automation scripts  
- Automating browsers and desktop tasks  
- Scraping data from real websites  
- Building simple web and UI applications  
- Managing project structure in GitHub  

---

**Author:** Vikash  
**Program:** Generative AI – 60 Days Learning Journey  
**Week:** 01
