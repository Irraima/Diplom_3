from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_element_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def wait_element_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator),
                                                         message=f"Can't find element by locator {locator}")

    def wait_element_not_visible(self, locator, timeout=60):
        return WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")

    def set_text(self, locator, text):
        element = self.wait_element_visible(locator)
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_element_visible(locator)
        return element.text

    def click_element_if_visible(self, locator):
        element = self.wait_element_visible(locator)
        element.click()

    def click_element_if_clickable(self, locator):
        click_element = self.wait_element_visible(locator)
        self.driver.execute_script('arguments[0].click();', click_element)

    def open_url(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def exist_element_check(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def drag_and_drop_element(self, locator_one, locator_two):
        draggable = self.driver.find_element(*locator_one)
        droppable = self.driver.find_element(*locator_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()

    def invisibility_check(self, locator) -> object:
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))

    def presence_check(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(locator))
