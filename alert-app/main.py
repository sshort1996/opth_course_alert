from alert_app.course_availability import check_course_availability
from alert_app.send_alert import send_alert
import time 


# The URL to monitor
url_to_monitor = "https://www.rcophth.ac.uk/events-courses/all-events-courses/"
course_to_look_for = "Introduction to Ophthalmic Surgery course"

while True:
    # Call the function with the specified URL and course name
    status = check_course_availability(url_to_monitor, course_to_look_for)
    print(status)
    if 'places available' in status:
        send_alert(status, 'MY_API_KEY')
        send_alert(status, 'KULTUMIS_API_KEY')

    time.sleep(300)