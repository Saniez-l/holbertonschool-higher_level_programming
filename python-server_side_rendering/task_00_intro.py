#!/usr/bin/python
'''
Module creating a Simple Templating
'''
import os


def generate_invitations(template, attendees):
    '''
    Generate personalized invitation
    '''
    # verifie template empty
    if not template:
        print('Template is empty, no output files generated.')
        return
    # verifie attendees empty
    if len(attendees) == 0:
        print('No data provided, no output files generated.')
        return
    # verifie template is str
    if not isinstance(template, str):
        print('Template must be a string.')
        return
    # verifie attendees is list of dict
    if (
        not isinstance(attendees, list)
        or not all(isinstance(a, dict) for a in attendees)
    ):
        print("Error: Attendees must be a list of dictionaries.")
        return

    for index, person in enumerate(attendees, start=1):
        output_filename = f"output_{index}.txt"
        invitation_text = template

        for key in ["name", "event_title", "event_date", "event_location"]:
            value = person.get(key) or "N/A"
            invitation_text = invitation_text.replace(f"{{{key}}}", str(value))

        # write file
        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(invitation_text)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
