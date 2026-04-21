
bookings = {}


def book_ticket(user, movie, date, time, theatre, seat):

    key = f"{movie}-{date}-{time}-{theatre}"

    
    if key not in bookings:
        bookings[key] = []

    if seat in bookings[key]:
        return "Seat already booked"


    bookings[key].append(seat)

    return f"""Booking Successful!

User: {user}
Movie: {movie}
Date: {date}
Time: {time}
Theatre: {theatre}
Seat: {seat}
"""


def show_seats(booked_seats):

    layout = [
        ("₹560 RECLINER ROWS", ["I", "J"]),
        ("₹380 PRIME ROWS", ["E", "F", "G", "H"]),
        ("₹290 CLASSIC PLUS ROWS", ["C", "D"]),
        ("₹270 CLASSIC ROWS", ["A", "B"])
    ]

    print("\n SCREEN THIS WAY\n")

    for section, rows in layout:
        print(f"\n--- {section} ---\n")

        for r in rows:
            row_display = ""

            for c in range(1, 6):
                seat = f"{r}{c}"

                if seat in booked_seats:
                    row_display += "** "
                else:
                    row_display += f"{seat} "

            row_display += "   " 

            for c in range(6, 11):
                seat = f"{r}{c}"

                if seat in booked_seats:
                    row_display += "** "
                else:
                    row_display += f"{seat} "

            print(row_display)