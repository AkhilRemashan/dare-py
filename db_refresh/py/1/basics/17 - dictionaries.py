
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# Basic Calling
# print(monthConversions["Dec"])

# Calling using .get
# print(monthConversions.get("Aug"))

# Calling with default value
print(monthConversions.get("Sun", "Not a valid key"))
