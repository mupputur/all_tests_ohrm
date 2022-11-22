#test scenario:
"""
Adding employee details with optional field
"""
#test steps:
"""
1.  Launch the application & login with default credentials 
2.  Navigate to the PIM 
3.  Click on configurations and go to optional fields
4.  Disable optional fields and save 
5.  Click add button  to add employee details 
6.  Enter the first  name & last name & employee ID 
7.  Enable the Craete Login Details button 
8.  User the firstname as the username and create a password 
9.  Click the status as enabled and clcik save button 
10. Check the employee details in employee list 
11. Check the persnoal details in employee list wheather the SSN and SIN are present or not
12. Logout the application and re-login with the  new emplyee login details 
"""
# test code:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
# Initiize the driver

driver_obj = webdriver.Chrome(executable_path="C:\\Users\\ankes\\PycharmProjects\\all_tests_ohrm\\chromedriver.exe")

# launch the application
driver_obj.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
# indentify the user filed & enter the email

username_filed = driver_obj.find_element(By.NAME, "username")
time.sleep(2)
username_filed.send_keys("Admin")
password_filed = driver_obj.find_element(By.NAME, "password")
time.sleep(2)
password_filed.send_keys("admin123")
time.sleep(6)
logging = driver_obj.find_element(By.XPATH,"//button[@type='submit']")
logging.click()
time.sleep(10)
#step2 navigating to PIM
pim_page=driver_obj.find_element (By.XPATH,"//a[@href= '/web/index.php/pim/viewPimModule']")
pim_page.click()
time.sleep(3)
#Click on configuaration
pim_page=driver_obj.find_element(By.XPATH,'//span[@class="oxd-topbar-body-nav-tab-item"]')
pim_page.click()
time.sleep(2)
#Choose optional field
pim_page=driver_obj.find_element(By.XPATH, "//a [@class='oxd-topbar-body-nav-tab-link']")
pim_page.click()
time.sleep(2)
pim_page=driver_obj.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]')
pim_page.click()
time.sleep(2)
pim_page=driver_obj.find_element(By.XPATH,'(//span[@class="oxd-switch-input oxd-switch-input--active --label-right"])[1]')
pim_page.click()
time.sleep(2)
pim_page=driver_obj.find_element(By.XPATH,'(//span[@class="oxd-switch-input oxd-switch-input--active --label-right"])[2]')
pim_page.click()
time.sleep(2)
pim_page=driver_obj.find_element(By.XPATH,'(//span[@class="oxd-switch-input oxd-switch-input--active --label-right"])[3]')
pim_page.click()
time.sleep(2)
#Save button
pim_page=driver_obj.find_element(By.XPATH, "//button [@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
pim_page.click()
time.sleep(3)
# Open employeelist
pim_page=driver_obj.find_element(By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item']")
pim_page.click()
time.sleep(2)
#Click on add button
pim_add = driver_obj.find_element(By.XPATH,'//button[text()=" Add "]')
pim_add.click()
time.sleep(2)
#Enter firstname and lastname
firstName_filed = driver_obj.find_element(By.NAME, "firstName")
firstName_filed.send_keys("Sree")
time.sleep(2)
lastName_filed = driver_obj.find_element(By.NAME, "lastName")
lastName_filed.send_keys("Devi")
time.sleep(2)
#take default employee_id
employeeid_filed=driver_obj.find_element(By.XPATH, '//*[@id="app"]//div[2]/div/div/div[2]/input')
time.sleep(2)
#Enable the Craete Login Details button
create=driver_obj.find_element(By.XPATH,'//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]')
create.click()
time.sleep(2)
#User thefirstname as the username and createapassword
username_filed = driver_obj.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input')
time.sleep(2)
username_filed.send_keys("Sree")
time.sleep(2)
password_filed = driver_obj.find_element(By.XPATH, '//input[@type="password"]')
time.sleep(2)
password_filed.send_keys("Devi123")
time.sleep(2)
confirmpassword_filed = driver_obj.find_element(By.XPATH,'(//input[@type="password"])[2]')
time.sleep(2)
confirmpassword_filed.send_keys("Devi123")
time.sleep(2)
#save button
pim_page=driver_obj.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
pim_page.click()
time.sleep(5)
#test scenario:
"""
Adding employee details with optional field
"""
#test steps:
"""
1.  Launch the application & login with default credentials 
2.  Navigate to the PIM 
3.  Click on configurations and go to optional fields
4.  Enable optional fields and save 
5.  Click add button  to add employee details 
6.  Enter the first  name & last name & employee ID 
7.  Enable the Craete Login Details button 
8.  User the firstname as the username and create a password 
9.  Click the status as enabled and clcik save button 
10. Check the employee details in employee list 
11. Check the persnoal details in employee list wheather the SSN and SIN are present or not
12. Logout the application and re-login with the  new emplyee login details 
"""
# test code:
#Teststep2:
#Click on configuaration
pim_page=driver_obj.find_element(By.XPATH,'//span[@class="oxd-topbar-body-nav-tab-item"]')
pim_page.click()
time.sleep(2)
#Choose optional field
pim_page=driver_obj.find_element(By.XPATH, "//a [@class='oxd-topbar-body-nav-tab-link']")
pim_page.click()
time.sleep(2)
#save button
pim_page=driver_obj.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
pim_page.click()
time.sleep(5)
# Open employeelist
pim_page=driver_obj.find_element(By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item']")
pim_page.click()
time.sleep(2)
#Click on add button
pim_add = driver_obj.find_element(By.XPATH,'//button[text()=" Add "]')
pim_add.click()
time.sleep(2)
#Enter firstname and lastname
firstName_filed = driver_obj.find_element(By.NAME, "firstName")
firstName_filed.send_keys("Sree")
time.sleep(2)
lastName_filed = driver_obj.find_element(By.NAME, "lastName")
lastName_filed.send_keys("Devi")
time.sleep(2)
#take default employee_id
employeeid_filed=driver_obj.find_element(By.XPATH, '//*[@id="app"]//div[2]/div/div/div[2]/input')
time.sleep(2)
#Enable the Craete Login Details button
create=driver_obj.find_element(By.XPATH,'//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]')
create.click()
time.sleep(2)
#User thefirstname as the username and createapassword
username_filed = driver_obj.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input')
time.sleep(2)
username_filed.send_keys("Sree")
time.sleep(2)
password_filed = driver_obj.find_element(By.XPATH, '//input[@type="password"]')
time.sleep(2)
password_filed.send_keys("Devi123")
time.sleep(2)
confirmpassword_filed = driver_obj.find_element(By.XPATH,'(//input[@type="password"])[2]')
time.sleep(2)
confirmpassword_filed.send_keys("Devi123")
time.sleep(2)
pim_page=driver_obj.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
pim_page.click()
time.sleep(2)
#Save button
pim_page=driver_obj.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
pim_page.click()
time.sleep(10)
#logout the application
pim_page=driver_obj.find_element(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
pim_page.click()
time.sleep(10)
pim_page=driver_obj.find_element(By.XPATH,'//a[@href="/web/index.php/auth/logout"]')
pim_page.click()
time.sleep(10)
#test scenario:
"""
Adding custom field with exsiting custom details
"""
#test steps:
"""
1.  Launch the application & login with default credentials 
2.  Navigate to the PIM 
3.  Click  on configuaration
4.  Go to custom fields and click on add button to add custom details (filed name :  Adhar, screen : personal details , type: text or Number)
5.  Add employee and check the personal details page weatehr added custom filed was showing or not "
"""
# test code:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time

# Initiize the driver

driver_obj = webdriver.Chrome(executable_path="C:\\Users\\ankes\\PycharmProjects\\all_tests_ohrm\\chromedriver.exe")

# launch the application
driver_obj.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)

# test code:
# enter username
username_filed = driver_obj.find_element(By.NAME, "username")
username_filed.send_keys("Admin")
# enter password
pass_filed = driver_obj.find_element(By.NAME, "password")
pass_filed.send_keys("admin123")
# login
login_button = driver_obj.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(5)
# step 2
# select pim
pim_filed = driver_obj.find_element(By.XPATH, "//a[@href= '/web/index.php/pim/viewPimModule']")
pim_filed.click()
time.sleep(5)
# select configure
configure=driver_obj.find_element(By.XPATH,'//span[@class="oxd-topbar-body-nav-tab-item"]')
configure.click()
time.sleep(5)
# select custom
custom_flied=driver_obj.find_element(By.XPATH,"//*[text()='Custom Fields']")
custom_flied.click()
time.sleep(5)
# add custom_filed
add_custom_filed=driver_obj.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
add_custom_filed.click()
time.sleep(5)
# enter filedname
filedname=driver_obj.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
filedname.send_keys("Adhar")
time.sleep(5)
# dropdown screen
screen=driver_obj.find_element(By.XPATH,'//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]')
screen.click()
time.sleep(10)
# select details
details=driver_obj.find_element(By.XPATH,'//*[text()="Personal Details"]')
details.click()
#time.sleep(10)
# dropdwon type
type=driver_obj.find_element(By.XPATH,'(//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"])[2]')
type.click()
time.sleep(10)
# select type_filed
type_detals=driver_obj.find_element(By.XPATH,'//*[text()="Text or Number"]')
type_detals.click()
#time.sleep(10)
custom_save=driver_obj.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')
custom_save.click()
time.sleep(10)
#test scenario:
"""
Adding new employee with default employee ID
"""
#test steps:
"""
1.  Launch the application & login with default credentials 
2.  Navigate to the PIM 
3.  Click add button  to add emplyee details 
4.  Enter the first  name & last name 
5.  Give the employee ID which alredy exits 
6.  Clcik the save button 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
# Initiize the driver
driver_obj = webdriver.Chrome(executable_path="C:\\Users\\ankes\\PycharmProjects\\all_tests_ohrm\\chromedriver.exe")
# launch the application
driver_obj.implicitly_wait(5)
driver_obj.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
from selenium.webdriver.support.wait import WebDriverWait
# indentify the user filed & enter the email
username_filed = driver_obj.find_element(By.NAME, "username")
time.sleep(2)
username_filed.send_keys("Admin")
time.sleep(2)
pass_filed = driver_obj.find_element(By.NAME, "password")
time.sleep(2)
pass_filed.send_keys("admin123")
time.sleep(2)
login_button = driver_obj.find_element(By.XPATH, "//button[@type='submit']")
time.sleep(2)
login_button.click()
time.sleep(2)
# step 2 navigate to the pim
pim_filed = driver_obj.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
time.sleep(2)
pim_filed.click()
time.sleep(2)
#step3 add button
pim_add = driver_obj.find_element(By.XPATH,'//button[text()=" Add "]')
pim_add.click()
time.sleep(2)
#step4 add employee details
add_employee=driver_obj.find_element(By.NAME,"firstName")
add_employee.send_keys("RADHA")
time.sleep(2)
add_employee1=driver_obj.find_element(By.NAME,"lastName")
add_employee1.send_keys("KRISHNA")
time.sleep(2)
action = ActionChains(driver_obj)
clear_box=driver_obj.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]")
action.move_to_element(clear_box).double_click().perform()
time.sleep(2)
action.send_keys(Keys.DELETE).perform()
time.sleep(2)
action.send_keys("9052").perform()
time.sleep(2)
# step6 save button
save_button=driver_obj.find_element(By.XPATH, "//button[@type='submit']")
save_button.click()
time.sleep(5)
#test scenario:
"""
Adding employee with login access 
"""
#test steps:
"""
1.  Launch the application & login with default credentials 
2.  Navigate to the PIM 
3.  Click add button  to add employee details
4.  Enter the first  name & last name & employee ID 
6.  Enable the Craete Login Details button 
7.   User the firstname as the username and create a password 
8.  click the status as enabled and clcik save button 
9.  Check the employee details in employee list 
10. Logout the application and re-login with the  new emplyee login details 
"""
# step 2
pim_filed = driver_obj.find_element(By.XPATH, "//a[@href= '/web/index.php/pim/viewPimModule']")
time.sleep(2)
pim_filed.click()
time.sleep(5)
pim_add = driver_obj.find_element(By.XPATH,'//button[text()=" Add "]')
pim_add.click()
time.sleep(5)
#FIRST NAME AND LAST NAME:------
firstName_filed = driver_obj.find_element(By.NAME, "firstName")
time.sleep(2)
firstName_filed.send_keys("Radha")
time.sleep(3)
lastName_filed = driver_obj.find_element(By.NAME, "lastName")
time.sleep(2)
lastName_filed.send_keys("Krishna")
time.sleep(3)
#Enable the Craete Login Details button
create=driver_obj.find_element(By.XPATH,'//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]')
create.click()
time.sleep(2)
#User thefirstname as the username and createapassword
username_filed = driver_obj.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input')
time.sleep(2)
username_filed.send_keys("Radha")
time.sleep(2)
password_filed = driver_obj.find_element(By.XPATH, '//input[@type="password"]')
time.sleep(2)
password_filed.send_keys("Krishna@9052")
time.sleep(2)
confirmpassword_filed = driver_obj.find_element(By.XPATH,'(//input[@type="password"])[2]')
time.sleep(2)
confirmpassword_filed.send_keys("Krishna@9052")
time.sleep(2)
pim_page=driver_obj.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
pim_page.click()
time.sleep(2)
#logout the application
pim_page=driver_obj.find_element(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
pim_page.click()
time.sleep(10)
pim_page=driver_obj.find_element(By.XPATH,'//a[@href="/web/index.php/auth/logout"]')
pim_page.click()
time.sleep(5)
#re-login with the  new emplyee login details
username_filed = driver_obj.find_element(By.NAME, "username")
time.sleep(2)
username_filed.send_keys("Radha")
time.sleep(2)
pass_filed = driver_obj.find_element(By.NAME, "password")
time.sleep(2)
pass_filed.send_keys("Krishna@9052")
time.sleep(2)
login_button = driver_obj.find_element(By.XPATH, "//button[@type='submit']")
time.sleep(2)
login_button.click()
time.sleep(3)
#test scenario:
"""
Adding new employee with default employee ID
"""
#test steps:
"""
1.  Launch the application & login with default credentials 
2.  Navigate to the PIM 
3.  Click add button  to add emplyee details 
4.  Enter the first  name & last name 
5.  Keep the default employee ID 
6.  Click the save button & check the emplyee was successfully created or not in the employee list 
"""
# test code:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
# Initiize the driver
driver_obj = webdriver.Chrome(executable_path="C:\\Users\\ankes\\PycharmProjects\\all_tests_ohrm\\chromedriver.exe")

# launch the application
driver_obj.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
# indentify the user filed & enter the email

username_filed = driver_obj.find_element(By.NAME, "username")
time.sleep(2)
username_filed.send_keys("Admin")
password_filed = driver_obj.find_element(By.NAME, "password")
time.sleep(2)
password_filed.send_keys("admin123")
time.sleep(5)
logging = driver_obj.find_element(By.XPATH,"//button[@type='submit']")
logging.click()
time.sleep(10)
#step2 navigating to PIM
pim_page=driver_obj.find_element (By.XPATH,"//a[@href= '/web/index.php/pim/viewPimModule']")
pim_page.click()
time.sleep(2)
#step3 add button
pim_add = driver_obj.find_element(By.XPATH,'//button[text()=" Add "]')
pim_add.click()
time.sleep(3)
#step4 add employee details
add_employee=driver_obj.find_element(By.NAME,"firstName")
add_employee.send_keys("Anjana")
time.sleep(3)
add_employee1=driver_obj.find_element(By.NAME,"lastName")
add_employee1.send_keys("mannam")
time.sleep(3)
# step5 defult employee id
defult=driver_obj.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
defult.click()
time.sleep(3)
#step6 save button
save_button=driver_obj.find_element(By.XPATH, "//button[@type='submit']")
save_button.click()
time.sleep(10)
#test scenario:
"""
Adding new employee with default employee ID 
"""
#test steps:
"""
1.  Launch the application & login with default credentials 
2.  Navigate to the PIM 
3.  Click add button  to add emplyee details 
4.  Enter the first  name & last name 
5.  Give the new employee ID 
6.  Click the save button & check the emplyee was successfully created or not in the employee list 
"""
# Initiize the driver

driver_obj = webdriver.Chrome(executable_path="C:\\Users\\ankes\\PycharmProjects\\all_tests_ohrm\\chromedriver.exe")

# launch the application
driver_obj.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
# indentify the user filed & enter the email

username_filed = driver_obj.find_element(By.NAME, "username")
time.sleep(2)
username_filed.send_keys("Admin")
password_filed = driver_obj.find_element(By.NAME, "password")
time.sleep(2)
password_filed.send_keys("admin123")
time.sleep(5)
logging = driver_obj.find_element(By.XPATH,"//button[@type='submit']")
logging.click()
time.sleep(10)
# step 2 navigate to the pim
pim_filed = driver_obj.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
time.sleep(2)
pim_filed.click()
time.sleep(3)
#step3 add button
pim_add = driver_obj.find_element(By.XPATH,'//button[text()=" Add "]')
pim_add.click()
time.sleep(3)
#step4 add employee details
add_employee=driver_obj.find_element(By.NAME,"firstName")
add_employee.send_keys("MANNAM")
time.sleep(3)
add_employee1=driver_obj.find_element(By.NAME,"lastName")
add_employee1.send_keys("Manasa")
time.sleep(3)
action = ActionChains(driver_obj)
clear_box=driver_obj.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]")
action.move_to_element(clear_box).double_click().perform()
time.sleep(3)
action.send_keys(Keys.DELETE).perform()
time.sleep(4)
action.send_keys("9012").perform()
time.sleep(5)
# step6 save button
save_button=driver_obj.find_element(By.XPATH, "//button[@type='submit']")
save_button.click()
time.sleep(10)

