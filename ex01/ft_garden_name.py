"""
Exercise 1: Garden Name

A function that prompts for a garden name and displays its status.
This exercise teaches basic input/output and string handling.
"""


def ft_garden_name() -> None:
    """
    Prompt for a garden name and display it with status information.

    This function asks the user for their garden name and displays
    it along with a fixed status message indicating the garden is
    growing well.

    Returns:
        None
    """
    garden_name: str = input("Enter garden name: ")
    print(f"Garden: {garden_name}")
    print("Status: Growing well!")
