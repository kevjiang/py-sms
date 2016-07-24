def response_handler(body):
    message = ""
    if body == 'start':
        message = "You are in a boring class.  Do you 'take a nap' or 'take notes'?"
    elif body == 'take a nap':
        message = "You fall asleep forever...and ever...and ever.  Do you want to 'start' over?"
    elif body == 'take notes':
        message = "You furiously take notes as the teacher drones on.  Your friend taps you on the shoulder.  Do you 'turn around' or keep looking at your 'notes'"
    elif body == 'turn around':
        message = "You turn around, only to find that you have just stared into the eyes of a basilisk!  Oh well...do you want to 'start' over?"
    elif body == 'notes':
        message = "Unfortunately, this game is incomplete...please come back later for more!  Do you want to 'start' over?"
    else:
        message = "Invalid command.  Text 'start' to restart the game.  Or text 'pic please' for a random picture"
    return message