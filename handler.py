import json

def response_handler(body, platypoints, state, name):
    message = ""
    if body == "r":
        message = "Restarting!"
        platypoints = 0
        state = 0
        name = ""
        return message, platypoints, state, name
    if platypoints >= 10:
        message = """You gave away your position.
        You have been recaptured and will spend the rest of
        your days at the local zoo."""
        platypoints = 0
        state = 0
        name = 0
        return message, platypoints, state, name
    if state == 0:
        #send_media(fromnumber, tonumber, https://s-media-cache-ak0.pinimg.com/736x/6b/d7/32/6bd73287df00888931972bbf8425f6a9.jpg)
        return """You are a platypus. You were once captured and put into a zoo, but you escaped. 
        Now as a rogue platypus, you must integrate yourself into human society. 
        Your actions determine how obvious it is that you are actually a platypus, not a human. 
        Actions that are non-humanlike add platypoints to your platypoints score. 
        If you go over 10 platypoints, then you are fully visible to all people, and you will be discovered as a 
        rogue platypus, leading to your reincarceration at the local zoo 
        Are you ready? Type yes if ready!""" , platypoints, state+1, name
    if state == 1:
        if body == "yes":
            message = "What is your name?"
            return message, platypoints, state+1, name
        else:
            message = "how about now?"
            return message, platypoints, state, name
    if state == 2:
        name = body
        message = """Welcome to the platyteam %s. Be as inconspicuous as possible.
        Two days have passed since your escape.
        You are feeling hungry, and decide it is time to go buy groceries.
        after a 10 minutes drive, with enjoyable music, you arrive at the store.
        What do you do at the grocery store?
        type 1 if you take a shopping cart and buy food.
        type 2 if you grab ice from a bag and throw it at the wall.
        type 3 if you pee in the corner, marking your territory.
        >""" %name
        return message, platypoints, state+1, name
    if state == 3:
        print state
        if body == "1":
            platypoints += 2
            message = """You managed to make it to the checkout line until the cashier asked for ID.
            You broke into a sweat and and looked around. You found nothing.
            You look back at the cashier, who is staring expectingly. 
            You throw your money onto the checkout stand and run away.
            The cashier doesn't care about their job enough to chase you.
            You get away.
            You are at %d platypoints!
            Later in the week, you realize that you need to do your laundry.
            You have no washer or dryer, so you run down to the laundromat.""" %platypoints
            return message, platypoints, state+1, name
        elif body == "2":
            platypoints += 5
            message = """The store manager came out to talk to you.
            The manager asked you why you were throwing ice at the wall.
            You are illiterate and cannot speak English.
            You pee on the manager's shoe and escape.
            You are at %d platypoints! Later in the 
            week, you realize that you need to do your laundry.
            You have no washer or dryer, so you run down to the laundromat.""" % platypoints
            return message, platypoints, state+1, name
        elif body == "3":
            platypoints += 8
            message = """You mark your territory.
            Everyone passing by stares at you.
            You don't understand embarassement so you waddle in your pee.
            You leave a few hours later, not realizing what you have done.
            You are at %d platypoints!
            Later in the week, you realize that you need to do your laundry.
            You have no washer or dryer, so you run down to the laundromat.
            What do you do at the laundromat?
            type 1 if you realize you have no laundry detergent so you use shampoo
            type 2 if you drink the free coffee until closing time
            type 3 if you eat someone's sock""" % platypoints
            return message, platypoints, state+1, name
        else:
            message = """You have compromised your position, platydummy! 
            Go back to the start!"""
            state = 0
            name = ""
            return message, platypoints, state, name
    if state == 4:
        if body == "1":
            platypoints += 5
            message = """The store staff takes a picture of you and hangs it on the wall.
            The frame reads "The biggest idiot of the year"
            The whole city knows about you.
            You are at %d platypoints!""" %platypoints
            return message, platypoints, state+1, name
        elif body == "2":
            platypoints += 3
            message = """The manager asks you to leave at closing time, but you continue drinking coffee.
            You are hyped up to the point where you don't know where you are.
            You are zooming at light speed through the galaxy.
            You don't see the manager. The manager is nothing in the universe.
            You see all truth. You see the future.
            You are enlightened. 
            You now know all of the answers in the universe, and have seen all good and evil.
            You wake up in a puddle of your drool on the sidewalk.
            You are at %d platypoints!""" %platypoints
            return message, platypoints, state+1, name
        elif body == "3":
            platypoints += 8
            message = """The sock tastes good. You eat another one. Then another.
            Soon enough, all socks have been devoured. 
            The crisp taste compliments the socks texture.
            You are addicted to eating socks.
            You are at %d platypoints!""" %platypoints
            return message, platypoints, state+1, name
        else:
            message = """You can't do that!"""
            return message, platypoints, state, name
    if state == 5 and platypoints >= 10:
        message = "You almost made it, but you slipped up. Try again! Hit R to restart!"
        platypoints = 0
        state = 0
        name = ""
        return message, platypoints, state, name
    else:
        return"""Good job, you are now a certified human.
        Enjoy using your apposable thumbs. You win!""", platypoints, state, name


'''
def response_handler(body):
    json1_file = open('dictionary.json')
    json1_str = json1_file.read()
    dictionary = json.loads(json1_str)
    
    print dictionary['BABY']

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
'''