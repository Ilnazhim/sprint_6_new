# Sprint_6
# установить зависимости
pip install -r requirements.txt
# запустить тесты
pytest --alluredir=allure_results
# открыть отчет Allure
allure serve allure_results