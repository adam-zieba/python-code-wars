from datetime import date

def period_is_late(last, today, cycle_lenght):
    res = (today - last)
    string_res = str(res).split()
    if int(string_res[0]) > cycle_lenght:
        return True
    else:
        return False


def period_is_late_best(last, today, cycle_lenght):
    return (today - last).days > cycle_lenght


print(period_is_late(date(2023, 6, 1), date.today(), 28))