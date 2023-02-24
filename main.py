from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_forms.asp")

var= driver.find_element_by_class_name("fav_language")

print(var.is_selected())

var2=driver.find_element_by_id("css")
print(var2.is_selected())


driver.quit()   

