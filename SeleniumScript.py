from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = 'C:/chromedriver-win64/chromedriver.exe'

chrome_options = Options()

chrome_service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.saucedemo.com/")

    user_name_element = driver.find_element(By.ID, 'user-name')
    user_name_element.send_keys('standard_user')

    password_element = driver.find_element(By.ID, 'password')
    password_element.send_keys('secret_sauce')

    password_element.send_keys(Keys.RETURN)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list')))

    add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, 'btn_inventory')
    add_to_cart_buttons[0].click()
    add_to_cart_buttons[1].click()

    cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_badge.text == '2', f"Expected 2 items in the cart, but found {cart_badge.text}"

    print("Successfully added 2 items to the cart")

    cart_icon = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_icon.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cart_item')))

    cart_items = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    for item in cart_items:
        print(f"Cart item: {item.text}")

    menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    menu_button.click()

    logout_link = wait.until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
    logout_link.click()

    wait.until(EC.presence_of_element_located((By.ID, 'login-button')))

    print("Successfully logged out")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
