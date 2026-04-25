#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    """
    Şablon və iştirakçı siyahısı əsasında fərdi dəvətnamələr yaradır.
    """
    
    # Giriş tiplərinin yoxlanılması (Input Type Validation)
    if not isinstance(template, str):
        print("Error: template must be a string. Got: {}".format(type(template).__name__))
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Boş girişlərin yoxlanılması (Empty Input Handling)
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Hər bir iştirakçı üçün emal prosesi
    for i, attendee in enumerate(attendees, start=1):
        personalized_invitation = template
        
        # Placeholder siyahısı
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            # Əgər məlumat yoxdursa və ya None-dırsa, "N/A" ilə əvəz et
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # Şablondakı {key} hissəsini real dəyərlə əvəz et
            target = "{" + key + "}"
            personalized_invitation = personalized_invitation.replace(target, str(value))
        
        # Faylın yaradılması
        filename = "output_{}.txt".format(i)
        
        try:
            with open(filename, 'w') as f:
                f.write(personalized_invitation)
        except Exception as e:
            print("Error writing to {}: {}".format(filename, e))
