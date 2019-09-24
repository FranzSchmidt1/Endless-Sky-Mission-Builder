""" Mission.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""

import logging

import src.model as model


class Mission(object):
    """The Mission class is the data structure that stores the data for an Endless Sky mission."""

    def __init__(self, mission_name):
        #TODO: remove default case after new parser is complete
        logging.debug("Building mission: %s" % mission_name)

        self.components = model.MissionComponents()
        self.missionName = mission_name
        self.missionLines = []

        self.parse_mission()
    #end init


    def print_mission_to_console(self):
        """Helper method to print out the formatted text of the mission. e.g.: what it will look like when saved"""
        print(self.missionLines)
    #end printMission


    def print_mission_lines_to_text(self):
        """Concatenate all the missionLines together. Used to make a block of text to display in the missionFrame."""
        # Note to self: this is the most efficient and pythonic way to concat all these strings together
        mission_text = "".join(self.missionLines)
        return mission_text
    #end print_mission_lines_to_text


    def parse_mission(self):
        parser = model.MissionParser(self)
        self.missionLines = parser.run()
    #end parse_mission


    def add_trigger(self):
        """Add a trigger object to this mission"""
        new_trigger = model.components.Trigger()
        self.components.triggerList.append(new_trigger)
        return new_trigger
    #end add_trigger


    def remove_trigger(self, trigger):
        """Remove a trigger object from this mission"""
        #print(trigger)
        self.components.triggerList.remove(trigger)
    #end remove_trigger
#end class Mission
