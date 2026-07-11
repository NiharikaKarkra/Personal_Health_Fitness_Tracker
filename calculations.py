"""calculations.py"""

#calculate bmi
def calculate_bmi(weight,height):
    h=height/100
    return round(weight/(h*h),2)
    
# BMI category check
def get_bmi_category(bmi):
    return "Underweight" if bmi<18.5 else "Normal" if bmi<25 else "Overweight" if bmi<30 else "Obese"

# Calculate water requirements
def calculate_water_requirement(weight): return round(weight*0.035,2)

#calculate calories intake
def calculate_calories(weight,height,age,gender):
    if gender.lower()=="male":
        return round(10*weight+6.25*height-5*age+5)
    return round(10*weight+6.25*height-5*age-161)

# fitness category check
def get_fitness_category(steps):
    if steps<3000:return "Sedentary"
    if steps<7000:return "Lightly Active"
    if steps<10000:return "Moderately Active"
    return "Highly Active"
    
#sleep quality
def get_sleep_quality(hours):
    if hours<6:return "Poor"
    if hours<=9:return "Good"
    return "Oversleep"
    

def calculate_weekly_average(values): return round(sum(values)/len(values),2) if values else 0
def highest_value(values): return max(values) if values else None
def lowest_value(values): return min(values) if values else None
def is_valid_age(v): return str(v).isdigit() and 5<=int(v)<=120

# VALIDATIONS

def is_valid_weight(weight):
    try:
        weight = float(weight)
        return 20 <= weight <= 300
    except ValueError:
        return False


def is_valid_steps(steps):
    try:
        steps = int(steps)
        return 0 <= steps <= 100000
    except ValueError:
        return False


def is_valid_water(water):
    try:
        water = float(water)
        return 0 <= water <= 10
    except ValueError:
        return False


def is_valid_sleep(sleep):
    try:
        sleep = float(sleep)
        return 0 <= sleep <= 24
    except ValueError:
        return False
