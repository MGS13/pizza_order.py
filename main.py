print("🅡 🅞 🅜 🅘 🅝 🅞 '🅢  🅟 🅘 🅩 🅩 🅐")
#You're on your own from there!
price=0

while(True):
  p_type=input("Please enter your pizza type: thin, italian, pan ").lower()
  if (p_type=="exit"):
    print("I hope to see you soon")
    exit()
  size=input("Please enter your size: small, medium, large  ").lower()
  if (size=="exit"):
    print("I hope to see you soon")
    exit()
  speed=input("Please enter the speed of your order: rush or standard: ").lower()
  if (speed=="exit"):
    print("I hope to see you soon")
    exit()
  dropoff=input("is your order delivery or collection?: ").lower()
  if (dropoff=="exit"):
    print("I hope to see you soon")
    exit()
  
  #these if statements will select prices based off pizza type and a nested loop will give accurate prices based off the size
  if p_type=="thin":
    if size=="small":
      price=4.99
    elif size=="medium":
      price=7.99
    elif size=="large":
      price=10.99
    if p_type=="thin" and "small":
      print("this works")
  if p_type=="italian":
    if size=="small":
      price=5.49
    elif size=="medium":
      price=8.99
    elif size=="large":
      price=12.49
    
  if p_type=="pan":
    if size=="small":
      price=5.99
    elif size=="medium":
      price=9.99
    elif size=="large":
      price=13.99
    #these if statements will select prices for rush or standard and then will add and set the prices based on any extra charges.
  if speed=="rush":
    if dropoff=="delivery":
      price+=3.99
    if dropoff=="collection":
      price+=1.99
  if speed=="standard":
    if dropoff=="delivery":
      price+=0.99
    if dropoff=="standard":
      price+=0
  print("Your total is:$",str(price))

