def main():
    spacecraft = {"Name":"James Webb Space Telescope"}
    spacecraft["Distance"] = 0.01 # Creates a new Dictionary Entry
    spacecraft.update({"Country": "USA", "Orbit":"Sun"}) # Creates multiple new Dictionary Entries


    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========== Report ========

    Name: {spacecraft.get("Name", "Unknown")}
    Distance: {spacecraft.get("Distance", "Unknown")} AU
    Orbit: {spacecraft.get("Orbit", "Unknown")}
    Country: {spacecraft.get("Country", "Unknown")}

    ==========================
    """
    # Name: {spacecraft["Name"]} alt. method to retreive name

main()
