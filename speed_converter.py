def mps_to_kph(mps):
    """
    Convert meters per second to kilometers per hour.
    Args: mps (float): Speed in meters per second
    Returns: float: Speed in kilometers per hour
    """
    return mps * 3.6

if __name__ == "__main__":

    try:
        user_input = float(input("\nEnter speed in m/s: "))
        result = mps_to_kph(user_input)
        print(f"{user_input} m/s = {result} km/h")
    except ValueError:
        print("Please enter a valid number")
