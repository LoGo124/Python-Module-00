"""
Exercise 4: Plant Age Check

A function that determines if a plant is ready to harvest based on its age.
This exercise introduces conditional logic (if/else statements).
"""


def ft_plant_age() -> None:
    """
    Check if a plant is ready to harvest based on its age in days.

    This function prompts the user for a plant's age in days and
    determines if it's ready for harvest (strictly more than 60 days)
    or if it needs more time to grow.

    Returns:
        None
    """
    age: int = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
