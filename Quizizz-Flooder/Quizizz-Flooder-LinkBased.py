def main() :

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import time

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://quizizz.com/join/pre-game/running/U2FsdGVkX188ZgN5Uak0kKSgh8ocr2LmhHoKdbqnehicfk8OfyhIn1wdwGcO7Mf%252F4myYm6g5%252BmSOHI%252FtUnqGQ1E1NhSB55zBclmN3I1vTLlHelZZAJ%252Fu50ISpbTND1tlNJ%252FvDmTNEHBxS5R%252F6iLg4F6MqCT5MNMRSvQ0Hb%252B72d8%253D/start")


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