def design(a) :
   de1 = "=" * 9
   de2 = "=" * 9
   return de1 + a + de2
    
result = design("Table")
print(result)
 
  
print("A1", "A2", "A3", "A4")
print("B1", "B2", "B3", "B4")
print("C1", "C2", "C3", "C4")
Table = input("Select table: ")

print (design("Table"))
answer = "yes"
order = [ ]
total_order = 0

while answer == "yes" :

 print (design("Menu"))
 print("1. Coffees")
 print("2. Drinks")
 print("3. Brunch")
 print("4. Lunch")
 categorie = int(input("Choose the categorie according the number: "))
 print(design("Menu"))

 if  categorie == 1 :
  result = design("Coffees")
  print (result)
  print ("1. Cappucino")
  print ("2. Espresso")
  choise_Co = int(input("Add coffee (with number) : "))
  quantity_co= int(input("Add quantity: "))

  if choise_Co == 1 : 
   print(f"{quantity_co} Cappucino")
   cappucino_price = 3.00
   total_order += cappucino_price * quantity_co
   order.append(f"{quantity_co} Cappucino -  {cappucino_price * quantity_co:.2f} €")
      
  elif choise_Co == 2:
   print (f"{quantity_co} Espresso")
   espresso_price = 2.50
   total_order += espresso_price * quantity_co
   order.append(f"{quantity_co} Espresso -  {espresso_price * quantity_co: .2f} €")

 elif categorie == 2 :
  result = design("Drinks")
  print(result)

  print("1. Apple Juice")
  print("2. Orange juice")
  print("3. Chocolate Drink")
  print("4. Tea")
  print("5. Soft Drinks")
  choice_dri = int(input("Add drink (with number): "))
  quantity_dri = int(input("Add quantity:"))

  if choice_dri == 1 :
    print(f"{quantity_dri} Apple Juices")
    applej_pri = 3.00
    total_order += applej_pri * quantity_dri
    order.append(f"{quantity_dri} Apple Juice -  {applej_pri * quantity_dri:.2f} €")

  elif choice_dri == 2 :
   print(f"{quantity_dri} Orange Juices")
   orangej_pri = 3.00
   total_order += orangej_pri * quantity_dri
   order.append(f"{quantity_dri} Orange Juice -  {orangej_pri * quantity_dri:.2f} €")

  elif choice_dri == 3 :
   print(f"{quantity_dri} Chocolate Drinks")
   choco_price = 4.00
   total_order += choco_price * quantity_dri
   order.append(f"{quantity_dri} Chocolate Drink -  {choco_price * quantity_dri:.2f} €")

  elif choice_dri == 4 :
   print("Black Tea")
   print("Green Tea")
   print("Ginger Tea")
   print("Ginger Lime")
   flavour = input("Add tea flavour(write): ").lower()
   print(f"{quantity_dri} {flavour}")
   flavour_pri = 2.50
   total_order += flavour_pri * quantity_dri
   order.append(f"{quantity_dri} {flavour} -  {flavour_pri * quantity_dri:.2f} €")

  elif choice_dri == "Soft Drinks" :
      
   print("1. Coca cola")
   print("2. Pepsi")
   print("3. Sprite")
   print("4. Lemonade")
   kind = input("Add soft drink(write): ").lower()
   print(f"{quantity_dri} {kind}")
   kind_pri = 4.00
   total_order += kind_pri * quantity_dri
   order.append(f"{quantity_dri} {kind} -  {kind_pri * quantity_dri:.2f} €")

 elif categorie == 3 :
   result = design("Brunch")
   print(result)

   print("1. Egg Omelete")
   print("2. sweet Pancakes (chocolate praline, biscuit and strawberries)")
   print("3. Salty pancakes (with cheese , creamcheese, Bacon and tomato)")
   print("4. fruitsalad (with banana, strawberries, blueberries and apple)")
   choice_bru = int(input("Add Brunch (with number): "))
   quantity_bru = int(input("Add quantity: "))

   if choice_bru == 1:
    print(f"{quantity_bru} Egg Omelete")
    eggom_pri = 6.00
    total_order += eggom_pri * quantity_bru
    order.append(f'{quantity_bru} Egg Omelete -  {eggom_pri * quantity_bru:.2f} €')

   elif choice_bru == 2 :
    print(f"{quantity_bru} Sweet Pancakes")
    swepan_pri = 9.00
    total_order += swepan_pri * quantity_bru
    order.append(f"{quantity_bru} Sweet Pancakes - {swepan_pri * quantity_bru:.2f} €")

   elif choice_bru ==  3 :
    print (f"{quantity_bru} salty pancakes")
    saltpan_pri = 10.00
    total_order += saltpan_pri * quantity_bru
    order.append(f"{quantity_bru} Salty Pancakes -  {saltpan_pri * quantity_bru:.2f} €")

   elif choice_bru == 4 :
    print (f"{quantity_bru} Fruitsalad")
    fruitsa_pri = 7.00
    total_order += fruitsa_pri * quantity_bru
    order.append(f"{quantity_bru} Fruitsalad -  {fruitsa_pri * quantity_bru:2f} €")

 elif categorie == 4 :
  result = design("Lunch")
  print(result)

  print ("1. Pizza Margarita (only Cheese)")
  print ("2. Pizza peperone (cheese and peperone)")
  print ("3. Smushed Burger (Beef, Onions, cheese, bbq sauce and potatoes)")
  print ("4. Chicken wrap (lettuce, chicken, mustard sauce, wrap and potatoes)")
  choice_lunch = int(input("Add Lunch(with number): "))
  quantity_lunch = int(input("Add Quantity: "))
    
  if choice_lunch == 1 :
    print(f"{quantity_lunch} pizza margarita")
    pizzama_pri = 12.00
    total_order += pizzama_pri * quantity_lunch
    order.append(f"{quantity_lunch} Pizza Margarita -  {pizzama_pri * quantity_lunch:.2f} €")
 
  elif choice_lunch == 2 :
   print(f"{quantity_lunch} Pizza Peperone")
   pizzape_pri = 14.00
   total_order += pizzape_pri * quantity_lunch
   order.append(f"{quantity_lunch} Pizza Peperone -  {pizzape_pri * quantity_lunch:.2f} €")
    
  elif choice_lunch == 3 :
   print(f"{quantity_lunch} Smushed Burger")
   burger_pri = 9.00
   total_order += burger_pri * quantity_lunch
   order.append(f"{quantity_lunch} Smushed Burger -  {burger_pri * quantity_lunch:.2f} €")

  elif choice_lunch == 4 :
   print(f"{quantity_lunch} Chicken Wrap")
   chickenwra_pri = 8.00
   total_order += chickenwra_pri * quantity_lunch
   order.append(f"{quantity_lunch} Chicken Wrap -  {chickenwra_pri * quantity_lunch:.2f} €")

 answer = input("Add anything else?: ").lower()


result=design("RECEIPT")
print(result)

import random
numbers = random.randint(1, 20)
print (f"ORDER NO {numbers}")
print (f"Table = {Table}")

line = ("-" * 19)
print(line)
    

for item in order :
   print(item)

print(line)


print (f"TOTAL: {total_order:.2f} €")
       

  
   


            
           


   


      
      



