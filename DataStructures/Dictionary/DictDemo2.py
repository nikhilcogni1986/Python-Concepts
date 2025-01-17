# Nested Dictionaries
travel_Log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuggart", "Berlin"]
}

# Print France details / values
print(travel_Log["France"])
print(travel_Log["France"][1])
print(travel_Log["France"][0])

# Nested List
nested_list = ["A", "B", ["C", "D"]]
print(nested_list)
print(nested_list[0])
print(nested_list[2][1])

# Nested dictionaries
travel_log_nested = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "UnitedKingdom": {
        "cities_visited": ["Leamington Spa", "Stratford", "London"],
        "total_visits": 3
    }
}

