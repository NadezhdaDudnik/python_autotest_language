from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_should_see_login_link(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    #link = " http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    # page = MainPage(browser, link)
    # page.open()
    # page.should_be_login_link()

    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()

