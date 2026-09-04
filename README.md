# Drone Flight-Time Calculator

This project calculates a commercial drone's active flight time based on payload weight.

The flight-time formula is:

T(w) = 180 - 0.1w

Flight time cannot go below 0 minutes.

## Functions

- `calculate_flight_time(weight_grams)` calculates active flight time based on payload weight.
- `flight_time_table(max_weight_grams, step_grams)` creates a table of weights and corresponding flight times.

## Testing

The project uses pytest to test zero payload, typical payloads, the zero-flight boundary, negative weight input, and the flight-time table.

All five tests pass.

## AI-Use Disclosure

Used GitHub Copilot and Copilot Chat (/tests) to assist with the implementation of the drone flight-time calculator and to generate the initial pytest test skeleton. I reviewed the generated code and tests, accepted a correct suggestion, edited an incorrect suggestion to meet the required formula and zero-flight behavior, rejected an unrelated suggestion, and verified the final implementation and all tests with pytest.