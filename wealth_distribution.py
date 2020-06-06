import random
import json
import time
import numpy as np

def coinFlip():    
    # Probablity 
    p = .5
    #perform the binomial distribution (returns 0 or 1)    
    result = np.random.binomial(1,p)
    return result


# We distribute wealth among 10 people equally. Give 20$ each.
people_wealth = {
    "person_1": 20,
    "person_2": 20,
    "person_3": 20,
    "person_4": 20,
    "person_5": 20,
    "person_6": 20,
    "person_7": 20,
    "person_8": 20,
    "person_9": 20,
    "person_10": 20
}

round = 1
while round <= 300:

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
                head_or_tail = coinFlip()
                # 0 - Head
                # 1 Tail
                # Person 1 wins if its Odd, Person 2 wins if its Even.
                if head_or_tail == 0:
                    result = "Head"
                    wealth_of_opponent = wealth_of_opponent + 1
                    persons_wealth = persons_wealth - 1
                    winner = person_betting_against
                else:
                    result = "Tail"
                    wealth_of_opponent = wealth_of_opponent - 1
                    persons_wealth = persons_wealth + 1
                    winner = person
                
                print ("Betting between %s and %s: It's %s! and the winner is %s" % (person, person_betting_against, result, winner))

                people_wealth[person_betting_against] = wealth_of_opponent
                people_wealth[person] = persons_wealth
    
    print ("******************* Result after round number %s: *********************" % round)  
    print(json.dumps(people_wealth, indent=4, sort_keys=False))
    round = round + 1

