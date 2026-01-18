# Physics Calculator

A Python-based physics calculation engine designed to model, validate, and compute
fundamental and advanced physical quantities using a structured, quantity-based architecture.

## Purpose

This project is developed to:

- Apply physics formulas through software engineering principles
- Model physical quantities with proper units, symbols, and domains
- Enforce physical correctness (delta quantities, absolute constraints, unit consistency)
- Build a long-term academic GitHub portfolio
- Support future studies in engineering, physics, and space sciences

## Scope

The calculator is designed as a **physics computation core**, not just a simple calculator.

It supports:
- Mechanics and thermodynamics quantities
- Delta (Δ) and absolute quantity distinction
- Physically meaningful validation rules
- Future dependency-based solving (deriving quantities from base quantities)

The system is intentionally built to scale toward **hundreds of physical quantities**
across multiple physics domains.

## Architecture

- `Quantity` abstraction for all physical values
- Domain-based formula separation (mechanics, thermodynamics, etc.)
- Modular core structure:
  - `quantities.py` – physical quantity model
  - `formulas.py` – validated physics formulas
  - `solver.py` – dependency resolution (planned)
  - `registry.py` – search & autocomplete infrastructure (planned)

## Features

- Quantity-aware physics calculations
- Delta vs absolute quantity enforcement
- Unit and symbol tracking
- Physics-consistent input validation
- Extendable and domain-oriented design

## Technologies

- Python 3

## Future Development

- Automatic dependency solving (advanced calculation mode)
- Physics search engine with autocomplete
- Expansion into electromagnetism, waves, and modern physics
- Web-based or graphical interface
- Dataset-driven formula registration

## License

This project is licensed under the MIT License.

## Author

**Berat Çetin**  
High school student interested in physics, aerospace engineering, and astronomy.
