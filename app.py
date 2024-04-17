import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style

# Function to send a message to the chatbot
def send_message(driver, message):
    try:
        # Find the input textarea element for the chat
        input_box = driver.find_element(By.CSS_SELECTOR, "textarea.m-0")

        # Send the message to the chat
        input_box.send_keys(message)
        input_box.send_keys(Keys.RETURN)  # Press the "RETURN" key

        # Wait for the chatbot to respond (adjust wait time as needed)
        time.sleep(5)

    except Exception as e:
        print(f"{Fore.RED}An error occurred while sending message: {e}{Style.RESET_ALL}")

# Function to extract the chatbot response
def extract_chatbot_response(driver, words):
    try:
        # Calculate the delay based on the number of words
        delay = len(words) * 0.5
        time.sleep(delay)

        # Find the element containing the chatbot response
        response_element = driver.find_element(By.CSS_SELECTOR, "div.prose.dark\:prose-invert.flex-1 p")

        # Extract the text from the response element and limit its length
        response_text = response_element.text.strip()[:1000]  # Limit to 1000 characters

        # Print the chatbot response
        print(f"{Fore.GREEN}Chatbot response: {response_text}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}An error occurred while extracting chatbot response: {e}{Style.RESET_ALL}")

# Set up options for headless mode
options = Options()
options.add_argument('-headless')  # Set headless mode

# Initialize Firefox webdriver with headless option
driver = webdriver.Firefox(options=options)

# Navigate to the website
driver.get("https://chatgptnologin.com/chatbot")

while True:
    # Wait for the page to load completely
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.m-0")))

    # Click the "New chat" button
    new_chat_button = driver.find_element(By.CSS_SELECTOR, "button.text-sidebar.flex")
    new_chat_button.click()

    # Take input for the question
    question = input("Enter your question for the chatbot (type 'quit' to exit): ")

    if question.lower() == 'quit':
        break

    # Send the question to the chatbot
    send_message(driver, question)

    # Extract the chatbot response
    extract_chatbot_response(driver, question.split())

# Close the browser window
driver.quit()
