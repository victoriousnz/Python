from datetime import datetime

def get_departures():
    departures = []
    with open('date-time\data\departure-data.txt') as f:
        for line in f.read().splitlines():
            departure = get_departure(line)
            if departure:
                departures.append(departure)
    return departures

def get_departure(line):
    if line[0] == "*":
        return None

    datelist = line.split('\t')
    dt_planned = datelist[0]
    date_planned = datetime.strptime(dt_planned, '%m/%d/%Y %I:%M %p')

    dt_actual = datelist[1]
    if dt_actual:
        date_actual = datetime.strptime(dt_actual, '%m/%d/%Y %I:%M %p')
    else:
        date_actual = None

    return (date_planned, date_actual)



    """Return a tuple containing two  datetime objects."""

    # If the line begins with an asterisk (*), return None

    # Get the planned and actual departures as strings by
    # splitting the line on a tab character into a list
    # Assign the first item in the list to planned and the
    # second item to actual

    # Convert the planned departure time to a datetime and
    # assign the result to date_planned

    # For those lines that have an actual departure time,
    # convert the actual departure time to a datetime and
    # assign the result to date_actual.
    # For lines that don't have an actual departure date, assign
    # None to date_actual.

    # Return a tuple with date_planned and date_actual.
    

def left_ontime(departure):
    planned = departure[0]
    actual = departure[1]
    if not actual:
        return False
    return actual == planned

# Write the following four functions. They should
# all return a boolean value
def left_early(departure):
    planned = departure[0]
    actual = departure[1]
    if not actual:
        return False
    if actual < planned:
        return actual < planned
    

def left_late(departure):
    planned = departure[0]
    actual = departure[1]
    if not actual:
        return False
    if actual > planned:
        return actual > planned

def left_next_day(departure):
    planned = departure[0]
    actual = departure[1]
    if not actual:
        return False
    return actual.day > planned.day

def did_not_run(departure):
    actual = departure[1]
    if not actual:
        return True

def main():
    departures = get_departures()
    ontime_departures = [d for d in departures if left_ontime(d)]
    early_departures = [d for d in departures if left_early(d)]
    late_departures = [d for d in departures if left_late(d)]
    next_day_departures = [d for d in departures if left_next_day(d)]
    cancelled_trips = [d for d in departures if did_not_run(d)]

    print(f"""Total Departures: {len(departures)}
Ontime Departures: {len(ontime_departures)}
Early Departures: {len(early_departures)}
Late Departures: {len(late_departures)}
Next Day Departures: {len(next_day_departures)}
Cancelled Trips: {len(cancelled_trips)}""")

main()