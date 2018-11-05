from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains
from PIL import Image

USERNAME = '18502827757'
PASSWORD = 'wyf073008'

class CrackGeeTest:
    def __init__(self):
        self.url = 'https://member.zjtcn.com/common/login.html'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser,20)
        self.username = USERNAME
        self.password = PASSWORD

    # def __del__(self):
        # self.browser.close()

    def getButton(self):
        login = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.bluebtn a')))
        print(login.text)
        return login

    def getSlider(self):
        slider = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.ui-slider-btn.init.ui-slider-no-select')))
        return slider

    def getDistance(self):
        slider_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.ui-slider-text.ui-slider-no-select')))
        print(slider_text.size['width'])
        return slider_text.size['width']

    def open(self):
        self.browser.get(self.url)
        username_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.user')))
        password_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.password')))
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

    def open_another(self):
        self.browser.get('https://hubei.zjtcn.com/facx/c000_t0101_d201811_p1_k_qa_qi.html')

    def getTracks(self,distance):
        track = []
        current = 0
        mid = distance * 4 /5
        t = 0.2 
        v = 0
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            v = v0 + a*t
            move = v0*t + 1/2*a*t*t
            current += move
            track.append(round(move))
        return track

    def moveToLeft(self,slider,tracks):
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x,yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()

    def crack(self):
        self.open()
        distance = self.getDistance()
        tracks = self.getTracks(distance)
        slider = self.getSlider()
        self.moveToLeft(slider,tracks)

        button = self.getButton()
        # print(button)
        button.click()


if __name__ == "__main__":
    crack = CrackGeeTest()
    crack.crack()
    crack.open_another()
    