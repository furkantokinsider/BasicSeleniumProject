import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TestCheckLcWaikikiAddToCart(unittest.TestCase):
    ACCEPT_COOKIES_BTN = (By.XPATH, "//button[text()='Tüm Çerezlere İzin Ver']")
    SUPPORT_BTN = (By.ID, "_sorun_icon")
    MAN_CAT_BTN = (By.LINK_TEXT, 'ERKEK')
    SWEATSHIRT_CAT_BTN = (By.LINK_TEXT, "Sweatshirt")
    HEADER = (By.XPATH, "//h1")
    PRODUCTS_IN_CAT = (By.CLASS_NAME, "product-card__title")
    SIZE_BTN = (By.XPATH, "//a[@size='L']")
    ADD_TO_CART_BTN = (By.ID, "pd_add_to_cart")
    ITEM_ADDED_POPUP = (By.XPATH, "//div[text()='Sepetinize 1 adet ürün eklenmiştir.']")
    CART_BTN = (By.XPATH, "//a[@class='header-dropdown-toggle']")
    PAYMENT_BTN = (By.LINK_TEXT, "ÖDEME ADIMINA GEÇ")
    HOME_LOGO = (By.CLASS_NAME, "main-header-logo")
    TOP_HEADER = (By.CLASS_NAME, "header__top ")

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.lcwaikiki.com/tr-TR/TR")
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def test_check_lcw_add_to_cart(self):
        self.assertTrue(*self.SUPPORT_BTN)
        action = ActionChains(self.driver)
        self.wait.until(EC.element_to_be_clickable(self.ACCEPT_COOKIES_BTN))
        self.driver.find_element(*self.ACCEPT_COOKIES_BTN).click()
        action.move_to_element(self.driver.find_element(*self.MAN_CAT_BTN)).perform()
        self.driver.find_element(*self.SWEATSHIRT_CAT_BTN).click()
        self.assertTrue(*self.HEADER)
        self.driver.find_elements(*self.PRODUCTS_IN_CAT)[1].click()
        self.assertTrue(*self.ADD_TO_CART_BTN)
        self.wait.until(EC.element_to_be_clickable(self.SIZE_BTN))
        self.driver.find_element(*self.SIZE_BTN).click()
        self.driver.find_element(By.ID, "pd_add_to_cart").click()
        self.wait.until(EC.element_to_be_clickable(self.ITEM_ADDED_POPUP))
        self.assertTrue(*self.ITEM_ADDED_POPUP)
        self.driver.find_elements(*self.CART_BTN)[2].click()
        self.assertTrue(*self.PAYMENT_BTN)
        self.driver.find_element(*self.HOME_LOGO).click()
        self.assertTrue(*self.SUPPORT_BTN)

    def tearDown(self):
        self.driver.quit()
