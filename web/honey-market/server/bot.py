from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import selenium
from multiprocessing import Process
from settings import *
from app import app # 
import time

# Main URL for login
ADMIN_URL_LOGIN = "http://127.0.0.1:5000/admin/login"

def visit_website_process(url):

    # Disable unnecessary settings to boost performance and lower memory
    options = Options()
    options.add_argument("headless")
    options.add_argument("no-sandbox")
    options.add_argument("ignore-certificate-errors")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("disable-infobars")
    options.add_argument("disable-background-networking")
    options.add_argument("disable-default-apps")
    options.add_argument("disable-extensions")
    options.add_argument("disable-gpu")
    options.add_argument("disable-sync")
    options.add_argument("disable-translate")
    options.add_argument("hide-scrollbars")
    options.add_argument("metrics-recording-only")
    options.add_argument("no-first-run")
    options.add_argument("safebrowsing-disable-auto-update")
    options.add_argument("media-cache-size=1")
    options.add_argument("disk-cache-size=1")

    # driver = webdriver.Firefox(service = service, options = options)
    driver = webdriver.Chrome(options=options)
    driver.get(ADMIN_URL_LOGIN)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login"))
        )
        driver.find_element(By.NAME, "username").send_keys(ADMIN_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(ADMIN_PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
    except selenium.common.exceptions.TimeoutException:
        print("[ERROR]: Unable to locate element #login, aborted. :(")
        return

    # Wait until the login process has finished
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "frame")))
    except selenium.common.exceptions.TimeoutException:
        print("[ERROR]: Unable to locate element #login, aborted. :(")
        return

    driver.get(url)
    print(f"* Bot visited url -> {url}")

    time.sleep(10) # wait for 10 seconds then sayonara

    driver.get("http://127.0.0.1:5000/logout")
    time.sleep(2)
    driver.quit()

def visit_website(url):
    Process(target=visit_website_process, args=[url]).start()

# UUggg me brain writing code at 3AM goes... DA HAIL U DOIN LA ? SSTTUUBID