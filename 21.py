import time

def part_1(p1_pos, p2_pos):
    p1_points = 0
    p2_points = 0

    die = 1
    die_rolls = 0
    while True:

        for _ in range(3):
            p1_pos += die
            die_rolls += 1
            die = (die + 1) % 100
        p1_pos = (p1_pos - 1) % 10 + 1
        p1_points += p1_pos
        if p1_points >= 1000:
            print("Part 1:")
            print(f"\tPlayer 1 wins with {p1_points} points.")
            print(f"\t{die_rolls} * {p2_points} = {die_rolls * p2_points}")
            break


        for _ in range(3):
            p2_pos += die
            die_rolls += 1
            die = (die + 1) % 100
        p2_pos = (p2_pos - 1) % 10 + 1
        p2_points += p2_pos
        if p2_points >= 1000:
            print("Part 1:")
            print(f"\tPlayer 2 wins with {p2_points} points.")
            print(f"\t{die_rolls} * {p1_points} = {die_rolls * p1_points}")
            break

def play_turns_wo_cache(p1_pos, p2_pos):
    n_universes_won = [0, 0]

    queue = [((p1_pos, 0), (p2_pos, 0), 1, 0)]

    round_number = 0
    start = time.time()

    while queue:
        (p1_pos, p1_score), (p2_pos, p2_score), n_permutations, count = queue.pop(0)
        for n_combinations, n_steps in zip(possible_n_combinations, possible_n_steps):
            p1_pos_ = p1_pos + n_steps
            p1_pos_ = (p1_pos_ - 1) % 10 + 1
            p1_score_ = p1_score + p1_pos_
            n_permutations_ = n_permutations * n_combinations
            if p1_score_ >= winning_score:
                n_universes_won[count % 2] += n_permutations_
            else:
                to_append = ((p2_pos, p2_score), (p1_pos_, p1_score_), n_permutations_, count + 1)
                queue.append(to_append)

        if count > round_number:
            round_number += 1
            print(f"\t\t...round {count} took {time.time() - start:.1f} seconds.")
            start = time.time()

    return n_universes_won

def play_turn_w_cache(position_1, position_2, score_1 = 0, score_2 = 0):
    state = (position_1, position_2, score_1, score_2)

    if state in saved_states:
        return saved_states[state]
    
    won_combinations = [0, 0]

    for (n_steps, n_combos) in combos:
        position_1_ = position_1 + n_steps
        position_1_ = (position_1_ - 1) % 10 + 1
        score_1_ = score_1 + position_1_
        if score_1_ >= winning_score:
            won_combinations[0] += n_combos
        else:
            won_combinations_next, won_combinations_current =  play_turn_w_cache(position_2, position_1_, score_2, score_1_)
            won_combinations[0] += won_combinations_current * n_combos
            won_combinations[1] += won_combinations_next * n_combos
    saved_states[state] = won_combinations

    return won_combinations

# Player 1 starting position: 4
# Player 2 starting position: 7
winning_score = 21
p1_pos = 4
p2_pos = 7

# ===== Part 1 =====
part_1(p1_pos, p2_pos)

# ===== Part 2 =====
print("Part 2:")
possible_n_combinations = [1, 3, 6, 7, 6, 3, 1]
possible_n_steps = [3, 4, 5, 6, 7, 8, 9]

combos = [(n_steps, n_combinations) for (n_steps, n_combinations) in zip(possible_n_steps, possible_n_combinations)]

# With cache
print("\tWith caching:")
saved_states = {}       
start = time.time() 
n_universes_won = play_turn_w_cache(p1_pos, p2_pos)
print(f"\t\tFinished in {time.time() - start:.1f} seconds.")
print(f"\t\tThe answer is {max(n_universes_won)}.")

# Without cache
print("\tWithout caching:")
start = time.time() 
n_universes_won = play_turns_wo_cache(p1_pos, p2_pos)
print(f"\t\tFinished in {time.time() - start:.1f} seconds.")
print(f"\t\tThe answer is {max(n_universes_won)}.")