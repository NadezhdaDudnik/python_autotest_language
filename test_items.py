import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    text_add_to_basket = button.text

    assert "Añadir al carrito" == text_add_to_basket, "Other language is selected"
