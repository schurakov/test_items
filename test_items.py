from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    add_to_basket_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert add_to_basket_button.is_displayed(), "Add to basket button is unvisible"

