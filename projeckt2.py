day = input("Enter your birthday (in number format from 1 to 31): ")
month = input("Enter month of birth (in number format from 1 to 12): ")
month = int(month)
day = int(day)

if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    sign = "Aries"
    print('You are an Aries Aries')
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    sign = "Taurus"
    print('Your sign is Taurus!')
elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
    sign = "Gemini"
    print('Your sign is Taurus Gemini!')
elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
    sign = "Cancer"
    print('Your sign is  Cancer')
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    sign = "Leo"
    print('You are a Leo!')
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    sign = "Virgo"
    print('You are a  Virgo')
elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
    sign = "Libra"
    print('Your sign is Libra!')
elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
    sign = "Scorpio"
    print('Your sign is Scorpio')
elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
    sign = "Saggitarius"
    print('Your sign is Saggitarius')
elif (month == 12 and day >= 22) or (month == 1 and day <= 20):
    sign = "Capricorn"
    print('Your sign is Capricorn')
elif (month == 1 and day >= 21) or (month == 2 and day <= 18):
    sign = "Aquarius"
    print('Your sign is Aquarius!')