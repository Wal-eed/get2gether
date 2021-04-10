# Get2Gether
An clean, elegant solution to let people decide on a common time to meet up. An event organizer simply creates an event, sends out invites to users who can fill it in with one button press (the app can sync from their Google Calendar and automatically block any times they have an event at, or from a preset), and submit. After all users have submitted, the organizer can see the best times, and confirm the event. 

# How it works:
The website uses a React frontend to display and manage the timetable. In the demo, two dummy user profiles exist on the frontend which are then used, so for the demo only, the frontend does not communicate with the backend. However, most, if not all, the functionality needed to execute interactions with the Google Calendar API such as fetching their calendar, storing their free times, and adding a new event upon event confirmation has been implemented in the backend, so please feel free to take a look. 

At the end once users have filled in the prefrences, the times are highlighted from least common to most common times, as shown by the legend in the bottom left.

# Credits:

Some frontend elements used from: https://github.com/cruip/open-react-template/ 

