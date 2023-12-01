import requests
from bs4 import BeautifulSoup

# Function to check for course availability
def check_course_availability(url, course_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all courses that match the title
    course_cards = soup.find_all('h2', class_='card-header-title',
                                 string=lambda text: course_name in text)

    availability_messages = []
    for card_header in course_cards:
        card = card_header.find_parent('div', class_='card')
        if card:
            availability_info = card.find('div', class_='card-places')
            
            if availability_info:
                # print(f"The course '{course_name}' is mentioned on the website.")
                # print(f"Availability: {availability_info.get_text(strip=True)}")
                
                # Optional: Retrieve URL if needed
                link_element = card.find_parent('a', class_='card-link')
                if link_element and 'href' in link_element.attrs:
                    print(f"URL: {link_element['href']}")
                availability_messages.append(f"Availability: {availability_info.get_text(strip=True)}")
                
            else:
                print(f"The course '{course_name}' does not have 'card-places' info available.")
        else:
            print(f"Card structure for '{course_name}' is different than expected.")
    
    return availability_messages
