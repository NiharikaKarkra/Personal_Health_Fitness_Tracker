"""reports.py"""
from calculations import *


#display summary
def display_summary(steps_list, weight_list, bmi, category):

    print("\n" + "="*40)
    print("         HEALTH SUMMARY")
    print("="*40)

    print(f"Highest Steps      : {highest_value(steps_list)}")
    print(f"Lowest Steps       : {lowest_value(steps_list)}")
    print(f"Average Steps      : {calculate_weekly_average(steps_list)}")

    print()

    print(f"Highest Weight     : {highest_value(weight_list)} kg")
    print(f"Lowest Weight      : {lowest_value(weight_list)} kg")
    print(f"Average Weight     : {calculate_weekly_average(weight_list)} kg")

    print()

    print(f"Current BMI        : {bmi}")
    print(f"BMI Category       : {category}")

    print("="*40)

#display heath analysis
def display_analysis(weight, steps, height, age, gender):
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    calories = calculate_calories(weight,height,age,gender)
    water = calculate_water_requirement(weight)
    fitness = get_fitness_category(steps)

    print("\n" + "=" * 40)
    print("Today's Health Analysis")
    print("="*40)
    print(f"BMI  :  {bmi}")
    print(f"BMI Category  =  {category}")
    print(f"Calories Required  :  {calories}")
    print(f"Ideal Water Intake  :  {water}")
    print(f"Fitness Category  :  {fitness}")
    print("\n" + "=" * 40)


