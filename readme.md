https://habr.com/ru/company/yandex/blog/242795/

generate allure report
py.test --alluredir report\allure

get report: 
allure serve report\allure


Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.