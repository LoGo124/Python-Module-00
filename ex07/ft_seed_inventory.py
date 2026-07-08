def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """
    This function takes a seed type, quantity, and unit of measurement,
    and prints out the inventory information in a formatted way.

    Parameters:
    - seed_type (str): The type of seed (e.g., "tomato", "carrot").
    - quantity (int): The quantity of seeds.
    - unit (str): The unit of measurement (e.g., "packets", "grams", "area").

    Returns:
    - None
    """
    # Validate the unit
    formated_strings = {
        "packets": f"{quantity} packets available",
        "grams": f"{quantity} grams total",
        "area": f"covers {quantity} square meters"
    }
    if unit not in formated_strings:
        print("Unknown unit type")
        return

    # Print the inventory information
    print(f"{seed_type.capitalize()} seeds: " + formated_strings[unit])
