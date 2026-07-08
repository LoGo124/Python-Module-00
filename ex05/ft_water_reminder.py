"""
Exercise 5: Water Reminder

A function that reminds when to water plants based on days since last watering.
This exercise practices conditional logic with numeric comparisons.
"""


def ft_water_reminder() -> None:
    """
    Determine if plants need watering based on days since last watering.

    This function prompts the user for the number of days since the
    last watering and advises whether the plants need watering now
    or if they're still fine (more than 2 days = water needed).

    Returns:
        None
    """
    days_since_watering: int = int(input("Days since last watering: "))
    if days_since_watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
