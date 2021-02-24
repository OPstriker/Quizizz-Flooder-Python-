def main():

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import time

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://quizizz.com/join")

    search = driver.find_element_by_class_name("check-room-input")
    search.send_keys("297936")
    search.send_keys(Keys.RETURN)

    try: 

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "player-name-generator-icon"))
            
        )
        element.click()

        time.sleep(1) 

        search = driver.find_element_by_class_name("enter-name-field")
        search.send_keys(Keys.RETURN)

    finally: 

        time.sleep(2)
        driver.close()
        main()
main()
    
        





