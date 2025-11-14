"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""
    seats = ['A','B','C','D']
    for i in range(number):
        yield seats[i % 4]

def generate_seats(number:int):
    """Generate a series of identifiers for airline seats."""
    seats_letters = ['A','B','C','D']
    row = 1
    count = 0

    while count < number:
        if row == 13:
            row += 1
            continue
        for letter in seats_letters:
            if count >= number:
                break
            yield f"{row}{letter}"
            count += 1
        row +=1


def assign_seats(passengers):
    """Assign seats to passengers. """

    seat_gen = generate_seats(len(passengers))
    return {passenger: next(seat_gen) for passenger in passengers}

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket."""
    for seat in seat_numbers:
        code = f"{seat}{flight_id}"
        yield code.ljust(12,"0")
