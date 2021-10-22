city=input("Enter city name:")
l=['hyderabad','chennai','delhi','mumbai']
if city.strip() in l:
    print("Your customer care call starts with +91")
else:
    print("Please enter valid city")