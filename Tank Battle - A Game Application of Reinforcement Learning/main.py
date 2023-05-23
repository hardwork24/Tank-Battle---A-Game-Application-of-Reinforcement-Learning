import collections as cl
import numpy as np
from tankbattle.env.engine import TankBattle
from tankbattle.env.utils import Utils

game = TankBattle(render=True, player1_human_control=False, two_players=False, speed=60, debug=True, frame_skip=5)


def human_control():
    exp_replay = cl.deque(maxlen=1000)

    num_of_actions = game.get_num_of_actions()  # 5
    game.reset()

    # Convert state into grayscale (84, 84)
    state = Utils.process_state(game.get_state())

    while True:

        random_action = np.random.randint(0, num_of_actions)
        score = game.step(random_action)

        next_state = Utils.process_state(game.get_state())
        is_terminal = game.is_terminal()

        exp_replay.append([state, score, next_state, is_terminal])

        if is_terminal:
            print("P1 Score:", game.total_score_p1)
            print("Total Score", game.total_score)
            game.reset()
            # break
            pass


if __name__ == '__main__':
    # machine_control()

    human_control()
