**Run without ALlure** 

`behave features/login.feature`

**Generate Allure reports**

`behave -f allure_behave.formatter:AllureFormatter -o reports/ features/login.feature`


**Run Allure server**

`allure serve reports/`

**Jenkins**

***Sample commands***:

*Install the latest LTS version:* 
`brew install jenkins-lts`

*Install a specific LTS version:* 
`brew install jenkins-lts@YOUR_VERSION`

*Start the Jenkins service:* 
`brew services start jenkins-lts`

*Stop the Jenkins service:* 
`brew services stop jenkins-lts`

*Restart the Jenkins service:* 
`brew services restart jenkins-lts`

*Update the Jenkins version:* 
`brew upgrade jenkins-lts`
