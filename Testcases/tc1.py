from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class sample:
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def a1(self):
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(By.XPATH,"//input[@id='email']")
        self.driver.find_element(By.XPATH,"//input[@id='pass']")
        self.driver.find_element(By.CSS_SELECTOR,"#u_0_h_aG")

    def a2(self):
        self.driver.get("https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#clone-repo")