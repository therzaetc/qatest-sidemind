from seleniumbase import BaseCase
from time import sleep


class QATest(BaseCase):
    def setUp(self, **kwargs):
        super().setUp()
        self.open(url="https://practice.automationtesting.in/shop/")

    def test_product_page(self):
        # opening "Android Quick Start Guide" page
        self.click_xpath(xpath='//*[@id="content"]/ul/li[1]/a[1]/h3')
        self.assert_equal(self.get_current_url(), 'https://practice.automationtesting.in/product/android-quick-start-guide/')

    def test_add_product(self):
        # opening "Android Quick Start Guide" page
        self.click_xpath(xpath='//*[@id="content"]/ul/li[1]/a[1]/h3')
        # adding to the basket
        self.click_xpath(xpath='//*[@id="product-169"]/div[2]/form/button')
        # looking for the message 'has been added to your basket'
        self.assert_element_present(selector='#content > div.woocommerce-message', timeout=10)

    def test_add_zero_quantity(self):
        # opening "Android Quick Start Guide" page
        self.click_xpath(xpath='//*[@id="content"]/ul/li[1]/a[1]/h3')
        self.click_xpath('//*[@id="product-169"]/div[2]/form/div/input')
        # setting the quantity to zero
        self.set_value(selector='#product-169 > div.summary.entry-summary > form > div > input', text=0)
        value = self.get_text(selector='#wpmenucartli > a > span.amount')
        # making sure the basket remains empty and the zero quantity cannot be added
        self.assert_equal('₹0.00', value)

    def test_add_product_from_home_page(self):
        # clicking on add to basket from home page
        self.click_xpath(xpath='//*[@id="content"]/ul/li[1]/a[2]')
        # give some time so the basket can update
        sleep(2)
        value = self.get_text(selector='#wpmenucartli > a > span.amount')
        # making sure the product was added to the basket
        self.assert_equal('₹450.00', value)

    def test_review_basket(self):
        # opening "Android Quick Start Guide" page
        self.click_xpath(xpath='//*[@id="content"]/ul/li[1]/a[1]/h3')
        # adding to the basket
        self.click_xpath(xpath='//*[@id="product-169"]/div[2]/form/button')
        sleep(2)
        # clicking on the basket
        self.click_xpath(xpath='//*[@id="wpmenucartli"]/a')
        # getting the product value on the basket
        product_value = self.get_text(selector='#page-34 > div > div.woocommerce > div > div > table > tbody > tr.cart-subtotal > td > span')
        self.assert_equal('₹450.00', product_value)

    def test_fill_checkout(self):
        # adding product from the home page
        self.click_xpath(xpath='//*[@id="content"]/ul/li[1]/a[2]')
        sleep(2)
        # clicking on basket icon
        self.click_xpath(xpath='//*[@id="wpmenucartli"]')
        # clicking on 'proceed to checkout'
        self.click_xpath(xpath='//*[@id="page-34"]/div/div[1]/div/div/div/a')
        # filling first name
        self.set_value(selector='#billing_first_name', text='Test QA')
        # filling last name
        self.set_value(selector='#billing_last_name', text='Sidemind')
        # filling email
        self.set_value(selector='#billing_email', text='testqa@gmail.com')
        # filling phone
        self.set_value(selector='#billing_phone', text='9999999999')
        # filling address
        self.set_value(selector='#billing_address_1', text='St Park')
        # filling town/city
        self.set_value(selector='#billing_city', text='Padova')
        # filling postcode/zip
        self.set_value(selector='#billing_postcode', text='50000000')
        # selecting 'Direct bank transfer'
        self.click_xpath(xpath='//*[@id="payment_method_bacs"]')
        # clicking on 'place order'
        self.click_xpath(xpath='//*[@id="place_order"]')
        # making sure it was successful
        self.assert_element_present(selector='#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received', timeout=10)

    def test_paypal_method(self):
        # adding product from the home page
        self.click_xpath(xpath='//*[@id="content"]/ul/li[1]/a[2]')
        sleep(2)
        try:
            # clicking on basket icon
            self.click_xpath(xpath='//*[@id="wpmenucartli"]')
            # clicking on 'proceed to checkout'
            self.click_xpath(xpath='//*[@id="page-34"]/div/div[1]/div/div/div/a')
            # filling first name
            self.set_value(selector='#billing_first_name', text='Test QA')
            # filling last name
            self.set_value(selector='#billing_last_name', text='Sidemind')
            # filling email
            self.set_value(selector='#billing_email', text='testqa@gmail.com')
            # filling phone
            self.set_value(selector='#billing_phone', text='9999999999')
            # filling address
            self.set_value(selector='#billing_address_1', text='St Park')
            # filling town/city
            self.set_value(selector='#billing_city', text='Padova')
            # filling postcode/zip
            self.set_value(selector='#billing_postcode', text='50000000')
            # clicking on 'PayPal Express Checkout'
            self.click_xpath(xpath='//*[@id="payment_method_ppec_paypal"]')
            # clicking on 'place order'
            self.click_xpath(xpath='//*[@id="place_order"]')
            # making sure it was successful
            self.assert_element_present(selector='#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received', timeout=10)
        except Exception as e:
            raise e
