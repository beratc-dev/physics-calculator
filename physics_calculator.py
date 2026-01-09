# Physics Calculator

print("Physics Calculator")
print("1 - Calculate Speed")
print("2 - Calculate Acceleration")

choice = input("Choose an option (1 or 2): ")

if choice == "1":
    distance = float(input("Enter distance (meters): "))
    time = float(input("Enter time (seconds): "))
    speed = distance / time
    print("Speed:", speed, "m/s")

elif choice == "2":
    velocity_change = float(input("Enter change in velocity (m/s): "))
    time = float(input("Enter time (seconds): "))
    acceleration = velocity_change / time
    print("Acceleration:", acceleration, "m/s^2")

else:
    print("Invalid choice")
