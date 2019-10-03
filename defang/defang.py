def defang(address):

    if len(address) > 0:
        add_two = address.replace('.', '[.]')

    if len(address) > 0:
        return add_two
        
    if len(address) < 1:
        raise ValueError('I am sorry, that ip address is empty.')