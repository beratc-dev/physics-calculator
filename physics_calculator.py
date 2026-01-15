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


def calculate_density():
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m³): "))

    if volume == 0:
        print("Volume cannot be zero for a physical object.")
    elif mass == 0:
        print("An object cannot have zero mass.")
    else:
        density = mass / volume
        print("Density:", density, "kg/m³")


def calculate_pressure():
    force = float(input("Enter force (N): "))
    area = float(input("Enter area (m²): "))

    if area == 0:
        print("Area cannot be zero.")
    else:
        pressure = force / area
        print("Pressure:", pressure, "Pa")


def calculate_potential_energy():
    mass = float(input("Enter mass (kg): "))
    height = float(input("Enter height (m): "))
    gravity = 9.81
    
    if mass == 0:
        print("An object cannot have zero mass.")
    else:
        potential_energy = mass * gravity * height
        print("Potential Energy:", potential_energy, "J" )


def calculate_kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))

    if mass == 0:
        print("An object cannot have zero mass.")
    else:
        kinetic_energy = 0.5 * mass * velocity ** 2
        print("Kinetic Energy:", kinetic_energy, "J" )


def calculate_momentum():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))

    if mass == 0:
        print("An object cannot have zero mass.")
    else:
        momentum = mass * velocity
        print("Momentum:", momentum, "p")


print("Physics Calculator")
print("1 - Calculate Speed")
print("2 - Calculate Acceleration")
print("3 - Calculate Force")
print("4 - Calculate Work")
print("5 - Calculate Density")
print("6 - Calculate Pressure")
print("7 - Calculate Potential Energy")
print("8 - Calculate Kinetic Energy")
print("9 - Calculate Momentum")

choice = input("Choose an option (1, 2, 3, 4, 5, 6, 7, 8, or 9): ")

if choice == "1":
    calculate_speed()
elif choice == "2":
    calculate_acceleration()
elif choice == "3":
    calculate_force()
elif choice == "4":
    calculate_work()
elif choice == "5":
    calculate_density()
elif choice == "6":
    calculate_pressure()
elif choice == "7":
    calculate_potential_energy()
elif choice == "8":
    calculate_kinetic_energy()
elif choice == "9":
    calculate_momentum()
else:
    print("Invalid choice")
