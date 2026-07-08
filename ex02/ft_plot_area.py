"""
Exercise 2: Garden Plot Area

A function that calculates the area of a rectangular garden plot.
This exercise introduces basic arithmetic operations and type conversion.
"""


def ft_plot_area() -> None:
    """
    Calculate and display the area of a rectangular garden plot.

    This function prompts the user for the length and width of a
    rectangular plot, calculates its area by multiplying the two values,
    and displays the result.

    Returns:
        None
    """
    length: int = int(input("Enter length: "))
    width: int = int(input("Enter width: "))
    area: int = length * width
    print(f"Plot area: {area}")
