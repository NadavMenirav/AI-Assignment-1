import ext_plant

id = ["000000000"]


class Controller:
    """This class is a controller for the ext_plant game."""

    def __init__(self, game: ext_plant.Game):
        """Initialize controller for given game model."""
        self.original_game = game

    # This function receives a point on the grid and returns a boolean value based on whether there is a robot in that
    # coordinate
    def is_coordinate_contain_robot(self, coordinate, robots):

        for _, (r, c), _ in robots:
            if coordinate == (r, c):
                return True
        return False

    # This function receives a point on the grid and returns a boolean value based on whether there is a wall in that
    # coordinate
    def is_coordinate_contain_wall(self, coordinate):

        for wall in self.original_game.walls:
            if coordinate in wall:
                return True
        return False

    # This function receives a point on the grid and returns a boolean value based on whether the point is a legal
    # point on the gird
    def is_on_grid(self, coordinate):
        (r, c) = coordinate
        return 0 <= r < self.original_game.rows and 0 <= c < self.original_game.cols

    def is_action_legal(self, state, action, robot_moving):

        (robots, plants, taps, total_water_needed) = state
        (r, c) = robot_moving[1] # The coordinate of the robot

        if action == "UP":
            return (
                    not self.is_coordinate_contain_robot((r - 1, c), robots)
                    and not self.is_coordinate_contain_wall((r - 1, c))
                    and self.is_on_grid((r - 1, c))
            )





    def choose_next_action(self, state):
        """ Choose the next action given a state."""
        # (robots, plants, taps, total_water_needed) = state
        #
        # possible_actions = []
        # for robot in robots:

