def load_eye_game(driver):
    driver.get("https://www.igame.com/eye-test/")
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))


def element_click(driver):
    el = driver.find_element_by_class_name("thechosenone")
    print(el)
    el.click()


