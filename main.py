import os

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time

load_dotenv()

EDGE_DRIVER_PATH = os.getenv("EDGE_DRIVER_PATH")
CARUSO_HEALH_FORM_SITE = os.getenv("CARUSO_HEALH_FORM_SITE")
SP_HEALTH_FORM_SITE = os.getenv("CARUSO_HEALH_FORM_SITE")
CARUSO_FNAME = os.getenv("CARUSO_FNAME")
CARUSO_LNAME = os.getenv("CARUSO_LNAME")
SP_FNAMES = os.getenv("SP_FNAMES")
SP_LNAME = os.getenv("SP_LNAME")


def fill_caruso_school_form():

    driver.get(CARUSO_HEALH_FORM_SITE)

    button_next1 = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")
    button_next1.click()

    input_fname = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    input_fname.send_keys(CARUSO_FNAME)

    input_lname = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_lname.send_keys(CARUSO_LNAME)

    button_drop_down = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    button_drop_down.click()
    time.sleep(1)
    # drop_down_grade = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div')
    # drop_down_grade.click()
    # time.sleep(1)
    sixth_grade = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]/span')))
    sixth_grade.click()
    time.sleep(1)
    # WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[5]')))
    button_next2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    button_next2.click()

    radio_button1 =driver.find_element(By.XPATH, '//*[@id="i11"]/div[3]/div')
    radio_button1.click()
    time.sleep(1)
    button_next3 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    button_next3.click()

    radio_button2 = driver.find_element(By.XPATH, '//*[@id="i11"]/div[3]/div')
    radio_button2.click()
    time.sleep(1)
    button_next4 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    button_next4.click()

    radio_button3 = driver.find_element(By.XPATH, '//*[@id="i8"]/div[3]/div')
    radio_button3.click()
    time.sleep(1)
    button_next5 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    button_next5.click()

    radio_button4 = driver.find_element(By.XPATH, '//*[@id="i8"]/div[3]/div')
    radio_button4.click()
    radio_button5 = driver.find_element(By.XPATH, '//*[@id="i16"]/div[2]')
    radio_button5.click()
    time.sleep(1)
    button_next6 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    button_next6.click()

    radio_button6 = driver.find_element(By.XPATH, '//*[@id="i5"]/div[3]/div')
    radio_button6.click()
    time.sleep(1)
    button_next7 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    button_next7.click()
    time.sleep(1)
    button_submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    # button_submit.click()


def fill_sp_school_form(name):
    driver.get(SP_HEALTH_FORM_SITE)
    driver.maximize_window()

    button_next1 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    button_next1.click()

    input_fname = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    input_fname.send_keys(name)

    input_lname = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_lname.send_keys(SP_LNAME)

    button_drop_down = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]')
    button_drop_down.click()

    pop_up_window = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]')
    # pop_up_window.send_keys(Keys.END)

    for _ in range(1, 3):
        driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight',
                pop_up_window)
        time.sleep(1)

    grade = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[20]/span')))
    grade.click()
    time.sleep(1)
    button_next2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    button_next2.click()

    radio_button1 = driver.find_element(By.XPATH, '//*[@id="i11"]/div[3]/div')
    radio_button1.click()
    time.sleep(1)
    button_next3 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    button_next3.click()

    radio_button2 = driver.find_element(By.XPATH, '//*[@id="i11"]/div[3]/div')
    radio_button2.click()
    time.sleep(1)
    button_next4 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    button_next4.click()

    radio_button3 = driver.find_element(By.XPATH, '//*[@id="i8"]/div[3]/div')
    radio_button3.click()
    time.sleep(1)
    button_next5 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    button_next5.click()

    radio_button4 = driver.find_element(By.XPATH, '//*[@id="i8"]/div[3]/div')
    radio_button4.click()
    radio_button5 = driver.find_element(By.XPATH, '//*[@id="i16"]/div[2]')
    radio_button5.click()
    time.sleep(1)
    button_next6 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    button_next6.click()

    radio_button6 = driver.find_element(By.XPATH, '//*[@id="i5"]/div[3]/div')
    radio_button6.click()
    time.sleep(1)
    button_next7 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    button_next7.click()
    time.sleep(1)
    button_submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    button_submit.click()

# ---------------------------------MAIN------------------------------------------ #


service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service)

fill_caruso_school_form()
for name in SP_FNAMES:
    fill_sp_school_form(name)

driver.close()
