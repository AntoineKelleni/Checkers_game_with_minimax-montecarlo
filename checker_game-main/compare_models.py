# compare_models.py

import time
from checker_model import CheckerModel
from minimax import Minimax

def run_game(player1, player2):
    # This function should run a game between player1 and player2 and return the winner
    # You'll need to implement this based on your game's rules
    pass

def compare_models(depths):
    results = {}
    for depth in depths:
        minimax = Minimax(depth)
        random_model = CheckerModel()  # Assuming CheckerModel is the random model
        start_time = time.time()
        winner = run_game(minimax, random_model)
        end_time = time.time()
        execution_time = end_time - start_time
        results[depth] = (winner, execution_time)
    return results

depths = [1, 2, 3, 4, 5]
results = compare_models(depths)
for depth, (winner, execution_time) in results.items():
    print(f"Depth: {depth}, Winner: {winner}, Execution time: {execution_time}")