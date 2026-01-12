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


def calculate_force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    
    if mass == 0:
        print("An object cannot have zero mass.")
    elif acceleration == 0:
        print("Acceleration is zero, force will be zero.")
    else:
        force = mass * acceleration
        print("Force:", force, "N")


def calculate_work():
    force = float(input("Enter force (N): "))
    distance = float(input("Enter distance (meters): "))
    
    if distance == 0:
        print("Distance is zero, work will be zero.")
    elif force == 0:
        print("Force is zero, work will be zero.")
    else:
        work = force * distance
        print("Work:", work, "J")


print("Physics Calculator")
print("1 - Calculate Speed")
print("2 - Calculate Acceleration")
print("3 - Calculate Force")
print("4 - Calculate Work")

choice = input("Choose an option (1, 2, 3, or 4): ")

if choice == "1":
    calculate_speed()
elif choice == "2":
    calculate_acceleration()
elif choice == "3":
    calculate_force()
elif choice == "4":
    calculate_work()
else:
    print("Invalid choice")
