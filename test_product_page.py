from .pages.base_page import BasePage


def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = BasePage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()