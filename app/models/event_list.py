from app.models.event import *


event1 = Event("19/11/2020", "Playstation 5 launch event", 400, "Internet", "YOU'RE NOT GOING TO GET ONE")
event2 = Event("10/12/2020", "Playstation 5 new Stock event", 600, "Internet", "STILL NOT GOING TO GET ONE")
events = [event1, event2]

def add_new_event(event):
    events.append(event)