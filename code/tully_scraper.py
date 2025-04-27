import re
from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.tullysgoodtimes.com/menus/")
    
        extracted_items = []

        titles = page.query_selector_all("h3.foodmenu__menu-section-title")
        for title in titles:
            title_text = title.inner_text()
            print("MENU SECTION:", title_text)

            # Find the sibling's sibling
            row = title.evaluate_handle("node => node.nextElementSibling?.nextElementSibling")

            if row:
                items = row.query_selector_all("div.foodmenu__menu-item")
                for item in items:
                    item_text = item.inner_text()
                    extracted_item = extract_menu_item(title_text, item_text)
                    print(f"  MENU ITEM: {extracted_item.name}")
                    extracted_items.append(extracted_item.to_dict())

        df = pd.DataFrame(extracted_items)
        df.to_csv("tullys_menu.csv", index=False)

        context.close()
        browser.close()

# Call the function
tullyscraper()


with sync_playwright() as playwright:
    tullyscraper(playwright)


