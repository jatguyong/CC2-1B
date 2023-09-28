POUNDS_TO_KG = 0.45359237 
pounds = float(input("Weight in Pounds (lbs): "))
converted_pounds = pounds * POUNDS_TO_KG
print("Weight converted to Kilograms (kg): ", round(converted_pounds, 2), "kg")

print("=============================================================")

LENGTH_TO_MILES = 1.609344
length = float(input("Length in Miles (mi): "))
converted_length = length * LENGTH_TO_MILES
print("Length in Kilometers (km): ", round(converted_length, 2), "km")

print("=============================================================")

fahrenheit = float(input("Temperature in Fahrenheit (°F): "))
converted_fahrenheit = ((fahrenheit-32) * 5)/9
print("Temperature in Celsius (°C): ", round(converted_fahrenheit, 2), "°C")

print("=============================================================")

average_of_students = 0

for i in range(1, 11):
    student = int(input(f"Age of Student {i}: "))
    average_of_students += student

print("The average age of the students is: ", average_of_students/10)

print("=============================================================")

char1 = "Xie Lian"
char2 = "Hanguang-Jun"
char3 = "Yling Patriarch"
char4 = "Hua Cheng"
char5 = "Luo Binghe"

ability = "spiritual blast"
equipment = "Chenqing"
item = "Yin Tiger Tally"


story = (f"""{char1}, the exiled heaven official and former prince of XianLe, encountered {char2}, a peculiar cultivator searching for someone dear. 
That person turned out to be the now-villain, {char3}, whose arrival had disrupted the celestial balance as he soared with his spirit-calling flute, {equipment}. 
Together, they aimed to uncover the truth behind the Patriarch's change in attitude. In a climactic battle, {char1} was forced to use his hidden power, 
the {ability}, but was gravely wounded by malevolent spirits. {char4}, the Ghost King, joined to avenge his beloved friend and revealed that the 
{char3} was controlled by the {item}. After vindicating the {char3}, they destroyed the tally…or so they thought. 
As the battle ended, {char5} collected the item and soon realized it wasn’t wholly destroyed. Pondering its fate, he chose to keep it for now.""") 

print(story)