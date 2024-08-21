name = str(input("Please inter your name: ")) #str input space for name
prompt = ''' 
*** Please select one option ***\n
1. option one
2. option 2
3. option three
>>>
'''


product = int(input(prompt)) # intiger input space

location_category = '''
*** Choose a location ***\n
1. Ethiopia
2. USA
3. Kenya
4. UK

'''
location = int(input(location_category))

print(f"name : {name}")
print(f'chosen product number: {product}')
print(f"location: {location}")


if product == 1:
    if location == 1:
        discount = 20
    elif location == 2:
        discount = 5
    elif location == 3:
        dicount = 10
    else:
        discount = None
elif product == 2:
        if location == 1:
              discount = 20
        elif location == 2:
            discount = 5
        elif location == 3:
            dicount = 10
        else:
            discount = None
else:
    if location == 1:
        discount = 20
    elif location == 2:
        discount = 5
    elif location == 3:
        dicount = 10
    else:
        discount = None