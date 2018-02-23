
class PlayerHelper(object):
    def __init__(self, player):
        self.player = player

    def position_is_bad(self):
        if self.aft_is_fore() or self.is_diagonal():
            return True
        return False

    def aft_is_fore(self):
        if self.player.buttons[0] == self.player.buttons[1]:
            return True

    def is_diagonal(self):
        if not (self.player.buttons[0][0] in self.player.buttons[1]
                or self.player.buttons[0][1] in self.player.buttons[1]):
                return True
        return False

    def get_length_and_alignment(self):
        length, vertical = {True: (
                            abs(self.player.buttons[0][1] - self.player.buttons[1][1]),
                            True),
                            False: (
                            abs(self.player.buttons[0][0] - self.player.buttons[1][0]),
                            False)
                            }[self.player.buttons[0][0] in self.player.buttons[1]]

        return (length, vertical)
