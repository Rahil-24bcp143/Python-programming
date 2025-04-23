for hour in range(24):
    if hour == 0:
        print("12 AM (midnight)")
    elif hour < 12:
        print(hour, "AM")
    elif hour == 12:
        print("12 PM (noon)")
    else:
        print(hour - 12, "PM")