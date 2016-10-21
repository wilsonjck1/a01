"""
Problem:

    Government guidelines on acceptable workplace temperatures suggest
    that working environments should be at least 16 degrees, and at most
    27 degrees Celsius.

    The function 'thermostat' takes an input, the temperature, and should
    print out "Acceptable" if the temperature is between 16 and 27 (inclusive).
    Otherwise it should print "Too hot" or "Too cold" if the temperate is above
    or below that range.


Tests:

    >>> thermostat(6)
    Too cold
    >>> thermostat(16)
    Acceptable
    >>> thermostat(24)
    Acceptable
    >>> thermostat(27)
    Acceptable
    >>> thermostat(30)
    Too hot

"""


# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def thermostat(temp):

    if temp >=16 and temp <=27:
        print("Acceptable")

    elif temp <16:
        print("Too cold")

    else:
        print("Too hot")

