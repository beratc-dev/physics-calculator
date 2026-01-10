def calculate_speed():
    distance = float(input("Enter distance (meters): "))
    
    time = float(input("Enter time (seconds): "))
    
    if time == 0:
        print("Time cannot be zero.")
    else:
        speed = distance / time
        print("Speed:", speed, "m/s")


def calculate_acceleration():
    velocity_change = float(input("Enter change in velocity (m/s): "))
    
    time = float(input("Enter time (seconds): "))
    
    if time == 0:
        print("Time cannot be zero.")
    else:
        acceleration = velocity_change / time
        print("Acceleration:", acceleration, "m/s²")


print("Physics Calculator")
print("1 - Calculate Speed")
print("2 - Calculate Acceleration")

choice = input("Choose an option (1 or 2): ")

if choice == "1":
    calculate_speed()
elif choice == "2":
    calculate_acceleration()
else:
    print("Invalid choice")
