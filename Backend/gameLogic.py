from apscheduler.schedulers.background import BackgroundScheduler


# This lets us handle the tick logic in the background while the game is running. It should
# integrate with fastAPI but we can always check for bugs later on
scheduler = BackgroundScheduler()
scheduler.start()

# Adding a dictionary of all active tick counters for all active games, since we can
# run multiple games at once
tickCounters = {}


# Processes a tick for the counter for each game. Using the gameID rather than incrementing all tick
# counters lets us make individual games
def processTick(game: "game"): #This will lead to an error for now but will be fixed later
    tickCounters[game.id] += 1


# Initializes the game clock
def startGameClock(game):
    tickCounters[game.id] = 0