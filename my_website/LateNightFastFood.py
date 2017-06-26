#LateNightFastFood v01
#Interactive Fiction
#Janet Hartkopf and Jacque Whitaker

#Introduction Setup
def introduction():
  print "\nTwo teens driving through a rural southern state late at night."
  print "Follow their quest to determine the outcome."
  
def go_home():
  print "\nYou made it home in time for curfew but starving!"
  
def determine_character():
  print "\nAre you the driver or a passenger?"
  print "Type d for driver and p for passenger."
  character = raw_input()
  if character == "d" :
    print "You must be the driver."
  else :
    print "You must be the copilot."
    
def question_appetite():
  print "\nAre you hungry?"
  print "Type y for yes and n for no."
  answer = raw_input()
  if answer == "n" :
    go_home()
  else :
    where_will_you_eat()
    
def where_will_you_eat():
  print "\nWhere to?"
  print "Type f for fast food and s for sit-down."
  answer = raw_input()
  if answer == "s" :
    go_home()
  else :
    print "Head to junk food alley."
    order_your_food()

def order_your_food():
  print "\nWhat do you want for your main item?"
  print "Type c for chicken, b for burger, or f for fish."
  entree = raw_input()
  print "\nWhat about for your side order?"
  print "Type c for coleslaw, f for French fries, or b for beans."
  side = raw_input()
  print "\nWhat would you like to drink?"
  print "Type t for sweet tea, p for pepsi, or l for lemonade."
  drink = raw_input()
  assembly_order(entree, side, drink)
  
def assembly_order(entree, side, drink):
  if entree == "c" :
    entree = "chicken"
  elif entree == "b" :
    entree = "fish"
  else :
      entree = "burger"
  if side == "c" :
    side = "coleslaw"
  elif side == "f" :
    side = "beans"
  else :
    side = "fries"
  if drink == "t" :
    drink = "sweet tea"
  elif drink == "p" :
    drink = "lemonade"
  else :
    drink = "pepsi"
  bagged_order(entree, side, drink)
  
def bagged_order(entree, side, drink):
  print "\nThank you for your order!"
  print "Here's your order. And, you drive away..."
  print "\nDid you get what you thought you ordered or did you just get Southern hospitality?"
  print "\nYou received:"
  print "Your main dish is %s, the side is %s, and your drink is %s" % (entree, side, drink)
  
def done():
  print "\nDo you want to make another order?"
  print "Type y for yes or n for no"
  answer = raw_input()
  return answer
  
  
def run_program():
  introduction()
#  not_done = y
  #while not_done :
  determine_character()
  question_appetite()
  #  not_done = done()
    
run_program()

