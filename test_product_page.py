from .Pages.product_page import ProductPage
import  pytest

@pytest.mark.parametrize('number', [str(x) for x in range(10)])
def test_guest_can_add_product_to_basket(browser,number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)
    page.open()

    product_name = page.save_name_product()
    product_price = page.save_price_product()

    page.add_to_cart()
    page.solve_quiz_and_get_code()

    page.testing_price_product(product_price)
    page.testing_name_product(product_name)