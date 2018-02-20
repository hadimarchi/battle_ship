
class Game:
    def __init__(self, **kwargs):
        self.active_player = kwargs['active']
        self.inactive_player = kwargs['inactive']

    def swap_active_players(self):
        self.active_player, self.inactive_player = \
            self.inactive_player, self.active_player
