#program to demonstrate default argument

def print_info(name,age=35):
    print("Name:",name)
    print("Age:",age)
print_info(age=50,name="gauri")
print_info(name="jaya")
print_info("priti",80)
