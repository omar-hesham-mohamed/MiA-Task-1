# Task 1.3: Verstappen vs Mostafa F1 Race Simulation

## Overview
This Python program simulates a head-to-head Formula 1 race between Max Verstappen and Hassan Mostafa using Object-Oriented Programming principles. The simulation features turn-based combat with offensive and defensive maneuvers that affect tire health and fuel levels.

## Files
- `Racer.py`: Abstract base class defining the racer interface
- `Verstappen.py`: Implementation of Max Verstappen's racing tactics
- `Mostafa.py`: Implementation of Hassan Mostafa's racing tactics
- `RaceText.py`: Text-based version of the race simulation
- `RaceVoice.py`: Voice-controlled version using Groq's speech-to-text API

## Features
1. **Complete OOP Implementation**:
   - Abstraction through `Racer` base class
   - Encapsulation of racer attributes
   - Polymorphism through different move implementations
   - Inheritance for shared racer properties

2. **Race Mechanics**:
   - Turn-based alternating gameplay
   - 3 offensive moves per racer with unique effects
   - 2 defensive maneuvers per racer
   - Fuel and tire health management
   - Voice control option for Max Verstappen

3. **Racer Specialties**:
   - **Verstappen**:
     - DRS Boost (45 fuel, 12 damage)
     - Red Bull Surge (80 fuel, 20 damage)
     - Precision Turn (30 fuel, 8 damage)
   - **Mostafa**:
     - Turbo Start (50 fuel, 10 damage)
     - Mercedes Charge (90 fuel, 22 damage)
     - Corner Mastery (25 fuel, 7 damage)

## How to Run
1. Run python RaceText.py or python RaceVoice.py