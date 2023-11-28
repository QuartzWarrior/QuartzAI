from selenium import webdriver
from undetected_chromedriver import Chrome, ChromeOptions

# Set up Chrome options
options = ChromeOptions()

# Set up the webdriver using Undetected Chromedriver
driver = Chrome(options=options, headless=True)


driver.get("https://chat.openai.com")

# Find and click on the "Sign up" button
signup_button = driver.find_element_by_xpath("//button[contains(text(), 'Sign up')]")
signup_button.click()

# Fill in the account creation form
name_input = driver.find_element_by_id("name")
name_input.send_keys("Your Name")

email_input = driver.find_element_by_id("email")
email_input.send_keys("your_email@example.com")

password_input = driver.find_element_by_id("password")
password_input.send_keys("your_password")

# Submit the form
submit_button = driver.find_element_by_xpath(
    "//button[contains(text(), 'Create account')]"
)
submit_button.click()

# Wait for the account creation process to complete
# You may need to add additional wait logic here depending on the website behavior

# Close the webdriver
driver.quit()
