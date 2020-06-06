import random
import json
import time

# We distribute wealth amont 10 people equally. Give 10$ each.
people_wealth = {
    "person_1": 10,
    "person_2": 10,
    "person_3": 10,
    "person_4": 10,
    "person_5": 10,
    "person_6": 10,
    "person_7": 10,
    "person_8": 10,
    "person_9": 10,
    "person_10": 10
}

round = 1
while round <= 30:

    # Betting starts in a round robin fashion.
    for person, persons_wealth in people_wealth.items():
        

        # Participate in betting only if you have 1$ left with you.
        if persons_wealth > 0:
            for person_betting_against, wealth_of_opponent in people_wealth.items():
                
                # Do not bet against yourself. 
                if person == person_betting_against:
                    continue
                
                # Do not bet against person who has no money.
                if wealth_of_opponent == 0:
                    continue
                
                # If you ran out of money in while you are in a betting round. Just stop. You are OUT ! 
                if persons_wealth == 0:
                    break

                # We pick a random number. 
                random_number = random.randint(0,99)
            
                # Person 1 wins if its Odd, Person 2 wins if its Even.
                if (random_number % 2) == 0:
                    wealth_of_opponent = wealth_of_opponent + 1
                    persons_wealth = persons_wealth - 1
                    winner = person_betting_against
                else:
                    wealth_of_opponent = wealth_of_opponent - 1
                    persons_wealth = persons_wealth + 1
                    winner = person
                
                print ("Betting between %s and %s: Winner is %s" % (person, person_betting_against, winner))

                people_wealth[person_betting_against] = wealth_of_opponent
                people_wealth[person] = persons_wealth
    
    print ("******************* Result after round number %s: *********************" % round)  
    print(json.dumps(people_wealth, indent=4, sort_keys=False))
    round = round + 1

    # Bettil thottavarkku oru shoda kudikkan ulla time :)
    time.sleep(0.5)
