from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
comments=['follow the page in my bio to see toxic niggalations daily 😈']

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        self.driver = webdriver.Firefox(
            executable_path=r"C:\Users\moica\OneDrive\Escritorio\Trabajos Fiverr\Python\Comment Bot\geckodriver.exe"
        )  # Coloque o caminho para o seu geckodriver aqui

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']"
            )
            login_button.click()
        except:
            print('já estamos na página de login')
            pass
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        time.sleep(random.randint(4, 6))
        user_element.send_keys(self.username)
        time.sleep(random.randint(4, 6))
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(random.randint(4, 6))
        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(4, 6))
        self.curtir_fotos_com_a_hastag(
            "elmoise_"
        ) 

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        print("login page")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def curtir_fotos_com_a_hastag(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/" + hashtag + "/")

        time.sleep(5)
        #element href
        hrefs = driver.find_elements_by_xpath('//div[@class="_aabd _aa8k _aanf"]/a')
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(pic_hrefs[0])
       
        driver.get(pic_hrefs[0])
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        try:

            time.sleep(5)
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[2]/button").click()
            time.sleep(5)
            write= driver.find_element_by_xpath('//form[@class="_aao9"]/textarea')
            write.send_keys(random.choice(comments))
            send= driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button').click()

            time.sleep(random.randint(19, 23))

        except Exception as e:
            print(e)


bot = InstagramBot(
    "username", "password"
)
bot.login()