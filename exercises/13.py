# user_input = int(input("Enter year of birth: "))

# def calculate(year_of_birth, current_year=2023):
#     age = current_year - year_of_birth
    
#     return age
# if calculate(user_input) > 120:
#     print("You are old")
# else:
#     print(calculate(user_input))

# user_input = input("Enter names seperated by commas (no spaces): ")

# def num_names(names):
#     items = names.split(",")
#     return len(items)

# print(num_names(user_input))

def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t
    
  
time = calculate_time(100)
print(time)