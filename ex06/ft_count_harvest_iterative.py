"""
Exercise 6: Count to Harvest - Iterative Version

A function that counts from 1 to N using a loop (iterative approach).
This exercise introduces loops and iteration patterns.
"""


def ft_count_harvest_iterative() -> None:
    """
    Count from 1 to a given number using an iterative loop.

    This function prompts the user for the number of days until harvest,
    then counts from 1 to that number, printing each day. After the count,
    it displays a "Harvest time!" message.

    Returns:
        None
    """
    days: int = int(input("Days until harvest: "))
    [print(f"Day {day}") for day in range(1, days + 1)]
    print("Harvest time!")
