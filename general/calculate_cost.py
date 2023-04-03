


def get_cost(minutes,km):
    route = km * 1000
    time = minutes * 200
    base_fee = 3500
    tarifa = route+time+base_fee
    return tarifa