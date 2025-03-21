from playwright.sync_api import sync_playwright
import os

jmeno = "Jarmil"
heslo = "Admin123"


def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://js-trebesin.github.io/playwright-exam/")
        page.fill('input[id="login"]', jmeno)
        page.fill('input[id="pass"]', heslo)
        page.click('button[class="login-btn"]')

        secret = page.locator('body > div > div > p').text_content()

        print(secret)


        # !!!
        # na page.locator(selector) se dá použít funkce .text_content(), která vypíše text daného prvku
        # !!!

        input("Klikni klávesu pro zavření")
        browser.close()
    

if __name__ == "__main__":
    main()
