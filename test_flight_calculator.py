import pytest

from flight_calculator import calculate_flight_time, flight_time_table


def test_zero_payload():
    assert calculate_flight_time(0) == 180


def test_typical_payload():
    assert calculate_flight_time(500) == pytest.approx(130)


def test_zero_flight_boundary():
    assert calculate_flight_time(1800) == 0


def test_negative_weight_raises_value_error():
    with pytest.raises(ValueError, match="Weight cannot be negative."):
        calculate_flight_time(-1)


def test_flight_time_table():
    table = flight_time_table(300, 100)

    assert table == [
        (0, 180),
        (100, 170),
        (200, 160),
        (300, 150),
    ]