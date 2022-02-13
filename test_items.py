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