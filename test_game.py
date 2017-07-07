from eye_game import element_click, load_eye_game
from browser.browser import get_driver


def test_kret_level():
    driver = get_driver()
    load_eye_game(driver)

    for i in range (5):
        element_click(driver)
   # driver.find_element_by_class_name("character-title")





# class TestEye:
#
#     def test_sum(self):
#         assert 1 + 1 == 2
#
#     def test_2(self):
#         assert True
