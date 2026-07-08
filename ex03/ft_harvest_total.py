"""
Exercise 3: Harvest Total

A function that calculates total harvest weight across multiple days.
This exercise teaches accumulation patterns and working with multiple inputs.
"""


def ft_harvest_total() -> None:
    """
    Calculate and display the total harvest weight across three days.

    This function prompts the user for harvest weights from three
    different days, sums them together, and displays the total.

    Returns:
        None
    """
    day1: int = int(input("Day 1 harvest: "))
    day2: int = int(input("Day 2 harvest: "))
    day3: int = int(input("Day 3 harvest: "))
    total: int = day1 + day2 + day3
    print(f"Total harvest: {total}")
