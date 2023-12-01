import os
from pushbullet import API
from dotenv import load_dotenv


def send_alert(message, recipient):
    # set the API Class and link it to the api object
    api = API()

    # Load the .env file
    load_dotenv()

    # Now you can access the environment variable
    access_token = os.getenv(recipient)
    api.set_token(access_token)

    # now you can use the API Wrapper

    # sending a note, arguments: title, message
    api.send_note(
        "Update",
        message)
