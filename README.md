## Project UI autotests for Tesla
<!-- Technology -->

### Используемые инструменты и фреймворки:
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

### Что проверяют автотесты:
* Проверка основных характеристик автомобиля "Tesla Model S"
* Покупка нового автомобиля "Tesla Model S"
* Проверка спецификаций "Tesla Model 3"
* Проверка спецификаций "Tesla Model S"


<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/ui_diploma_tests/)

##### Когда нажимаем "Собрать сейчас" начинается сборка билда, запустятся тесты. Тесты проходят на виртуальной машине в Selenide.
![This is an image](images/screenshots/jenkins_start.png)

##### Пример прохождения теста в Selenide:
![This is an image](images/screenshots/example_test.gif)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/logo/allure_report.png"> Allure report

##### После прохождения всех тестов, генерируется Allure отчет, в котором есть вся информация о тестах, которые были запущены
![This is an image](images/screenshots/allure_dashboard.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshots/allure_graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы, к которым прикрепляются аттачменты: видео прохождение теста, скриншот, page_source и браузер логи
![This is an image](images/screenshots/allure_attachments.png)

<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/logo/tg.png"> Проект так же интегрирован с telegram
##### Как только все тесты проходят, бот присылает сообщение с информацией о test run'е, в сообщении содержится ссылка на Allure отчет

![This is an image](images/screenshots/telegran_notification.png)

<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/logo_stacks/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/1720/dashboards)

##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![This is an image](images/screenshots/allure_testops_dashboard.png)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![This is an image](images/screenshots/allure_testops_suites.png)


<!-- Jira -->

### <img width="3%" title="Jira" src="images/logo_stacks/jira.png"> Интеграция с Jira
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно пробросить результат прохождение тестов и список тест-кейсов из Allure

![This is an image](images/screenshots/jira.png)
