from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver= webdriver.Firefox(
            executable_path=r"C:\Users\moica\OneDrive\Escritorio\Trabajos Fiverr\Python\Comment Bot\geckodriver.exe"
        ) 
driver.get("https://www.instagram.com/snoopdogg/")   
click_on_post = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a"))).click()     