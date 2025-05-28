def square_meters_to_square_kilometers(square_meters):
    """
    Convert area from square meters to square kilometers.

    Args:
        square_meters (float): Area in square meters

    Returns:
        float: Area in square kilometers
    """
    return square_meters / 1_000_000


if __name__ == "__main__":
    # Example usage
    print(square_meters_to_square_kilometers(500_000))  # Output: 0.5
    print(square_meters_to_square_kilometers(2_500_000))  # Output: 2.5