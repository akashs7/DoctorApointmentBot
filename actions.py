# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from datetime import datetime

import logging
import requests
import json
from rasa_sdk.interfaces import Action
import pandas as pd

logger = logging.getLogger(__name__)

class ActionAppointment(Action):
    def name(self):
        return "action_appointment"
        

    def run(self, dispatcher, tracker, domain):
        specialist = tracker.get_slot('specialist')
        print(specialist)
        df = pd.read_csv("doctor.csv")
        print(df)
        doc = df.where(df['Specialization'].str.lower() == specialist.lower())
        doc = doc.dropna()
        print(doc)
        if not doc.empty:
            doctorname = doc.iloc[0,0]
            timings = doc.iloc[0,3]
            contactnumber = int(doc.iloc[0,4])
            days = doc.iloc[0,2]
            rating = int(doc.iloc[0,5])
            print (doctorname)
            print(contactnumber)
            response = """The doctor for {} is {}\nOpen hours are {}, {}\nThe contact number is {}\nRating is {} stars""".format(specialist, 
            doctorname, timings, days, contactnumber, rating)
            
        else:
            response = """Could not find the doctor for {}""".format(specialist)
        dispatcher.utter_message(response)
        
        return []
        

        def run(self, dispatcher, tracker, domain):
            name = tracker.get_slot('name')
            time = tracker.get_slot('time')
            confirmresp = """Your appointment with Dr. {} is confirmed for {}""".format(name, time) 
            dispatcher.utter_message(confirmresp)

            return []
    