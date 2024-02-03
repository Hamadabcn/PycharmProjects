import webbrowser

address = input('Enter an address: ')  # get the address from the user

webbrowser.open('https://www.google.com/maps/place/' + address)  # open the web browser with the address

