"""reports.py"""
from calculations import *


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


