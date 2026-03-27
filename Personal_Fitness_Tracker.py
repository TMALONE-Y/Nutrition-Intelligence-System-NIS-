def clear_screen():
   
    print("=" * 50)

def get_user_info():
    
    print("\n" + "="*50)
    print("        NUTRITION CALCULATOR PROGRAM")
    print("="*50)
    
   
    name = input("\n Enter your name: ").strip()
    while name == "":
        name = input(" Please enter a valid name: ").strip()
    
    
    while True:
        try:
            age = int(input(" Enter your age (years): "))
            if age > 0 and age < 120:
                break
            else:
                print(" Please enter age between 1 and 120")
        except ValueError:
            print(" Please enter a valid number")
    
    
    while True:
        try:
            height = float(input(" Enter your height (cm): "))
            if height > 50 and height < 300:
                break
            else:
                print(" Please enter height between 50 and 300 cm")
        except ValueError:
            print(" Please enter a valid number")
    
    
    while True:
        try:
            weight = float(input(" Enter your weight (kg): "))
            if weight > 20 and weight < 500:
                break
            else:
                print(" Please enter weight between 20 and 500 kg")
        except ValueError:
            print(" Please enter a valid number")
    
    return name, age, height, weight

def calculate_bmr(weight, height, age):
    
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    return bmr

def calculate_maintenance_calories(bmr, activity_level):
    
    if activity_level == 1:
        multiplier = 1.2 
    elif activity_level == 2:
        multiplier = 1.375  
    elif activity_level == 3:
        multiplier = 1.55 
    elif activity_level == 4:
        multiplier = 1.725  
    else:
        multiplier = 1.9  
    
    return bmr * multiplier

def choose_goal():
    

    print("\n" + "-"*40)
    print(" CHOOSE YOUR GOAL:")
    print("   [1]  MUSCLE BUILDING (Bulking)")
    print("   [2]  CUTTING (Fat loss with muscle preservation)")
    print("-"*40)
    
    while True:
        try:
            choice = int(input(" Enter your choice (1 or 2): "))
            if choice == 1 or choice == 2:
                return choice
            else:
                print(" Please enter 1 or 2")
        except ValueError:
            print(" Please enter a valid number")

def choose_activity_level():
    
    print("\n" + "-"*40)
    print(" DAILY ACTIVITY LEVEL:")
    print("   [1] Sedentary (office job, no exercise)")
    print("   [2] Light activity (exercise 1-3 days/week)")
    print("   [3] Moderate activity (exercise 3-5 days/week)")
    print("   [4] Very active (exercise 6-7 days/week)")
    print("   [5] Extra active (athlete, twice daily)")
    print("-"*40)
    
    while True:
        try:
            choice = int(input(" Enter activity level (1-5): "))
            if choice >= 1 and choice <= 5:
                return choice
            else:
                print(" Please enter number between 1 and 5")
        except ValueError:
            print(" Please enter a valid number")

def calculate_nutrition(weight, maintenance_calories, goal):
   
    
    if goal == 1:  
        calories = maintenance_calories + 300
        goal_text = " CALORIE SURPLUS (Muscle Building)"
    else: 
        calories = maintenance_calories - 400
        goal_text = " CALORIE DEFICIT (Cutting)"
    
    if goal == 1: 
        protein_per_kg = 2.0
    else:  
        protein_per_kg = 2.2
    
    protein_grams = weight * protein_per_kg
    protein_calories = protein_grams * 4
    
   
    fat_percentage = 0.28
    fat_calories = calories * fat_percentage
    fat_grams = fat_calories / 9
    
    
    carb_calories = calories - (protein_calories + fat_calories)
    carb_grams = carb_calories / 4
    
   
    nutrition_info = {
        'calories': calories,
        'protein_grams': protein_grams,
        'protein_calories': protein_calories,
        'fat_grams': fat_grams,
        'fat_calories': fat_calories,
        'carb_grams': carb_grams,
        'carb_calories': carb_calories,
        'goal_text': goal_text
    }
    
    return nutrition_info

def display_results(name, age, height, weight, maintenance_calories, nutrition, goal):
    """Display all results in a nice format"""
    clear_screen()
    
    print("\n" + "="*55)
    print("              NUTRITION REPORT")
    print("="*55)
    
    
    print(f"\n USER INFORMATION:")
    print(f"   * Name: {name}")
    print(f"   * Age: {age} years")
    print(f"   * Height: {height} cm")
    print(f"   * Weight: {weight} kg")
    
    
    print(f"\n CALORIES:")
    print(f"   * Maintenance calories: {maintenance_calories:.0f} calories/day")
    print(f"   * {nutrition['goal_text']}: {nutrition['calories']:.0f} calories/day")
    
    
    if goal == 1:
        goal_name = " MUSCLE BUILDING"

    else:
        goal_name = " CUTTING"
    print(f"\n GOAL: {goal_name}")
    
    print("\n" + "-"*55)
    print(" DAILY NUTRIENT REQUIREMENTS:")
    print("-"*55)
    
   
    protein_percentage = (nutrition['protein_calories'] / nutrition['calories']) * 100
    print(f"\n PROTEIN:")
    print(f"   * Amount: {nutrition['protein_grams']:.1f} grams")
    print(f"   * Calories: {nutrition['protein_calories']:.0f} calories")
    print(f"   * Percentage: {protein_percentage:.1f}%")
    
   
    carb_percentage = (nutrition['carb_calories'] / nutrition['calories']) * 100
    print(f"\n CARBOHYDRATES:")
    print(f"   * Amount: {nutrition['carb_grams']:.1f} grams")
    print(f"   * Calories: {nutrition['carb_calories']:.0f} calories")
    print(f"   * Percentage: {carb_percentage:.1f}%")
    
  
    fat_percentage = (nutrition['fat_calories'] / nutrition['calories']) * 100
    print(f"\n FATS:")
    print(f"   * Amount: {nutrition['fat_grams']:.1f} grams")
    print(f"   * Calories: {nutrition['fat_calories']:.0f} calories")
    print(f"   * Percentage: {fat_percentage:.1f}%")

    print("\n" + "="*55)
    
    
    print("\n HELPFUL TIPS:")
    if goal == 1:
        print("   * Eat protein across 4-5 meals throughout the day")
        print("   * Drink plenty of water (3-4 liters daily)")
        print("   * Focus on compound exercises (squats, bench press, deadlift)")
        print("   * Get 7-8 hours of sleep for optimal recovery")
        print("   * Eat in a slight calorie surplus (300-500 calories)")
    else:
        print("   * Maintain high protein intake to preserve muscle")
        print("   * Reduce processed carbs and added sugars")
        print("   * Add cardio 3-4 times per week")
        print("   * Drink lots of water (3-4 liters daily)")
        print("   * Eat in a moderate calorie deficit (300-500 calories)")
    
    print("\n" + "="*55)

def main():
    """Main program function"""
    clear_screen()
    
    print(" " + " "*48 + " ")
    print(" " + " "*12 + " NUTRITION CALCULATOR " + " "*13 + " ")
    print(" " + " "*48 + " ")
    print(f"\n Welcome! This program will help you calculate your")
    print("daily nutrition needs for your fitness goals.")
    
    
    name, age, height, weight = get_user_info()
    
   
    activity_level = choose_activity_level()
    
   
    goal = choose_goal()
    
    
    bmr = calculate_bmr(weight, height, age)
    
  
    maintenance_calories = calculate_maintenance_calories(bmr, activity_level)
    
   
    nutrition = calculate_nutrition(weight, maintenance_calories, goal)
    
   
    display_results(name, age, height, weight, maintenance_calories, nutrition, goal)
    
  
    print("\n Would you like to calculate for someone else?")
    while True:
        again = input("Enter 'yes' or 'no': ").strip().lower()

        if again in ["yes" , "y"]:
            main()
            break

        elif again in ["no" , "n"]:

            print("\n Thank you for using the Nutrition Calculator!")
            print("   Good luck with your fitness journey! ")
            break
        else:
            print(" Please enter 'yes' or 'no'")


print("Starting Nutrition Calculator...")
#print("Created by: First Year Data Science Student ======> Yazan Abushreefih.")
main()
