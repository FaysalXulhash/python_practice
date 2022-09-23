phone = input("Enter digit ")

digit_map = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
}
output = ""
for ch in phone:
    output += digit_map.get(ch, "!") + " "

print(output)
