from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SUGGEST = (By.CSS_SELECTOR, ".mini-suggest__popup")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_SEARCH_LINKS = (By.CSS_SELECTOR, "#search-result > .serp-item a.link > b")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, "li.services-new__list-item")
    LOCATOR_YANDEX_IMAGES_LINK = (By.CSS_SELECTOR, "li.services-new__list-item:nth-child(3) > a:nth-child(1)")
    LOCATOR_YANDEX_FIRST_CATEGORY = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div/div/div[1]/a")
    LOCATOR_YANDEX_FIRST_IMAGE = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a")
    LOCATOR_YANDEX_GO_FORWARD = (By.XPATH, "/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[4]/i")
    LOCATOR_YANDEX_GO_BACK = (By.XPATH, "/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[1]/i")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def check_suggest(self):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=10)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def check_five_links(self):
        links = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_LINKS, time=10)
        five_links = [elem.text.strip() for elem in links[:5]]
        return five_links

    def go_to_images(self):
        images_link = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_LINK, time=2)
        images_link.click()
        time.sleep(10)
        return images_link

    def click_on_first_category(self):
        image = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_CATEGORY, time=2)
        image.click()
        time.sleep(5)
        return image

    def get_name_first_category(self):
        image = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_CATEGORY, time=2)
        name_image = image.text
        return name_image

    def click_on_first_image(self):
        image = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_IMAGE, time=2)
        image.click()
        time.sleep(5)
        return image

    def go_forward(self):
        image = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_GO_FORWARD, time=2)
        image.click()
        time.sleep(5)
        return image

    def go_back(self):
        image = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_GO_BACK, time=2)
        image.click()
        time.sleep(5)
        return image






