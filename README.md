# Drone Flight-Time Calculator

This project calculates a commercial drone's active flight time based on payload weight.

The flight-time formula is:

T(w) = 180 - 0.1w

Flight time cannot be less than 0 minutes.

## Functions

- `calculate_flight_time(weight_grams)` calculates the drone's flight time based on payload weight.
- `flight_time_table(max_weight_grams, step_grams)` creates a table of payload weights and their corresponding flight times.

## Testing

The project uses pytest to test zero payload, typical payloads, the zero-flight boundary, negative weight input, and the flight-time table. All five tests pass.

## AI-Use Disclosure

I used GitHub Copilot and Copilot Chat (`/tests`) to assist with the implementation and generate an initial test structure. I reviewed and modified the suggestions as needed, including accepting a correct suggestion, editing an incorrect suggestion, and rejecting an unrelated suggestion. I also reviewed the generated tests and verified the final implementation by running pytest.