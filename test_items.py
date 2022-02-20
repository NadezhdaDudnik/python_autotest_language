import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    button_basket = browser.find_element_by_css_selector(".btn-add-to-basket")
    #text_add_to_basket = button_basket.text

    assert button_basket, "The text of element is absent on this page"

    #assert "Añadir al carrito" == text_add_to_basket, "wrong text"

#pytest --language=es test_items.py

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time
#
# # запуск теста: pytest --language=es test_items.py
# def test_presence_of_add_to_cart_button(browser):
#     browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
#     time.sleep(10)
#     button = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")))
#     assert button is not None