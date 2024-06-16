from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from dotenv import load_dotenv

import os
import time


class AutomaticLinkedInConnectionsAcceptor:
    def __init__(self):
        print("Initiated...")
        load_dotenv()

        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 100)

    def get_element(self, xpath):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def login(self):
        print("Loggin in...")
        email_field = self.get_element('//*[@id="username"]')
        email_field.send_keys(os.environ["EMAIL"])

        password_field = self.get_element('//*[@id="password"]')
        password_field.send_keys(os.environ["PASSWORD"])

        sign_in_btn = self.get_element(
            "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
        sign_in_btn.click()

    def run(self):

        self.driver.get("https://linkedin.com/login")

        self.login()

        try:
            logo = self.get_element(
                "/html/body/div[5]/header/div/nav/ul/li[2]/a")
        except TimeoutException:
            self.driver.close()
            raise TimeoutException

        print("Successfully logged in!")

        self.driver.get(
            "https://www.linkedin.com/mynetwork/invitation-manager/")

        all_invts_span = self.get_element(
            "/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/section/div[2]/nav/button[1]/span")
        num_invts = int(all_invts_span.text[-2])

        for i in range(1, num_invts+1):
            el = self.get_element(
                f"/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/section/div[2]/section/ul/li[{i}]/div[1]/div[2]/button[2]")
            el.click()

        if num_invts:
            print(f"Successfully accepted {num_invts} invites.")
        else:
            print("No invites")

        self.driver.close()


def main():

    while True:
        try:
            app = AutomaticLinkedInConnectionsAcceptor()
            app.run()
        except TimeoutException:
            continue

        time.sleep(60 * 60 * 24)


if __name__ == "__main__":
    main()
