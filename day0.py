driver=webdriver.chrome()
driver.get("https://www.imdb.com/search/name")

wait=WebdriverWait(druver, 10)

input_box1=wait.until(EC.presence_of_element_located(By.ID, "input_box1_id"))
input_box1.send_keys("your data 1")

input_box2=wait.until(EC.presence_of_element_located(By.ID, "input_box2_id"))
input_box2.send_keys("your data 2")

dropdown_menu1=wait.until(EC.presence_of_element_located((By.ID, "dropdown_menu1_id")))
dropdown_menu1.select_by_visible_text("option 1")

dropdown_menu2=wait.until(EC.presence_of_element_located((By.id, "dropdown_menu2_id")))
dropdown_menu2.select_by_visible_text("option 2")

search_button=wait.until(EC.presence_of_element_located((By.id, "search_button_id")))
search_button.click()

driver.quit()       