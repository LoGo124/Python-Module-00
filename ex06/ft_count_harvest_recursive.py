"""
Exercise 6: Count to Harvest - Recursive Version

A function that counts from 1 to N using recursion.
This exercise introduces recursive function patterns and base cases.
"""


def ft_count_harvest_recursive() -> None:
    """
    Count from 1 to a given number using recursion.

    This function prompts the user for the number of days until harvest,
    then counts from 1 to that number using a recursive helper function.
    After the count completes, it displays a "Harvest time!" message.

    Returns:
        None
    """

    def count_days(current_day: int, total_days: int) -> None:
        """
        Recursively count days from current_day to total_days.

        Args:
            current_day: The current day number to print
            total_days: The total number of days to count to

        Returns:
            None
        """
        if current_day <= total_days:
            print(f"Day {current_day}")
            count_days(current_day + 1, total_days)

    days: int = int(input("Days until harvest: "))
    count_days(1, days)
    print("Harvest time!")
