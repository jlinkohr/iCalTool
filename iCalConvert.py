# adjust iCal files e.g. notifications
# 2022 Jochen Linkohr
# start code done with help of Chat GPT

import icalendar
from datetime import timedelta

# Open the input .ics file
with open('calendar.ics', 'rb') as f:
    # Parse the file into a Calendar object
    calendar = icalendar.Calendar.from_ical(f.read())

# Loop through all events in the calendar
for component in calendar.walk():
    # Check if the component is an event
    if component.name == "VEVENT":
        # add alarms
        alarm = icalendar.Alarm()
        trigger = -timedelta(hours=12)
        alarm.add('TRIGGER', trigger)
        alarm.add('ACTION', 'DISPLAY')
        component.add_component(alarm)
      
#Open a new .ics file for writing
with open('modified_calendar.ics', 'wb') as f:
    # Write the modified calendar to the file
    f.write(calendar.to_ical())
