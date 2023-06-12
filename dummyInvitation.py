#!/usr/bin/env python3

def print_sample_invitation(mother, father, child, teacher, event):

    sample_text = f'''
    Dear {mother} and {father}.
    {teacher} and I would love to see you both as well as {child} at our {event} tomorrow

    Best regards,
    Principal G. Sturgis.
    '''

    print(sample_text)

    
print_sample_invitation('Denise', 'Randy', 'Jared', 'Dr. Reid', 'Class session 1')


