from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
class sample:
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def a1(self):
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(By.XPATH,"//input[@id='email']").send_keys("reddy.csri@gmail.com")
        self.driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("Csrireddy77!")
        self.driver.implicitly_wait(7)
        try:
            self.driver.find_element(By.XPATH,"//button[@id='u_0_h_aG']").click()
        except Exception as e:
            print("no  major issue")

    def a2(self):
        self.driver.get("https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#clone-repo")
a=sample()
a.a1()
a.a2()