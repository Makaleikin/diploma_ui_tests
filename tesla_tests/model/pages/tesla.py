import allure
from selene import have, be
from selene.support.shared import browser


@allure.step('Открываем сайт Tesla')
def given_opened():
    browser.open('https://www.tesla.com/')


@allure.step('В хедере, кликаем на "Model S"')
def click_on_tesla_model_s():
    browser.element('[title="Model S"]').click()


@allure.step('Проверяем, что открылась модель "Model S Plaid"')
def model_s_has_opened(model):
    browser.element('[class="tcl-hero__heading tds-colorscheme--light tds-animate_small--to_reveal"]').should(have.text(model.value))


@allure.step('Проверяем основные характеристики')
def check_tesla_model_s_specification(range, boost, speed, power):
    browser.all('[class="tcl-badge tcl-animate tcl-animate--to-reveal tcl-animate--revealed"]').should(have.exact_texts(range.value, boost.value, speed.value, power.value))


@allure.step('Жмем кнопку "Order Now"')
def click_order_now():
    button_buy_now = '[class="tcl-badges__button tcl-animate tcl-animate--to-reveal tcl-animate--revealed"]'
    browser.element(button_buy_now).should(be.visible)
    browser.element(button_buy_now).click()


def check_price_model_s_and_model_s_plaid():
    price = '[class="group--options_block-container_price group--options_block-option_price text-loader--content price-not-included"]'
    browser.all(price).should(have.texts('$96,590', '$127,590'))

# @allure.step('Проверяем, что открылся "Inventory"')
# def inventory_has_open():
#     inventory = '[class="inventory-header-wrapper sticky-content tds-scrim--white"]'
#     browser.element(inventory).should(be.visible)


# @allure.step('Жмем чекбокс "Used"')
# def click_checkbox_used():
#     used_checkbox = '[title="Used"]'
#     browser.element(used_checkbox).click()


# @allure.step('Проверяем, что в продаже есть автомобили с пробегом')
# def inventory_display_used_cars():
#     used_cars = '[class="result card"]'
#     browser.all(used_cars).should(have.size_greater_than_or_equal(1))


@allure.step('В хедере, кликаем на "Model 3"')
def click_on_tesla_model_3():
    browser.element('[title="Model 3"]').click()


@allure.step('Проверяем, что открылась модель "Model 3"')
def model_3_has_opened(model):
    browser.element('[class="tcl-hero__heading tds-colorscheme--dark tds-animate_small--to_reveal"]').should(have.text(model.value))


@allure.step('Проверяем основные характеристики автомобиля')
def check_tesla_model_y_specification(boost, range, drive):
    specification_model_y = '[class="tcl-badge tcl-animate tcl-animate--to-reveal tcl-animate--revealed"]'
    browser.all(specification_model_y).should(have.exact_texts(boost.value, range.value, drive.value))


@allure.step('В хедере, кликаем на "Model X"')
def click_on_tesla_model_x():
    browser.element('[title="Model X"]').click()


@allure.step('Проверяем, что открылась модель "Model X"')
def model_x_has_opened(model):
    browser.element('[class="tcl-hero__heading tds-colorscheme--light tds-animate_small--to_reveal"]').should(have.text(model.value))


@allure.step('Проверяем основные характеристики автомобиля')
def check_tesla_model_x_specification(range, boost, quarter, power):
    specification_model_x = '[class="tcl-badge tcl-animate tcl-animate--to-reveal tcl-animate--revealed"]'
    browser.all(specification_model_x).should(have.exact_texts(range.value, boost.value, quarter.value, power.value))
