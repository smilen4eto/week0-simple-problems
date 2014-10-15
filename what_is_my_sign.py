def what_is_my_sign(day, month):
    signs = (
        ("Aries", 21, 3, 20, 4),
        ("Taurus", 21, 4, 21, 5),
        ("Gemini", 22, 5, 21, 6),
        ("Cancer", 22, 6, 22, 7),
        ("Leo", 23, 7, 22, 8),
        ("Virgo", 23, 8, 23, 9),
        ("Libra", 24, 9, 23, 10),
        ("Scorpio", 24, 10, 22, 11),
        ("Sagittarius", 23, 11, 21, 12),
        ("Capricorn", 22, 12, 20, 1),
        ("Aquarius", 21, 1, 19, 2),
        ("Pisces", 20, 2, 20, 3)
        )
    for sign in signs:
        start_day = sign[1]
        start_month = sign[2]
        end_day = sign[3]
        end_month = sign[4]

        if day >= start_day and month == start_month or \
                day <= end_day and month == end_month:
            return sign[0]

print(what_is_my_sign(6, 8))
