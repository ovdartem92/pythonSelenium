# Python + Selenium. Test Automation Framework
1. Selenium 4
2. PyTest
3. Allure
4. Web Driver Factory
5. Gmail Client
6. Wed Driver Listener
7. Page object, Factory patterns
8. User model
9. Wrappers to Web Element
10. Config.json with customize parameters (Headless mode, Browser Type, Timeout)

## Run test
Firstly you should install all dependency from requirements.txt
```
pip install -r requirements.txt
```

After type to command line
```
py.test
```
## Generate allure report
```
py.test --alluredir report\allure
```

## Get report: 
```
allure serve report\allure
```