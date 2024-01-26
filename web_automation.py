#import
from selenium import webdriver
import time

def perform_web_actions(command):
    # Initialize WebDriver
    driver = webdriver.Chrome()

    try:
        if "open website" in command:
            website = command.split("open website")[1].strip()
            open_website(driver, website)

    except Exception as e:
        print(f"Error performing web actions: {e}")

    finally:
        # CLose the browser window

        if driver:
            driver.quit()


# define open_web function

def open_website(driver, website):
    #Open the specified website
    driver.get(f"https://www.{website}.com")
    print(f"Opened website: {website}")
    time.sleep(3)