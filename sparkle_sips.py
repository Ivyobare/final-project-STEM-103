

def legal_age():   
        try:
          age = int(input("Please enter your age: "))
          if age >= 21:
            print("You are old enough. ")
          else:
               print("You are not old enough to drink")
               exit()
        except ValueError:
            print("Invalid input.Please enter a number.")


def num_ofpeople():
  total_people = int(input("How many people are under this order:"))
  if total_people > 5:
    print("Maximum number of people per order is 5. Add another account ")  
    exit()
  else:
    print("Proceed to  Order list")


def menu_drinks(user_name):
   print(f"Hello {user_name}, here is a list of drinks and  cocktails  we have." )
   list =  {
           1: {"drink":"Oldfashioned" , "price": 8.50} ,
           2: {"drink":"Martini" ,"price":7.25}  , 
           3: {"drink":"Manhattan","price":  9.00} ,
           4: {"drink":"?Whiskey Sour", "price": 8.95} , 
           5: {"drink":"Bloody Mary","price": 11.00} ,
           6: {"drink":"Moscow Mule","price":  10.55} ,
           7: {"drink":"French 75","price":  9.85} 
           
   }
   return list

def place_order(drinks):
   print("\Menu:")
   for i, drink in enumerate(drinks):
      print(f"{i +1 }.{drink['name']}- ${drink['price']}")

  
    while True:
     try:
          choice = input("Enter the number of choice of drink you want: (and 'X' TO EXIT): ")

          if choice == 'X':
              print("Exiting order")

          choice = int(choice) - 1
          if 0 <= choice < len(drinks):
           num_drinks = int(input("Enter the number of {drinks[choice]['name']}"))
           order_total  =drinks[choice]['price']  * num_drinks
           print("You  have ordered {num_drinks}{drinks[choice]['name']}")
          print("Total cost:{order_total:2f}")
     except ValueError:
        print("invalid input")
        
    
      
                 


   

       
