**Run without ALlure** 

`behave features/login.feature`

**Generate Allure reports**

`behave -f allure_behave.formatter:AllureFormatter -o reports/ features/login.feature`


**Run Allure server**

`allure serve reports/`

