place = {
    'comilla': ['kandirpar', 'lhawtola', 'sadar'],
    'noakhali': ['maijdee', 'sonapur', 'chowrasta'],
    'dhaka': ['dhanmondi', 'mohammodpur', 'gulshan', 'moakhali']
}

for pla, citys in place.items():
    print(f"\nCity in {pla.title()} are: ")
   # print(f"->{citys}")

    for city in citys:
        print(f"->{city.title()}")
