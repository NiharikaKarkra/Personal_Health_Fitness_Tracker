"""reports.py"""
from calculations import *

# def display_daily_report(d):
#     print("="*40)
#     for k,v in d.items(): print(f"{k.replace('_',' ').title():20}: {v}")
#     print("="*40)

# def display_weekly_summary(d): display_daily_report(d)

# def display_bmi_history(h):
#     print("BMI HISTORY")
#     for k,v in h.items(): print(k,v)

# def display_weight_history(h):
#     print("WEIGHT HISTORY")
#     for k,v in h.items(): print(k,v)

# def display_health_tips(data):
#     tips=[]
#     bmi=data.get("bmi",0)
#     if bmi<18.5: tips.append("Increase nutritious calorie intake.")
#     elif bmi>=25: tips.append("Exercise regularly and maintain a balanced diet.")
#     if data.get("steps",0)<7000: tips.append("Walk more every day.")
#     if data.get("sleep_hours",7)<7: tips.append("Aim for 7-9 hours of sleep.")
#     if not tips: tips=["Great job! Keep maintaining your routine."]
#     print("\n".join(tips))


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


