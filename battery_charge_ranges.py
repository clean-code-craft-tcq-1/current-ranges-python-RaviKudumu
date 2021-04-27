
def charge_ranges(charge_rates):
    ranges = []
    range = []
    charge_rates.sort()
    for charge_rate in charge_rates:
        range.append(charge_rate)
    ranges.append(range)
    return ranges

