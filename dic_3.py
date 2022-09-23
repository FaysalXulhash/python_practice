mnb = {
    'Name': 'Faisal',
    'Age': '24',
    'Roll': 'ASh1825015M'
}

for k, v in mnb.items():
    print(f"\nkey: {k}")
    print(f"Value: {v}")


fav_lan = {
    'faisal': 'python',
    'rahat': 'php',
    'priyo': 'ruby',
    'sourav': 'js',
    'gorila': 'react'
}

for name , language in fav_lan.items():
    print(f"{name.title()}' s favourite language is {language} ")
