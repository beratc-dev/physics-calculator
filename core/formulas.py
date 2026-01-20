from core.quantities import Quantity

# -----------------
# MECHANICS
# -----------------

def speed(delta_distance: Quantity, delta_time: Quantity) -> Quantity:
    delta_distance.require_value()
    delta_time.require_value()

    if not delta_distance.is_delta:
        raise ValueError("Distance must be a delta quantity.")
    if not delta_time.is_delta:
        raise ValueError("Time must be a delta quantity.")
    if delta_time.value <= 0:
        raise ValueError("Delta time must be greater than zero.")
    if delta_distance.value < 0:
        raise ValueError("Delta distance cannot be negative.")

    value = delta_distance.value / delta_time.value

    return Quantity(
        key="speed",
        name="Speed",
        symbol="v",
        value=value,
        unit="m/s",
        domain="mechanics")


def acceleration(delta_velocity: Quantity, delta_time: Quantity) -> Quantity:
    delta_velocity.require_value()
    delta_time.require_value()

    if not delta_velocity.is_delta:
        raise ValueError("Velocity must be a delta quantity.")
    if not delta_time.is_delta:
        raise ValueError("Time must be a delta quantity.")
    if delta_time.value <= 0:
        raise ValueError("Delta time must be greater than zero.")
        
    value = delta_velocity.value / delta_time.value

    return Quantity(
        key="acceleration",
        name="Acceleration",
        symbol="a",
        value=value,
        unit="m/s²",
        domain="mechanics")


def force(mass: Quantity, acceleration: Quantity) -> Quantity:
    mass.require_value()
    acceleration.require_value()

    if mass.value <= 0:
        raise ValueError("Mass must be greater than zero.")

    value = mass.value * acceleration.value

    return Quantity(
        key="force",
        name="Force",
        symbol="F",
        value=value,
        unit="N",
        domain="mechanics")


def work(force: Quantity, delta_distance: Quantity) -> Quantity:
    force.require_value()
    delta_distance.require_value()

    if not delta_distance.is_delta:
        raise ValueError("Distance must be a delta quantity.")
    if delta_distance.value < 0:
        raise ValueError("Delta distance cannot be negative.")

    value = force.value * delta_distance.value

    return Quantity(
        key="work",
        name="Work",
        symbol="W",
        value=value,
        unit="J",
        domain="mechanics",
        is_delta=True)


def momentum(mass: Quantity, velocity: Quantity) -> Quantity:
    mass.require_value()
    velocity.require_value()

    if mass.value <= 0:
        raise ValueError("Mass must be greater than zero.")

    value = mass.value * velocity.value

    return Quantity(
        key="momentum",
        name="Momentum",
        symbol="p",
        value=value,
        unit="kg·m/s",
        domain="mechanics")


def kinetic_energy(mass: Quantity, velocity: Quantity) -> Quantity:
    mass.require_value()
    velocity.require_value()

    if mass.value <= 0:
        raise ValueError("Mass must be greater than zero.")

    value = 0.5 * mass.value * velocity.value ** 2

    return Quantity(
        key="kinetic_energy",
        name="Kinetic energy",
        symbol="Eₖ",
        value=value,
        unit="J",
        domain="mechanics")


def potential_energy(mass: Quantity, delta_height: Quantity, gravity: Quantity) -> Quantity:
    mass.require_value()
    delta_height.require_value()
    gravity.require_value()

    if not delta_height.is_delta:
        raise ValueError("Height must be a delta quantity.")
    if mass.value <= 0:
        raise ValueError("Mass must be greater than zero.")

    value = mass.value * gravity.value * delta_height.value

    return Quantity(
        key="potential_energy",
        name="Gravitational potential energy",
        symbol="Eₚ",
        value=value,
        unit="J",
        domain="mechanics")


def density(mass: Quantity, volume: Quantity) -> Quantity:
    mass.require_value()
    volume.require_value()

    if mass.value <= 0:
        raise ValueError("Mass must be greater than zero.")
    if volume.value <= 0:
        raise ValueError("Volume must be greater than zero.")

    value = mass.value / volume.value

    return Quantity(
        key="density",
        name="Density",
        symbol="ρ",
        value=value,
        unit="kg/m³",
        domain="mechanics")


def pressure(force: Quantity, area: Quantity) -> Quantity:
    force.require_value()
    area.require_value()

    if area.value <= 0:
        raise ValueError("Area must be greater than zero.")

    value = force.value / area.value

    return Quantity(
        key="pressure",
        name="Pressure",
        symbol="p",
        value=value,
        unit="Pa",
        domain="mechanics)


def power(delta_work: Quantity, delta_time: Quantity) -> Quantity:
    delta_work.require_value()
    delta_time.require_value()

    if not delta_work.is_delta:
        raise ValueError("Work must be a delta quantity.")
    if not delta_time.is_delta:
        raise ValueError("Time must be a delta quantity.")
    if delta_time.value <= 0:
        raise ValueError("Delta time must be greater than zero.")

    value = delta_work.value / delta_time.value

    return Quantity(
        key="power",
        name="Power",
        symbol="P",
        value=value,
        unit="W",
        domain="mechanics"


def impulse(force: Quantity, delta_time: Quantity) -> Quantity:
    force.require_value()
    delta_time.require_value()

    if not delta_time.is_delta:
        raise ValueError("Time must be a delta quantity.")
    if delta_time.value <= 0:
        raise ValueError("Delta time must be greater than zero.")

    value = force.value * delta_time.value

    return Quantity(
        key="impulse",
        name="Impulse",
        symbol="J",
        value=value,
        unit="N·s",
        domain="mechanics",
        is_delta=True)

# -----------------
# THERMODYNAMICS
# -----------------

def delta_thermo_entropy(
    delta_reversible_heat: Quantity,
    absolute_temperature: Quantity
) -> Quantity:

    delta_reversible_heat.require_value()
    absolute_temperature.require_value()

    if not delta_reversible_heat.is_delta:
        raise ValueError("Reversible heat must be a delta quantity.")
    if absolute_temperature.value <= 0:
        raise ValueError("Absolute temperature must be greater than zero (Kelvin).")

    value = delta_reversible_heat.value / absolute_temperature.value

    return Quantity(
        key="delta_thermo_entropy",
        name="Change in thermodynamic entropy",
        symbol="ΔS",
        value=value,
        unit="J/K",
        domain="thermodynamics",
        is_delta=True)

# -----------------
# REGISTRY
# -----------------

from core.registry import FormulaRegistry

registry = FormulaRegistry()

registry.register(
    key="speed",
    func=speed,
    aliases=["velocity", "average speed"]
)

registry.register(
    key="acceleration",
    func=acceleration,
    aliases=["dv/dt"]
)

registry.register(
    key="force",
    func=force,
    aliases=["newton force"]
)

registry.register(
    key="pressure",
    func=pressure,
    aliases=["force per area"]
)

registry.register(
    key="delta_thermo_entropy",
    func=delta_thermo_entropy,
    aliases=["entropy change", "thermodynamic entropy"]
)

