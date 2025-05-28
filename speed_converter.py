def mps_to_kph(mps):
    """
    Convert meters per second to kilometers per hour.

    Args:
        mps (float): Speed in meters per second

    Returns:
        float: Speed in kilometers per hour
    """
    return mps * 3.6

if __name__ == "__main__":
    # Test cases
    speeds_mps = [10, 25, 50, 100]

    print("MPS to KPH Conversion:")
    print("-" * 25)
    for speed in speeds_mps:
        kph = mps_to_kph(speed)
        print(f"{speed} m/s = {kph} km/h")

    try:
        user_input = float(input("\nEnter speed in m/s: "))
        result = mps_to_kph(user_input)
        print(f"{user_input} m/s = {result} km/h")
    except ValueError:
        print("Please enter a valid number")
