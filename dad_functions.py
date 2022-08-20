import requests

def dad_message(input):
    """ Function to see if message should return a dad joke or not
    return: boolean
    """

    check = str(input)
    if check.lower() == "hello":
        return True
    return False

def dad_text():
    """Function to get dad joke from the API
    return: string
    """

    reply = requests.get('https://icanhazdadjoke.com', headers={"Accept":"text/plain"})
    return reply.text