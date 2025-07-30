# Task 1.2: Secure Race Radio Transmission Protocol

## Overview
This Python implementation provides a robust encoding/decoding system for transmitting Formula 1 race commands between the pit crew and driver. The `Codec` class converts lists of commands into a single encoded string for transmission and accurately reconstructs the original commands upon receipt.

## File
- `Codec.py`: Contains the complete encoding/decoding implementation

## Features
1. **Lossless Encoding/Decoding**:
   - Preserves exact command content including spaces and special characters
   - Handles empty strings in command lists

2. **Transmission Format**:
   - Uses length-prefix encoding (e.g., "Hello" → "5_Hello")
   - Separates commands with underscore delimiters

3. **Error Resilience**:
   - Automatically handles commands containing underscores
   - Properly processes multi-word commands

## How to Use
1. Import Codec
2. Run Codec().encode(["Commands"]) to encode the commands
3. Run Codec().decode(encoded) to decode the encoded message