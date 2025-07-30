# Task 1.1: Digital Gear Indicator

## Overview
This Python implementation simulates a Formula 1 steering wheel's digital gear display using 7-segment-style representation. The system shows gear positions from Neutral (0) to 8th gear with animation during gear shifts.

## Files
- `Gears.py`: Contains gear display patterns as Enum
- `Gearstick.py`: Main implementation with display and animation logic

## Features
1. **7-Segment Display Simulation**:
   - Each gear (0-8) has a unique 5x4 grid representation
   - Uses `#` for active segments and `-` for inactive segments

2. **Gear Shift Animation**:
   - Shows current gear for 0.5 seconds
   - Clears console
   - Displays new gear

3. **Error Handling**:
   - Catches invalid gear inputs (non-integers or out-of-range values)

## How to Use
1. Run `Gearstick.py`
2. The demo automatically shows gear shift from Neutral (0) → 1st gear
3. To test other gears, modify the last line:
   ```python
   myGearStick.display_gear(3)  # Change number to desired gear (0-8)