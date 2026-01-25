import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Step 1: Browser open
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Step 2: Open Wikipedia home
        await page.goto("https://www.wikipedia.org", timeout=60000)
        await page.wait_for_timeout(3000)

        # Step 3: Search box-ல "Vijay" type பண்ணு
        search_box = page.locator('input[name="search"]')
        await search_box.type("Vijay actor", delay=150)

        # Step 4: Press Enter (search)
        await search_box.press("Enter")

        # Wait for search results page
        await page.wait_for_timeout(3000)

        # Step 5: Vijay page link-ஐ click பண்ணு
        # This clicks the first result link
        first_result = page.locator("//ul[@class='mw-search-results']//li//a").first
        await first_result.click()

        # Wait for Vijay page to load
        await page.wait_for_timeout(5000)

        # Step 6: Vijay page-ல main content paragraphs select பண்ணு
        content = page.locator("#mw-content-text p")
        paragraphs = await content.all_inner_texts()

        # Step 7: Text file create & save
        with open("vijay_wikipedia.txt", "w", encoding="utf-8") as f:
            for para in paragraphs:
                if para.strip():
                    f.write(para + "\n\n")

        print("✅ எல்லா ஸ்டெப்பும் முடிஞ்சது.")
        print("📄 File created: vijay_wikipedia.txt")

        await browser.close()

asyncio.run(main())