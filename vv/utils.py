from datetime import datetime

def calculate_parking_cost(start_time, end_time, hourly_rate=5.0):
    """
    Calculate the cost of parking based on start and end times.

    Args:
        start_time (datetime): The start time of the parking session.
        end_time (datetime): The end time of the parking session.
        hourly_rate (float): The hourly rate for parking (default is $5.0 per hour).

    Returns:
        float: The total parking cost.
    """
    # Calculate the duration of the parking session in hours
    duration = (end_time - start_time).total_seconds() / 3600.0

    # Calculate the total cost based on the hourly rate
    total_cost = duration * hourly_rate

    return total_cost
