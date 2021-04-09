import math 


# TODO: make this specific to each category 

# Update user proficiency using elo model
def getNewRating(
        rec_params: dict,
        qRating: float, 
        uRating: float, 
        actTime: float, 
        nIncorrect: int
    ):
    expTime = float(rec_params["exp_time"])
    K = float(rec_params["k_factor"])        # K Factor (indicates rating flexibility)
    incorrect_penalty_factor = float(rec_params["incorrect_penalty_factor"])
    time_multiplier = float(rec_params["time_multiplier"])

    # Calculate expected result
    # scoreExpected = 1 / (1 + pow(10, (uRating - qRating)/400))

    # TODO: set max penalty
    # if (nIncorrect == 0):
    #     scoreActual = 1
    # else:
    #     # For now, multiple incorrect answers are counted as just one incorrect answer
    #     scoreActual = 0

    # Reference: https://en.wikipedia.org/wiki/Elo_rating_system#Theory
    if actTime >= expTime:
        K *= -time_multiplier * (actTime - expTime)   # TODO: temp moderator
    else:
        K *= time_multiplier * (expTime - actTime) 

    adjustment = K #  * (scoreActual - scoreExpected)
    # Perform time adjustment TODO

    # Apply elo adjustment to get new elo 
    newRating = uRating + adjustment

    newRating -= nIncorrect * incorrect_penalty_factor

    return int(newRating)
