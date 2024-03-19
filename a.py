from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.instagram.com/")
    page.get_by_label("Phone number, username, or").click()
    page.get_by_label("Phone number, username, or").fill("devapptestingig")
    page.get_by_label("Phone number, username, or").press("Tab")
    page.get_by_label("Password").fill("Dfxtr8$w")
    page.get_by_label("Password").press("Enter")
    page.get_by_role("button", name="Not now").click()
    page.get_by_role("button", name="Not Now").click()
    page.get_by_role("link", name="Search Search").click()
    page.get_by_role("link", name="marciaconradolorena's profile picture marciaconradolorena Verified Márcia").click()
    page.get_by_role("link", name="Esquadrilha da Fumaça em").click()
    # page.get_by_role("button", name="Next").click()
    # page.get_by_role("button", name="Load more comments").click()
    html = page.content()
    html = BeautifulSoup(html, 'html.parser')
 
    with open("test_example.html", "w") as f:
        f.write(html.prettify())
        

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
