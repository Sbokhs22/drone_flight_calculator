# Drone flight-time calculator


def calculate_flight_time(weight_grams):
    """Calculate active flight time based on payload weight.

    Args:
        weight_grams: Payload weight in grams.

    Returns:
        Active flight time in minutes.

    Raises:
        ValueError: If weight_grams is negative.
    """
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.")

    flight_time = 180 - (0.1 * weight_grams)

    return max(0, flight_time)


def flight_time_table(max_weight_grams, step_grams):
    """Create a table of payload weights and their flight times.

    Args:
        max_weight_grams: Maximum payload weight in grams.
        step_grams: Amount to increase the weight each time.

    Returns:
        A list of (weight, flight_time) pairs.
    """
    table = []

    weight = 0

    while weight <= max_weight_grams:
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time))
        weight += step_grams

    return table