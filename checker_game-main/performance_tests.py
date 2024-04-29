import time
from minimax import Minimax
from monte_carlo import MonteCarlo

def run_game(player1, player2):
    # This function should run a game between player1 and player2 and return the winner
    # You'll need to implement this based on your game's rules
    pass

def test_performance(models, depths, num_pieces_list, num_games):
    results = {}
    for model in models:
        for depth in depths:
            for num_pieces in num_pieces_list:
                total_time = 0
                wins = 0
                for _ in range(num_games):
                    player1 = model(depth)
                    player2 = model(depth)
                    start_time = time.time()
                    winner = run_game(player1, player2, num_pieces)
                    end_time = time.time()
                    total_time += end_time - start_time
                    if winner == player1:
                        wins += 1
                average_time = total_time / num_games
                win_rate = wins / num_games
                results[(model.__name__, depth, num_pieces)] = (win_rate, average_time)
    return results

models = [Minimax, MonteCarlo]
depths = [1, 2, 3, 4, 5]
num_pieces_list = [10, 20, 30, 40, 50]
num_games = 10
results = test_performance(models, depths, num_pieces_list, num_games)
for (model_name, depth, num_pieces), (win_rate, average_time) in results.items():
    print(f"Model: {model_name}, Depth: {depth}, Number of pieces: {num_pieces}, Win rate: {win_rate}, Average execution time: {average_time}")