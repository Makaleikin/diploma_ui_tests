# Project UI autotests for Tesla
<!-- Technology -->

## Используемые инструменты и фреймворки:
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="images/logo/docker.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>

<!-- Тест кейсы -->

## Что проверяют автотесты:
* Проверка основных характеристик автомобиля "Tesla Model S"
* Покупка нового автомобиля "Tesla Model S"
* Проверка спецификаций "Tesla Model 3"
* Проверка спецификаций "Tesla Model S"

<!-- Jenkins -->

## <img width="3%" title="Jenkins" src="images/logo/jenkins.png"> Запуск проекта в Jenkins

## [Job](https://jenkins.autotests.cloud/job/ui_diploma_tests/)

#### Когда нажимаем "Собрать сейчас" начнется сборка билда, запустятся тесты. Тесты проходят на виртуальной машине в Selenide.

![This is an image](images/screenshots/jenkins_start.png)

#### Пример прохождения теста в Selenide:

![This is an image](images/screenshots/example_test.gif)

<!-- Allure report -->

## <img width="3%" title="Allure Report" src="images/logo/allure_report.png"> Allure report

#### После прохождения всех тестов, генерируется Allure отчет, в котором есть вся информация о тестах, которые были запущены
![This is an image](images/screenshots/allure_dashboard.png)

#### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshots/allure_graphs.png)

#### Во вкладке Suites находятся собранные тест кейсы, к которым прикрепляются аттачменты: видео прохождение теста, скриншот, page_source и логи браузера
![This is an image](images/screenshots/allure_attachments.png)

<!-- Telegram -->

## <img width="3%" title="Telegram" src="images/logo/tg.png"> Проект так же интегрирован с telegram
#### По окончании прохождения тестов, бот присылает сообщение с информацией о test run'е, в сообщении содержится ссылка на Allure отчет

![This is an image](images/screenshots/telegram_notification.png)

<!-- Allure TestOps -->

## <img width="3%" title="Allure TestOps" src="images/logo/allure_testops.png"> Интеграция с Allure TestOps

#### Вся отчетность сохраняется в Allure TestOps, где есть вся аналогичная информация с Allure отчета

![This is an image](images/screenshots/allure_testops_dashboard.png)

#### После того, как мы запускаем сборку в Jenkins, Allure TestOps автоматически создает test suites, test cases на основе нашего кода:

![This is an image](images/screenshots/allure_testops_test_cases.png)

#### На вкладке с тестами, мы можем:
- Управлять всеми тест-кейсами (стандартный функционал для TMS)
- Запускать тесты по отдельности, если они автоматические, то они запустятся на сервере в Jenkins
- Интегрировать с Jira

#### Если мы запустили test run, то на вкладке "launches", мы можем:
- Наблюдать, как будут проходить тесты в live режиме
- Перезапускать тесты, если они со статусом broken и failed
- Перезапускать тесты мануально, если, к примеру, у нас проблема с web.driver
- Создавать дефекты

<!-- Jira -->

## <img width="3%" title="Jira" src="images/logo/jira.png"> Интеграция с Jira
#### Настроив через Allure TestOps интеграцию с Jira, мы можем отправлять тест-кейс и тест раны в Jira

![This is an image](images/screenshots/jira_issue.png)
