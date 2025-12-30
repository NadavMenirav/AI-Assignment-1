import ext_plant

id = ["000000000"]


class Controller:
    """This class is a controller for the ext_plant game."""

    def __init__(self, game: ext_plant.Game):
        """Initialize controller for given game model."""
        self.original_game = game


    def is_coordinate_contain_robot(self, coordinate, robots):

        for _, (r, c), _ in robots:
            if coordinate == (r, c):
                return True
        return False

    def is_coordinate_contain_wall(self, coordinate):

        for wall in self.original_game.walls:
            if coordinate in wall:
                return True
        return False

    def is_action_legal(self, state, action, robot_moving):

        #if action == "UP":




    def choose_next_action(self, state):
        """ Choose the next action given a state."""
        # (robots, plants, taps, total_water_needed) = state
        #
        # possible_actions = []
        # for robot in robots:

