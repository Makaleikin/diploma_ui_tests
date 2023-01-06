import allure
from allure_commons.types import Severity

from tesla_tests.model.pages import tesla
from test_data.tesla_data import model_s, model_3, model_x


@allure.tag("web")
@allure.label('owner', 'MlynskijArtem')
@allure.feature('Проверка характеристик Tesla Model S')
@allure.link('https://www.tesla.com/models', name='Testing')
@allure.severity(Severity.CRITICAL)
def test_check_specification_model_s():
    # GIVEN
    tesla.given_opened()
    # WHEN
    tesla.click_on_tesla_model_s()
    # THEN
    tesla.model_s_has_opened(model_s.model)
    tesla.check_tesla_model_s_specification(model_s.range, model_s.boost, model_s.speed, model_s.power)


@allure.tag("web")
@allure.label('owner', 'MlynskijArtem')
@allure.feature('Проверка цены Tesla Model S/Tesla Model S')
@allure.link('https://www.tesla.com/models/design#overview', name='Testing')
@allure.severity(Severity.CRITICAL)
def test_order_now_model_s():
    # GIVEN
    tesla.given_opened()
    # WHEN
    tesla.click_on_tesla_model_s()
    tesla.click_order_now()
    # THEN
    tesla.check_price_model_s_and_model_s_plaid()


@allure.tag("web")
@allure.label('owner', 'MlynskijArtem')
@allure.feature('Проверка характеристик Tesla Model 3')
@allure.link('https://www.tesla.com/model3', name='Testing')
@allure.severity(Severity.CRITICAL)
def test_check_specification_model_3():
    # GIVEN
    tesla.given_opened()
    # WHEN
    tesla.click_on_tesla_model_3()
    # THEN
    tesla.model_3_has_opened(model_3.model)
    tesla.check_tesla_model_y_specification(model_3.boost, model_3.range, model_3.drive)


@allure.tag("web")
@allure.label('owner', 'MlynskijArtem')
@allure.feature('Проверка характеристик Tesla Model X')
@allure.link('https://www.tesla.com/modelx', name='Testing')
@allure.severity(Severity.CRITICAL)
def test_check_specification_model_x():
    # GIVEN
    tesla.given_opened()
    # WHEN
    tesla.click_on_tesla_model_x()
    # THEN
    tesla.model_x_has_opened(model_x.model)
    tesla.check_tesla_model_x_specification(model_x.range, model_x.boost, model_x.boost_quarter, model_x.power)
