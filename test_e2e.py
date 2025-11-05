import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import chromedriver_autoinstaller

"""
    instanca browsera
    koja ce se koristiti u svakom testu
"""


@pytest.fixture()
def browser():
    # instaliraj chrome driver
    # ukoliko ne postoji
    if chromedriver_autoinstaller.get_chrome_version() is None:
        chromedriver_autoinstaller.install()
    # neophodno odraditi ovo zbog problema sa CORS
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-site-isolation-trials")
    # kreiraj instancu drajvera za test
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()


# Zadaci V7:
@pytest.mark.skip
def test_logovanje_student(browser: 'WebDriver'):
    browser.get("http://localhost:3000/auth/login")

    username_input = browser.find_element(By.ID, 'username')
    password_input = browser.find_element(By.ID, 'password')

    login_dugme = browser.find_element(By.XPATH, '//*[@id="root"]/main/div/form/button')

    username_input.send_keys('student_e2_1')
    password_input.send_keys('student1234!')

    login_dugme.click()

    korisnici_title = browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div[2]/div/div/div[1]/h4')
    profil_ikonica = browser.find_element(By.XPATH, '//*[@id="avatar-button"]')

    assert korisnici_title.text == "Korisnici"
    assert profil_ikonica != None
    assert browser.title == "FTN Student"


@pytest.mark.skip
def test_failed_login_student(browser: 'WebDriver'):
    browser.get("http://localhost:3000/auth/login")

    username_input = browser.find_element(By.ID, 'username')
    password_input = browser.find_element(By.ID, 'password')

    username_input.send_keys('student_e2_1')
    password_input.send_keys('student12345!')

    login_btn = browser.find_element(By.XPATH, '//*[@id="root"]/main/div/form/button')
    login_btn.click()

    error_msg = browser.find_element(By.XPATH, '//*[@id="root"]/main/div/div[1]/div')

    assert error_msg != None
    assert browser.find_element(By.XPATH,
                                '//*[@id="root"]/main/div/div[1]/div/div[2]').text == "Neispravni kredencijali"


@pytest.mark.skip
def test_no_input_login(browser: 'WebDriver'):
    browser.get("http://localhost:3000/auth/login")

    login_btn = browser.find_element(By.XPATH, '//*[@id="root"]/main/div/form/button')
    login_btn.click()

    username_validation = browser.find_element(By.XPATH, '//*[@id="username-helper-text"]')
    password_validation = browser.find_element(By.XPATH, '//*[@id="password-helper-text"]')

    assert username_validation != None
    assert password_validation != None


# Priprema K3.pdf:

def test_pace_calculator(browser: 'WebDriver'):
    browser.get("https://www.calculator.net/")

    pace_href = browser.find_element(By.XPATH, '//*[@id="hl2"]/li[6]/a')
    pace_href.click()

    time_tab_href = browser.find_element(By.XPATH, '//*[@id="topmenu"]/ul/li[2]/a')
    time_tab_href.click()

    distance_input = browser.find_element(By.ID, 'cdistance')
    distance_input.clear()
    distance_input.send_keys('55')

    pace_input = browser.find_element(By.ID, 'cpace')
    pace_input.clear()
    pace_input.send_keys('2:15:55')

    pace_select = browser.find_element(By.XPATH, '//*[@id="calinputpace"]/tbody/tr/td[3]/select')
    pace_dropdown = Select(pace_select)

    pace_dropdown.select_by_visible_text("Per Kilometer")

    browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/form/div[2]/table[4]/tbody/tr/td/input[2]').click()

    result = browser.find_element(By.XPATH, '//*[@id="content"]/p[2]/font/b')

    assert result.text == "124 hours, 35 minutes, and 25 seconds"


def test_pace_calculator2(browser: 'WebDriver'):
    browser.get("https://www.calculator.net/")

    pace_href = browser.find_element(By.XPATH, '//*[@id="hl2"]/li[6]/a')
    pace_href.click()

    time_tab_href = browser.find_element(By.XPATH, '//*[@id="topmenu"]/ul/li[2]/a')
    time_tab_href.click()

    distance_input = browser.find_element(By.ID, 'cdistance')
    distance_input.clear()

    pace_input = browser.find_element(By.ID, 'cpace')
    pace_input.clear()

    pace_select = browser.find_element(By.XPATH, '//*[@id="calinputpace"]/tbody/tr/td[3]/select')
    pace_dropdown = Select(pace_select)

    pace_dropdown.select_by_visible_text("Per Kilometer")

    browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/form/div[2]/table[4]/tbody/tr/td/input[2]').click()

    result = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]')

    assert result != None
    assert browser.find_element(By.XPATH,
                                '//*[@id="content"]/div[2]/div[1]/font').text == "Please provide positive distance value."
    assert browser.find_element(By.XPATH,
                                '//*[@id="content"]/div[2]/div[2]/font').text == "Please provide a valid pace value in the format of hh:mm:ss."


# Moja aplikacija:

@pytest.mark.skip
def test_logovanje_aeroletovi(browser: 'WebDriver'):
    browser.get("http://localhost:8080/PrviMavenVebProjekat/")

    login_dugme = browser.find_element(By.XPATH, '//*[@id="navcol-6"]/ul/li[3]/a')
    login_dugme.click()

    username_input = browser.find_element(By.ID, 'korisnickoIme')
    password_input = browser.find_element(By.ID, 'lozinka')

    username_input.send_keys('pera')
    password_input.send_keys('pera123')

    prijava_btn = browser.find_element(By.XPATH, '/html/body/div/form/button')
    prijava_btn.click()

    admin_button = browser.find_element(By.XPATH, '//*[@id="navcol-6"]/ul/a[2]')

    # time.sleep(10)

    assert admin_button != None
