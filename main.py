start=int(input("Hi! What would you like to order today? Input 1 if you want to order; Input 2 if you want to exit."))

#ask again if the input is neither 1 nor 2
while  start != 1 and start != 2:
  start = int(input("Hi! What would you like to order today? Input 1 if you want to order; Input 2 if you want to exit. "))

#terminates
if start == 2:
  print("")
  print("Thank you for using this program!")
    
#start of the program
    
if start == 1:
  
#instruction to users
  print("")
  print("----------------------------")
  print("")
  print("Before you start, please take note that our program only accept:")
  print("")
  print("  1. A maximum amount of 3 orders.")
  print("  2. The order number of the type of food you are choosing.")
  print("")
  print("Thank you for your understanding! :)")
  print("")
  print("-------------------------------------------------")

#Menu
  print("")
  print("We provide the following:")
  print("")
  print("Main Dishes:")
  print("")
  print("ID:       Dish:               Price:")
  print("")
  print("1.        Chicken             ₱ 90.00")
  print("2.        Pork                ₱ 105.00")
  print("3.        Fish                ₱ 120.00")
  print("4.        Beef                ₱ 135.00")
  print("")
  print("Side Dishes:")
  print("")
  print("ID:       Dish:               Price:")
  print("")
  print("1.        Steamed Rice        ₱ 20.00")
  print("2.        Shredded Corn       ₱ 35.00 ")
  print("3.        Mashed Potatoes     ₱ 50.00")
  print("4.        Steam Vegetables    ₱ 65.00")
  print("")
  print("Drinks")
  print("")
  print("ID:       Dish:               Price:")
  print("")
  print("1.        Mineral Water       ₱ 25.00")
  print("2.        Iced Tea            ₱ 35.00")
  print("3.        Soda                ₱ 45.00 ")
  print("4.        Fruit Juice         ₱ 55.00")
  print("")
  print("------------------------------------------------")
  
  
#asking for the number of people
  print("")
  num_people = int(input("How many people are there in your group? "))

  while num_people <= 0: #when number of people is negative, ask again
    num_people = int(input("How many people are there in your group? "))

  #initial variable
  nxt1 = 'n'
  nxt3 = 'n'
  nxt5 = 'n'
  cancel = 'y'
  subtotal2 = 1
  subtotal3 = 1
  main2 = 0
  side2 = 0
  drink2 = 0
  main3 = 0
  side3 = 0
  drink3 = 0
      
  #start ordering
  while cancel == 'y':
    
    #Order 1
    while nxt1 == 'n':
      print("")
      print("----------------------------")
      print("")
      print("Order #1: ")
      print("")
    
      #asking for main dish
      main1 = int(input("Main Dish: ID #"))
      while main1 < 0 or main1 > 4:
        print("")
        print("We don't have this dish in our menu! Please try again :)")
        print("")
        main1 = int(input("Main Dish: ID #"))
      if main1 == 1:
        print("Type: Chicken")
      elif main1 == 2:
        print("Type: Pork")
      elif main1 == 3:
        print("Type: Fish")
      elif main1 == 4:
        print("Type: Beef")
      elif main1 == 0:
        print("Type: None")
    
      #asking for side dish
      print("")
      side1 = int(input("Side Dish: ID #"))
      while side1 < 0 or side1 > 4:
        print("")
        print("We don't have this dish in our menu! Please try again :)")
        print("")
        side1 = int(input("Side Dish: ID #"))
      if side1 == 1:
        print("Type: Steamed Rice")
      elif side1 == 2:
        print("Type: Shredded Corn")
      elif side1 == 3:
        print("Type: Mashed Potatoes")
      elif side1 == 4:
        print("Type: Steam Vegetables")
      elif side1 == 0:
        print("Type: None")
    
      #asking for drinks
      print("")
      drink1 = int(input("Drink: ID #"))
      while drink1 < 0 or drink1 > 4:
        print("")
        print("We don't have this dish in our menu! Please try again :)")
        print("")
        drink1 = int(input("Drink: ID #"))
      if drink1 == 1:
        print("Type: Mineral Water")
      elif drink1 == 2:
        print("Type: Iced Tea")
      elif drink1 == 3:
        print("Type: Soda")
      elif drink1 == 4:
        print("Type: Fruit Juice")
      elif drink1 == 0:
        print("Type: None")
    
      #display order 1 (main dish)
      print("") 
      print("--------- Order #1 ---------")
      print("")
      if main1 == 1:
        print("Main Dish: Chicken")
      elif main1 == 2:
        print("Main Dish: Pork")
      elif main1 == 3:
        print("Main Dish: Fish")
      elif main1 == 4:
        print("Main Dish: Beef")
      elif main1 == 0:
        print("Main Dish: None")
        
      #display order 1 (side dish)
      if side1 == 1:
        print("Side Dish: Steamed Rice")
      elif side1 == 2:
        print("Side Dish: Shredded Corn")
      elif side1 == 3:
        print("Side Dish: Mashed Potatoes")
      elif side1 == 4:
        print("Side Dish: Steam Vegetables")
      elif side1 == 0:
        print("Side Dish: None")
        
      #display order 1 (drinks)
      if drink1 == 1:
        print("Drinks: Mineral Water")
      elif drink1 == 2:
        print("Drinks: Iced Tea")
      elif drink1 == 3:
        print("Drinks: Soda")
      elif drink1 == 4:
        print("Drinks: Fruit Juice")
      elif drink1 == 0:
        print("Drinks: None")
       
      print("")
      print("----------------------------")
      print("") 

      #asking if the customer is the given order is correct
      nxt1 = str(input("Is this order correct? (y/n)"))
      while nxt1 != 'n' and nxt1 != 'y':
        nxt1 = str(input("Is this order correct? (y/n)"))
      if nxt1 == 'y':
        #if the order is correct, ask if the customer wants to go to the next order
        nxt2 = str(input("Would you like to proceed to the next order? (y/n)"))
        while nxt2 != 'n' and nxt2 != 'y':
          nxt2 = str(input("Would you like to proceed to the next order? (y/n)"))
        if nxt2 == 'n':
          nxt3 = 'y'
          nxt5 = 'y'
        if nxt2 == 'y':
          nxt3 = 'n'
          nxt5 = 'n'
      if nxt1 == 'n':
        print("")
        print("----------------------------")
        print("")
        print("Repeating your order....")

    #Order 2
    while nxt3 == 'n':
      print("")
      print("----------------------------")
      print("")
      print("Order #2: ")
      print("")
      
      #asking for main dish
      main2 = int(input("Main Dish: ID #"))
      while main2 < 0 or main2 > 4:
        print("")
        print("We don't have this dish in our menu! Please try again :)")
        print("")
        main2 = int(input("Main Dish: ID #"))
      if main2 == 1:
        print("Type: Chicken")
      elif main2 == 2:
        print("Type: Pork")
      elif main2 == 3:
        print("Type: Fish")
      elif main2 == 4:
        print("Type: Beef")
      elif main2 == 0:
        print("Type: None")
    
      #asking for side dish
      print("")
      side2 = int(input("Side Dish: ID #"))
      while side2 < 0 or side2 > 4:
        print("")
        print("We don't have this dish in our menu! Please try again :)")
        print("")
        side2 = int(input("Side Dish: ID #"))
      if side2 == 1:
        print("Type: Steamed Rice")
      elif side2 == 2:
        print("Type: Shredded Corn")
      elif side2 == 3:
        print("Type: Mashed Potatoes")
      elif side2 == 4:
        print("Type: Steam Vegetables")
      elif side2 == 0:
        print("Type: None")
    
      #asking for drinks
      print("")
      drink2 = int(input("Drink: ID #"))
      while drink2 < 0 or drink2 > 4:
        print("")
        print("We don't have this dish in our menu! Please try again :)")
        print("")
        drink2 = int(input("Drink: ID #"))
      if drink2 == 1:
        print("Type: Mineral Water")
      elif drink2 == 2:
        print("Type: Iced Tea")
      elif drink2 == 3:
        print("Type: Soda")
      elif drink2 == 4:
        print("Type: Fruit Juice")
      elif drink2 == 0:
        print("Type: None")
    
      #display order 2 (main dish)
      print("")
      print("--------- Order #2 ---------")
      print("") 
      if main2 == 1:
        print("Main Dish: Chicken")
      elif main2 == 2:
        print("Main Dish: Pork")
      elif main2 == 3:
        print("Main Dish: Fish")
      elif main2 == 4:
        print("Main Dish: Beef")
      elif main2 == 0:
        print("Main Dish: None")
        
      #display order 2 (side dish)
      if side2 == 1:
        print("Side Dish: Steamed Rice")
      elif side2 == 2:
        print("Side Dish: Shredded Corn")
      elif side2 == 3:
        print("Side Dish: Mashed Potatoes")
      elif side2 == 4:
        print("Side Dish: Steam Vegetables")
      elif side2 == 0:
        print("Side Dish: None")
        
      #display order 2 (drinks)
      if drink2 == 1:
        print("Drinks: Mineral Water")
      elif drink2 == 2:
        print("Drinks: Iced Tea")
      elif drink2 == 3:
        print("Drinks: Soda")
      elif drink2 == 4:
        print("Drinks: Fruit Juice")
      elif drink2 == 0:
        print("Drinks: None")
        print("") 
  
      print("")
      print("----------------------------")
      print("") 
      
      #asking if the customer is the given order is correct
      nxt3 = str(input("Is this order correct? (y/n)"))
      while nxt3 != 'n' and nxt3 != 'y':
        nxt3 = str(input("Is this order correct? (y/n)"))
      if nxt3 == 'y':
        #If the order is correct, ask if the customer wants to go to the next order
        nxt4 = str(input("Would you like to proceed to the next order? (y/n)"))
        while nxt4 != 'n' and nxt4 != 'y':
          nxt4 = str(input("Would you like to proceed to the next order? (y/n)"))
        if nxt4 == 'n':
          nxt5 = 'y'
          subtotal2 = 2 #Indicator that order 2 is made
        if nxt4 == 'y':
          subtotal2 = 2
          nxt5 = 'n'
      if nxt3 == 'n':
        nxt5 = 'y'
        print("")
        print("----------------------------")
        print("")
        print("Repeating your order....")
    
    #Order 3
    while nxt5 == 'n':
      print("")
      print("----------------------------")
      print("")
      print("Order #3: ")
      print("")
      
      #asking for main dish
      main3 = int(input("Main Dish: ID #"))
      while main3 < 0 or main3 > 4:
        print("")
        print("We don't have this dish in our menu! Please try again :)")
        print("")
        main3 = int(input("Main Dish: ID #"))
      if main3 == 1:
        print("Type: Chicken")
      elif main3 == 2:
        print("Type: Pork")
      elif main3 == 3:
        print("Type: Fish")
      elif main3 == 4:
        print("Type: Beef")
      elif main3 == 0:
        print("Type: None")
    
      #asking for side dish
      print("")
      side3 = int(input("Side Dish: ID #"))
      while side3 < 0 or side3 > 4:
        print("")
        print("We don't have this dish in our menu! Please try again :)")
        print("")
        side3 = int(input("Side Dish: ID #"))
      if side3 == 1:
        print("Type: Steamed Rice")
      elif side3 == 2:
        print("Type: Shredded Corn")
      elif side3 == 3:
        print("Type: Mashed Potatoes")
      elif side3 == 4:
        print("Type: Steam Vegetables")
      elif side3 == 0:
        print("Type: None")
        
      #asking for drinks
      print("")
      drink3 = int(input("Drink: ID #"))
      while drink3 < 0 or drink3 > 4:
        print("")
        print("We don't have this dish in our menu! Please try again :)")
        print("")
        drink3 = int(input("Drink: ID #"))
      if drink3 == 1:
        print("Type: Mineral Water")
      elif drink3 == 2:
        print("Type: Iced Tea")
      elif drink3 == 3:
        print("Type: Soda")
      elif drink3 == 4:
        print("Type: Fruit Juice")
      elif drink3 == 0:
        print("Type: None")
          
      #display order 3 (main dish)
      print("") 
      print("--------- Order #3 ---------")
      print("") 
      if main3 == 1:
        print("Main Dish: Chicken")
      elif main3 == 2:
        print("Main Dish: Pork")
      elif main3 == 3:
        print("Main Dish: Fish")
      elif main3 == 4:
        print("Main Dish: Beef")
      elif main3 == 0:
        print("Main Dish: None")
        
      #display order 3 (side dish)
      if side3 == 1:
        print("Side Dish: Steamed Rice")
      elif side3 == 2:
        print("Side Dish: Shredded Corn")
      elif side3 == 3:
        print("Side Dish: Mashed Potatoes")
      elif side3 == 4:
        print("Side Dish: Steam Vegetables")
      elif side3 == 0:
        print("Side Dish: None")
        
      #display order 3 (drinks)
      if drink3 == 1:
        print("Drinks: Mineral Water")
      elif drink3 == 2:
        print("Drinks: Iced Tea")
      elif drink3 == 3:
        print("Drinks: Soda")
      elif drink3 == 4:
        print("Drinks: Fruit Juice")
      elif drink3 == 0:
        print("Drinks: None")
      
      print("")
      print("----------------------------")
      print("") 
      
      #asking if the customer is the given order is correct
      nxt5 = str(input("Is this order correct? (y/n)"))
      while nxt5 != 'n' and nxt5 != 'y':
        nxt5 = str(input("Is this order correct? (y/n)"))
      if nxt5 == 'n':
        print("----------------------------")
        print("")
        print("Repeating your order...")
      if nxt5 == 'y':
        subtotal3 = 2

    #asking if the customer wants to cancel the order
    cancel = str(input("Would you want to cancel your order? (y/n)"))
    while cancel != 'n' and cancel != 'y':
      cancel = str(input("Would you want to cancel your order? (y/n)"))
    if cancel == 'y':
      print("")
      #Reset initial variables
      nxt1 = 'n'
      nxt3 = 'n'
      nxt5 = 'n'
      subtotal2 = 1
      subtotal3 = 1
  
  #Excluding an item
  excludeorder=0
  excludeitem=0
  
  #Asking if the customer wants to exclude something
  exclude = str(input("Exclude an item from the total? (y/n)"))
  while exclude != 'y' and exclude != 'n':
    exclude = str(input("Exclude an item from the total? (y/n)"))
    
  if exclude == 'y':
    print("")
    #Ask from which order would the customer like to exclude
    excludeorder = int(input("From which order?"))
    #Repeats the request when the customer didn't order such order numbers
    while excludeorder < 1 or excludeorder == 0:
      excludeorder = int(input("From which order?"))
    while excludeorder > 1 and subtotal2 == 1 and subtotal3 == 1:
      excludeorder = int(input("From which order?"))
    while excludeorder > 2 and subtotal3 == 1:
      excludeorder = int(input("From which order?"))
    while excludeorder > 3:
      excludeorder = int(input("From which order?"))
      
    #Ask for the item the customer like to exclude
    excludeitem = int(input("Which item will be excluded?"))
    while excludeitem == 0 or excludeitem < 1 or excludeitem > 3:
      excludeitem = int(input("Which item will be excluded?"))
      
    #excluding a main (order 1)
    if excludeorder == 1 and excludeitem == 1:
      if main1 == 1:
        print("Chicken will be excluded.")
      if main1 == 2:
        print("Pork will be excluded.")
      if main1 == 3:
        print("Fish will be excluded.")
      if main1 == 4:
        print("Beef will be excluded.")
        
    #excluding a main (order 2)
    if excludeorder == 2 and excludeitem == 1:
      if main2 == 1:
        print("Chicken will be excluded.")
      if main2 == 2:
        print("Pork will be excluded.")
      if main2 == 3:
        print("Fish will be excluded.")
      if main2 == 4:
        print("Beef will be excluded.")
        
    #excluding a main (order 3)
    if excludeorder == 3 and excludeitem == 1:
      if main3 == 1:
        print("Chicken will be excluded.")
      if main3 == 2:
        print("Pork will be excluded.")
      if main3 == 3:
        print("Fish will be excluded.")
      if main3 == 4:
        print("Beef will be excluded.")
        
    #excluding a side
    if excludeorder == 1 and excludeitem == 2:
      if side1 == 1:
        print("Steamed rice will be excluded.")
      if side1 == 2:
        print("Shredded corn will be excluded.")
      if side1 == 3:
        print("Mashed potatoes will be excluded.")
      if side1 == 4:
        print("Steam vegetables will be excluded.")
        
    #excluding a side (order 2)
    if excludeorder == 2 and excludeitem == 2:
      if side2 == 1:
        print("Steamed rice will be excluded.")
      if side2 == 2:
        print("Shredded corn will be excluded.")
      if side2 == 3:
        print("Mashed potatoes will be excluded.")
      if side2 == 4:
        print("Steam vegetables will be excluded.")
        
    #excluding a side (order 3)
    if excludeorder == 3 and excludeitem == 2:
      if side3 == 1:
        print("Steamed rice will be excluded.")
      if side3 == 2:
        print("Shredded corn will be excluded.")
      if side3 == 3:
        print("Mashed potatoes will be excluded.")
      if side3 == 4:
        print("Steam vegetables will be excluded.")
        
    #excluding a drink (order 1)
    if excludeorder == 1 and excludeitem == 3:
      if drink1 == 1:
        print("Mineral water will be excluded.")
      if drink1 == 2:
        print("Iced tea will be excluded.")
      if drink1 == 3:
        print("Soda will be excluded.")
      if drink1 == 4:
        print("Fruit juice will be excluded.")

    #excluding a drink (order 2)
    if excludeorder == 2 and excludeitem == 3:
      if drink2 == 1:
        print("Mineral water will be excluded.")
      if drink2 == 2:
        print("Iced tea will be excluded.")
      if drink2 == 3:
        print("Soda will be excluded.")
      if drink2 == 4:
        print("Fruit juice will be excluded.")

    #excluding a drink (order 3)
    if excludeorder == 3 and excludeitem == 3:
      if drink3 == 1:
        print("Mineral water will be excluded.")
      if drink3 == 2:
        print("Iced tea will be excluded.")
      if drink3 == 3:
        print("Soda will be excluded.")
      if drink3 == 4:
        print("Fruit juice will be excluded.")
  
  #Subtotals // RECEIPT
  subtotal22=0
  subtotal33=0
  
  print("")
  print("---------- RECEIPT ----------")
  print("")
  print("Order party of", num_people)
  print("")
  print("----------------------------")
  print("")
  
  #Displaying order 1
  print("Order #1:")
  print("")
  
  #Main Dish: Order 1
  if main1 == 0:
    print("Main Dish: None")
    main1 = 0.00
  elif main1 == 1: 
    if excludeorder == 1 and excludeitem == 1:
      print("Main Dish: Chicken - ₱ 0.00")
      main1 = 0.00
    else:
      print("Main Dish: Chicken - ₱ 90.00")
      main1 = 90.00
  elif main1 == 2:
    if excludeorder == 1 and excludeitem == 1:
      print("Main Dish: Pork - ₱ 0.00")
      main1 = 0.00
    else:
      print("Main Dish: Pork - ₱ 105.00")
      main1 = 105.00
  elif main1 == 3:
    if excludeorder == 1 and excludeitem == 1:
      print("Main Dish: Fish - ₱ 00.00")
      main1 = 0.00
    else:
      print("Main Dish: Fish - ₱ 120.00")
      main1 = 120.00
  elif main1 == 4:
    if excludeorder == 1 and excludeitem == 1:
      print("Main Dish: Beef - ₱ 00.00")
      main1 = 0.00
    else:
      print("Main Dish: Beef - ₱ 135.00")
      main1 = 135.00

  #Side Dish: Order 1
  if side1 == 0:
    print("Side Dish: None")
    side1 = 0.00      
  elif side1 == 1:
    if excludeorder == 1 and excludeitem == 2:
      print("Side Dish: Steamed Rice - ₱ 00.00")
      side1 = 0.00
    else: 
      print("Side Dish: Steamed Rice - ₱ 20.00")
      side1 = 20.00
  elif side1 == 2:
    if excludeorder == 1 and excludeitem == 2:
      print("Side Dish: Shredded Corn - ₱ 00.00")
      side1 = 0.00
    else: 
      print("Side Dish: Shredded Corn - ₱ 35.00")
      side1 = 35.00
  elif side1 == 3:
    if excludeorder == 1 and excludeitem == 2:
      print("Side Dish: Mashed Potatoes - ₱ 00.00")
      side1 = 0.00
    else: 
      print("Side Dish: Mashed Potatoes - ₱ 50.00")
      side1 = 50.00
  elif side1 == 4:
    if excludeorder == 1 and excludeitem == 2:
      print("Side Dish: Steam Vegetables - ₱ 00.00")
      side1 = 0.00
    else: 
      print("Side Dish: Steam Vegetables - ₱ 65.00")
      side1 = 65.00

  #Drinks: Order 1
  if drink1 == 0:
    print("Drinks: None")
    drink1 = 0.00 
  elif drink1 == 1:
    if excludeorder == 1 and excludeitem == 3:
      print("Drink: Mineral Water - ₱ 00.00")
      drink1 = 0.00
    else: 
      print("Type: Mineral Water - ₱ 25.00")
      drink1 = 25.00
  elif drink1 == 2:
    if excludeorder == 1 and excludeitem == 3:
      print("Drink: Iced Tea - ₱ 00.00")
      drink1 = 0.00
    else: 
      print("Type: Iced Tea - ₱ 35.00")
      drink1 = 35.00
  elif drink1 == 3:
    if excludeorder == 1 and excludeitem == 3:
      print("Drink: Soda - ₱ 00.00")
      drink1 = 0.00
    else:
      print("Type: Soda - ₱ 45.00")
      drink1 = 45.00
  elif drink1 == 4:
    if excludeorder == 1 and excludeitem == 3:
      print("Drink: Fruit Juice - ₱ 00.00")
      drink1 = 0.00
    else:
      print("Type: Fruit Juice - ₱ 55.00")
      drink1 = 55.00
  
  subtotal1 = main1+side1+drink1
  print("Subtotal: ₱",subtotal1)

  #Displaying order 2 (Only when the customer ordered an order 2)
  if subtotal2 == 2:
    print("")
    print("Order #2")
    print("")
    
    #Main Dish: Order 2
    if main2 == 0:
      print("Main Dish: None")
      main2 = 0.00 
    elif main2 == 1:
      if excludeorder == 2 and excludeitem == 1:
        print("Main Dish: Chicken - ₱ 0.00")
        main2 = 0.00
      else:
        print("Main Dish: Chicken - ₱ 90.00")
        main2 = 90.00
    elif main2 == 2:
      if excludeorder == 2 and excludeitem == 1:
        print("Main Dish: Pork - ₱ 0.00")
        main2 = 0.00
      else:
        print("Main Dish: Pork - ₱ 105.00")
        main2 = 105.00
    elif main2 == 3:
      if excludeorder == 2 and excludeitem == 1:
        print("Main Dish: Fish - ₱ 00.00")
        main2 = 0.00
      else:
        print("Main Dish: Fish - ₱ 120.00")
        main2 = 120.00
    elif main2 == 4:
      if excludeorder == 2 and excludeitem == 1:
        print("Main Dish: Beef - ₱ 00.00")
        main2 = 0.00
      else:
        print("Main Dish: Beef - ₱ 135.00")
        main2 = 135.00

    #Side Dish: Order 2
    if side2 == 0:
      print("Side Dish: None")
      side2 = 0.00 
    elif side2 == 1:
      if excludeorder == 2 and excludeitem == 2:
        print("Side Dish: Steamed Rice - ₱ 00.00")
        side2 = 0.00
      else: 
        print("Side Dish: Steamed Rice - ₱ 20.00")
        side2 = 20.00
    elif side2 == 2:
      if excludeorder == 2 and excludeitem == 2:
        print("Side Dish: Shredded Corn - ₱ 00.00")
        side2 = 0.00
      else: 
        print("Side Dish: Shredded Corn - ₱ 35.00")
        side2 = 35.00
    elif side2 == 3:
      if excludeorder == 2 and excludeitem == 2:
        print("Side Dish: Mashed Potatoes - ₱ 00.00")
        side2 = 0.00
      else: 
        print("Side Dish: Mashed Potatoes - ₱ 50.00")
        side2 = 50.00
    elif side2 == 4:
      if excludeorder == 2 and excludeitem == 2:
        print("Side Dish: Steam Vegetables - ₱ 00.00 ")
        side2 = 0.00
      else: 
        print("Side Dish: Steam Vegetables - ₱ 65.00")
        side2 = 65.00
        
    #Drinks: Order 2
    if drink2 == 0:
      print("Side Dish: None")
      drink2 = 0.00
    elif drink2 == 1:
      if excludeorder == 2 and excludeitem == 3:
        print("Drink: Mineral Water - ₱ 00.00")
        drink2 = 0.00
      else: 
        print("Type: Mineral Water - ₱ 25.00")
        drink2 = 25.00
    elif drink2 == 2:
      if excludeorder == 2 and excludeitem == 3:
        print("Drink: Iced Tea - ₱ 00.00")
        drink2 = 0.00
      else: 
        print("Type: Iced Tea - ₱ 35.00")
        drink2 = 35.00
    elif drink2 == 3:
      if excludeorder == 2 and excludeitem == 3:
        print("Drink: Soda - ₱ 00.00")
        drink2 = 0.00
      else:
        print("Type: Soda - ₱ 45.00")
        drink2 = 45.00
    elif drink2== 4:
      if excludeorder == 2 and excludeitem == 3:
        print("Drink: Fruit Juice - ₱ 00.00")
        drink2 = 0.00
      else:
        print("Type: Fruit Juice - ₱ 55.00")
        drink2 = 55.00
        
    subtotal22 = main2+side2+drink2
    print("Subtotal: ₱",subtotal22)

  #Displaying order 3 (Only when the customer ordered an order 3)
  if subtotal3 == 2:
    print("")
    print("Order #3")
    print("")

    #Main Dish: Order 3
    if main3 == 0:
      print("Main Dish: None")
      main3 = 0.00
    elif main3 == 1:
      if excludeorder == 3 and excludeitem == 1:
        print("Main Dish: Chicken - ₱ 0.00 ")
        main3 = 0.00
      else:
        print("Main Dish: Chicken - ₱ 90.00")
        main3 = 90.00
    elif main3 == 2:
      if excludeorder == 3 and excludeitem == 1:
        print("Main Dish: Pork - ₱ 0.00")
        main3 = 0.00
      else:
        print("Main Dish: Pork - ₱ 105.00")
        main1 = 105.00
    elif main3 == 3:
      if excludeorder == 3 and excludeitem == 1:
        print("Main Dish: Fish - ₱ 00.00")
        main3 = 0.00
      else:
        print("Main Dish: Fish - ₱ 120.00")
        main3 = 120.00
    elif main3 == 4:
      if excludeorder == 3 and excludeitem == 1:
        print("Main Dish: Beef - ₱ 00.00")
        main3 = 0.00
      else:
        print("Main Dish: Beef - ₱ 135.00")
        main3 = 135.00

    #Side Dish: Order 3
    if side3 == 0:
      print("Side Dish: None")
      side3 = 0.00 
    elif side3 == 1:
      if excludeorder == 3 and excludeitem == 2:
        print("Side Dish: Steamed Rice - ₱ 00.00")
        side3 = 0.00
      else: 
        print("Side Dish: Steamed Rice - ₱ 20.00")
        side3 = 20.00
    elif side3 == 2:
      if excludeorder == 3 and excludeitem == 2:
        print("Side Dish: Shredded Corn - ₱ 00.00")
        side3 = 0.00
      else: 
        print("Side Dish: Shredded Corn - ₱ 35.00")
        side3 = 35.00
    elif side3 == 3:
      if excludeorder == 1 and excludeitem == 2:
        print("Side Dish: Mashed Potatoes - ₱ 00.00")
        side3 = 0.00
      else: 
        print("Side Dish: Mashed Potatoes - ₱ 50.00")
        side3 = 50.00
    elif side3 == 4:
      if excludeorder == 3 and excludeitem == 2:
        print("Side Dish: Steam Vegetables - ₱ 00.00")
        side3 = 0.00
      else: 
        print("Side Dish: Steam Vegetables - ₱ 65.00")
        side3 = 65.00

    #Drinks: Order 3
    if drink3 == 0:
      print("Drinks: None")
      drink3 = 0.00 
    elif drink3 == 1:
      if excludeorder == 3 and excludeitem == 3:
        print("Drink: Mineral Water - ₱ 00.00")
        drink3 = 0.00
      else: 
        print("Type: Mineral Water - ₱ 25.00")
        drink3 = 25.00
    elif drink3 == 2:
      if excludeorder == 3 and excludeitem == 3:
        print("Drink: Iced Tea - ₱ 00.00")
        drink1 = 0.00
      else: 
        print("Type: Iced Tea - ₱ 35.00")
        drink3 = 35.00
    elif drink3 == 3:
      if excludeorder == 3 and excludeitem == 3:
        print("Drink: Soda - ₱ 00.00")
        drink1 = 0.00
      else:
        print("Type: Soda - ₱ 45.00")
        drink3 = 45.00
    elif drink3 == 4:
      if excludeorder == 3 and excludeitem == 3:
        print("Drink: Fruit Juice - ₱ 00.00")
        drink3 = 0.00
      else:
        print("Type: Fruit Juice - ₱ 55.00")
        drink3 = 55.00
  
    subtotal33=main3+side3+drink3
    print("Subtotal: ₱",subtotal33)
  
  #Total Amount Due
  totalamount = subtotal1+subtotal22+subtotal33
  print("")
  print("----------------------------")
  print("")
  print("Total Amount Due: ₱", totalamount) 
  
  #Division of payment
  div = totalamount/num_people
  print("")
  print("Each person must pay: ₱ %.2f" % div)
  print("")
  print("----------------------------")  

#Modified: <3/20/2023>
#Modified: <3/24/2023>
#Modified: <3/25/2023>
#Modified: <3/27/2023>
#Modified: <4/3/2023>
#Modified: <4/5/2023>
#Modified: <4/6/2023>
    
#Description: <Describe what this program does briefly>
#Programmed by: Cao, Jingwen and Garcia, Czarina
#Last modified: <4/6/2023>
#Version: 5.2
#Acknowledgements: <https://docs.python.org/3/tutorial/>
