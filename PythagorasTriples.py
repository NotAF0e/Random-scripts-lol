import math as m
import time
import os

# Initialize variables ----------------------------------------------------------------------------
while True:
    try:
        a_range_bottom = int(input("Enter the bottom range for a²: "))
        a_range_top = int(input("Enter the top range for a²: "))

        b_range_bottom = int(input("Enter the bottom range for b²: "))
        b_range_top = int(input("Enter the top range for b²: "))
        break

    except ValueError:
        print("You must enter an integer.")

a = a_range_bottom
b = b_range_bottom
amount_of_numbers = a_range_top * b_range_top

# Checks if inputs are_valid
if a_range_top < a_range_bottom or b_range_top < b_range_bottom:
    print("The top range cannot be smaller than the bottom range.")
    exit()
if a_range_top <= 0 or a_range_bottom <= 0 or b_range_top <= 0 or b_range_bottom <= 0:
    print("Range bottom and top cannot be negative or zero.")
    exit()

show_progress = input("Show progress while calculating"
                      "(VERY HIGH PERFORMANCE HIT)? (y/n): ").strip().lower()
if show_progress == "y":
    show_progress = True
else:
    show_progress = False

# Clears screen
os.system('cls' if os.name == 'nt' else 'clear')
print("Calculating Pythagoras triples...")

parameters_lst = (a, b, a_range_bottom, a_range_top, b_range_top, show_progress)


# Calculate Pythagoras triples --------------------------------------------------------------------
def calculate_triples(parameters):
    a_val = parameters[0]
    b_val = parameters[1]
    a_range_bottom_val = parameters[2]
    a_range_top_val = parameters[3]
    b_range_top_val = parameters[4]
    show_progress_val = parameters[5]
    triple_num_lst = 0
    triples_val = []
    while a_val < a_range_top_val and b_val < b_range_top_val:
        c = m.sqrt(a_val ** 2 + b_val ** 2)
        if c.is_integer() and a_val < b_val:
            triples_val.append(f"{a_val}² + {b_val}² = {int(c)}²")
            if show_progress_val:
                print(triples_val[triple_num_lst])
                triple_num_lst += 1
        a_val += 1
        if a_val == a_range_top_val:
            a_val = a_range_bottom_val
            b_val += 1
    return triples_val


time_start = time.time()
triples = calculate_triples(parameters_lst)
time_end = time.time()
time_taken = time_end - time_start
if not show_progress:
    for triple in triples:
        print(triple)

print(f"\n{len(triples)} Pythagoras triples found.")
if len(triples) == 0:
    print("No Pythagoras triples found.")
print(f"Completed in {time_taken}")
input("Press enter to continue...")
