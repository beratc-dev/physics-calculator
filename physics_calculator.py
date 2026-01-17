def speed(delta_distance, delta_time):
    if delta_time <= 0:
        raise ValueError("Delta time must be greater than zero.")
    if delta_distance < 0:
        raise ValueError("Delta distance cannot be negative.")
    return delta_distance / delta_time


def acceleration(delta_velocity, delta_time):
    if delta_time <= 0:
        raise ValueError("Delta time must be greater than zero.")
    return delta_velocity / delta_time


def force(mass, acceleration):
    if mass <= 0:
        raise ValueError("Mass must be greater than zero.")
    return mass * acceleration


def work(force, delta_distance):
    if delta_distance < 0:
        raise ValueError("Delta distance cannot be negative.")
    return force * delta_distance


def density(mass, volume):
    if mass <= 0:
        raise ValueError("Mass must be greater than zero.")
    if volume <= 0:
        raise ValueError("Volume must be greater than zero.")
    return mass / volume


def pressure(force, area):
    if area <= 0:
        raise ValueError("Area must be greater than zero.")
    return force / area


def potential_energy(mass, delta_height, gravity=9.81):
    if mass <= 0:
        raise ValueError("Mass must be greater than zero.")
    return mass * gravity * delta_height


def kinetic_energy(mass, delta_velocity):
    if mass <= 0:
        raise ValueError("Mass must be greater than zero.")
    return 0.5 * mass * delta_velocity ** 2


def momentum(mass, delta_velocity):
    if mass <= 0:
        raise ValueError("Mass must be greater than zero.")
    return mass * delta_velocity


def delta_thermo_entropy(delta_reversible_heat, absolute_temperature):
    if absolute_temperature <= 0:
        raise ValueError("Absolute temperature must be greater than zero (Kelvin).")
    return delta_reversible_heat / absolute_temperature

