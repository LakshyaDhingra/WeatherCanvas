def get_data(days):
    dates = ["2024-26-12", "2024-27-12", "2024-28-12", "2024-29-12", "2024-30-12"]
    temperatures = [10, 11, 12, 13, 14]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures