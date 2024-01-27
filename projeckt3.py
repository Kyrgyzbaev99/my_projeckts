day1 = 'Monday'
day2 = 'Tuesday'
day3 = 'Wednwsday'
day4 = 'Thursday'
day5 = 'Friday'
day6 = 'Saturday'
day7 = 'Sonnday'

all_days = 7
days = (day1, day2, day3, day4, day5, day6, day7)
expenses_summe1 = float(input(f" Enter your expenses for Monday {day1}"))
expenses_summe2 = float(input(f" Enter your expenses for Tuesday {day2}"))
expenses_summe3 = float(input(f" Enter your expenses for Wednesday  {day3}"))
expenses_summe4 = float(input(f" Enter your expenses for Thurssday {day4}"))
expenses_summe5 = float(input(f" Enter your expenses for Friday {day5}"))
expenses_summe6 = float(input(f" Enter your expenses for Saturday {day6}"))
expenses_summe7 = float(input(f" Enter your expenses for Sonnday {day7}"))


avarege_exspense = round(expenses_summe1 + expenses_summe2 + expenses_summe3 + expenses_summe4 + expenses_summe5 +
                         expenses_summe6 + expenses_summe7 / all_days,1)
print(f"Ваш средний расходы в день :{avarege_exspense}")
