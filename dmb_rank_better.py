import random


def intro():
    # Simple intro of the program with instructions
    # used input to allow user to read instructions easier
    # as well as one at a time
    print("Hello and welcome")
    input("Please press the enter key after each statement the program says")
    input("We're gonna play a game today.")
    print("It's called, Rank these 5 Dave Matthews Band Songs")
    input("without knowing what come next.")
    input("You will be given 5 random songs")
    input("You won't know what song comes next.")
    input("You will then have to rank that item on a top 5 list")
    input("If you like the song rank it higher, if not rank it lower")
    input("You can only rank one song per number")
    input("so only one thing at number 1 and so on.")
    input("Let's begin")


intro()


def DMB():
    # gets user ranking of an item from an input
    # will return where the user ranked each item on their top 5 list
    song_choices = \
        ["I'll Back You Up", 'Recently', 'Typical Situation', 'Christmas Song',
         'Seek Up', 'Dancing Nancies', 'Satellite', 'Ants Marching',
         'Warehouse', 'Jimi Thing',
         '#34', 'Lover Lay Down',
         'Two Step', 'Crash Into Me'
         'Too Much', '#41',
         'Lie In Our Graves',
         'Tripping Billies', 'Rapunzel',
         'Halloween', 'The Last Stop',
         '#40', 'Crush',
         'The Stone', 'Everyday',
         'Space Between', 'I Did it',
         'Angel', 'Busted Stuff',
         'Grey Street', 'Grace is Gone',
         'Bartender', 'Old Dirt Hill',
         'Hello Again', 'Dream Girl',
         'American Baby', 'Louisiana Bayou',
         'Grave Digger', 'Some Devil',
         'So Damn Lucky', 'Oh',
         'Grux', 'Why I am',
         'Alligator Pie', 'Spaceman'
         'Seven', 'Funny The Way It Is',
         'Broken Things', 'Belly Full',
         'Drunken Soldier', 'The Riff',
         'Virginia In The Rain', 'Again and Again',
         'Come Tomorrow', 'Samurai Cop',
         'Walk Around The Moon', "Madman's Eyes",
         'Looking For a Vein', 'Monsters',
         '#27', 'Eh Hee',
         'Beach Ball', 'Corn Bread',
         'Bismark', 'Blackjack',
         'JTR', 'Sister',
         'Kill The Preacher',
         'Anyone Seen The Bridge?',
         'All Along The Watchtower', 'Cha Cha',
         "Let's Dance", 'Melissa',]
    random.shuffle(song_choices)  # changes the choice order
    user_rankings_1 = {}  # will be used to store user rankings
    songs = [song_choices.pop() for _ in range(5)]  # user won't get the
    #  same choice twice

    for song in songs:
        while True:
            try:  # assures user enters a number
                user_choice = int(input(f"Where would you rank {song}?: "))
                if 1 <= user_choice <= 5 and \
                        user_choice not in user_rankings_1.values():
                    user_rankings_1[song] = user_choice
                    # adds ranking to dictionary
                    break
                else:
                    print("You already ranked a song at that spot")
            except ValueError:
                print("Please enter a number.")
    print("Here are your rankings...")
    for song, user_choice in user_rankings_1.items():
        print(f"You ranked {song} at {user_choice}")
    user_play_again = input("Would you like to play again? ")
    if user_play_again.lower() == "yes":
        DMB()
    elif user_play_again.lower() == "no":
        input("Thank you for playing.")


DMB()
