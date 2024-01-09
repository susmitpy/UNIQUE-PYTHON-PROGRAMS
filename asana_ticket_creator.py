from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

with open("./tickets.txt", "r") as f:
    tickets = f.read().splitlines()

brow = webdriver.Chrome(ChromeDriverManager().install())

EMAIL = ""
PASSWORD = ""


def login():
    brow.get("https://app.asana.com/-/login?u=%2F0%2F1200472438130897%2Fboard")
    login_with_google = brow.find_element_by_xpath(
        '//*[@id="Login-appRoot"]/div/div[1]/div[2]/div[3]'
    )
    login_with_google.click()
    brow.switch_to.active_element.send_keys(EMAIL)
    sleep(2)
    brow.switch_to.active_element.send_keys(PASSWORD)


def main(ticket):
    add_task_btn = brow.find_element_by_xpath(
        '//*[@id="asana_main_page"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]'
    )
    add_task_btn.click()

    new_task_input = brow.switch_to.active_element
    new_task_input.send_keys(ticket)


login()
input("Press Enter after opening board")

for ticket in tickets:
    main(ticket)
    sleep(1)

brow.close()
