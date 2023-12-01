import requests
from bs4 import BeautifulSoup

# Function to check for course availability
def check_course_availability(url, course_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Search for all instances of the course name
    courses = soup.find_all(string=lambda text: course_name in text)

    if courses:
        print(f"The course '{course_name}' is mentioned on the website.")
        for course in courses:
            parent_element = course.parent
            if parent_element.name == 'a':
                # Print out the URL if the mention is part of a link
                print(f"URL: {parent_element['href']}")
    else:
        print(f"The course '{course_name}' is not currently listed on the website.")

# The URL to monitor
url_to_monitor = "https://www.rcophth.ac.uk/events-courses/all-events-courses/"
course_to_look_for = "Introduction to Ophthalmic Surgery course"

# Call the function with the specified URL and course name
check_course_availability(url_to_monitor, course_to_look_for)
