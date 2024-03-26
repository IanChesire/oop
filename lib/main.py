from operator import itemgetter

def create_scoreboard(participants):
    scoreboard = []

    # Define points for each food type
    points_allocation = {
        "Chickenwings": 5,
        "Hamburgers": 3,
        "Hotdogs": 2
    }

    # Calculate each participant's total points
    for participant in participants:
        name = participant["name"]
        foods_consumed = participant["foods"]

        total_points = sum(points_allocation.get(food, 0) for food in foods_consumed)

        scoreboard.append({"name": name, "score": total_points})
        
    scoreboard.sort(key=itemgetter("score", "name"), reverse=True)

    return scoreboard