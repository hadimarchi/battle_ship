# battle_ship

## User Stories
### As a user I would like to ...
  1. Play a full game of battleship
  2. Not see my opponents PIECES
  3. Not have the oponent see my pieces
  4. View the game through a GUI
  5. Have intuitive gui menu
  6. Easily place pieces
  7. Make hits obvious and satisfying
  8. Make misses obvious and unsatisfying
  9. Audio
  10. Scoreboar/profiles/save previous games
  11. Board for each action (shooting, receiving shots)
  12. Add more features to core game(radar) to make game more skill based.
  13. Customize game options (board size, number of ships)
  14. Alternate weapons
  15. Random map events (depth charge, weapons, storms?)
  16. Historic/geographic maps
  17. Battleship POV
  18. Subs/Airplanes(scouts?) in differnt layers/planes
  19. find Easter Eggs

## Journal Entries

### William Horn <wbhorn@alaska.edu>

Date:   Sun Feb 25 18:33:27 2018 -0900

    Add endpoint to create game and save it in session

    The code to store the player/ships objects as dict's still needs to be
    implimented so the whole game object can be stored in the session as
    json.

Date:   Sun Feb 25 18:32:17 2018 -0900

    Add colors to for ascetics

    Also have a dummy request to create a game, and
    a none functioning button to switch players.

Date:   Sun Feb 25 17:14:51 2018 -0900

    Remove duplicat ship info

Date:   Sun Feb 25 17:03:55 2018 -0900

    Getting init ship types from backend

Date:   Sun Feb 25 16:15:22 2018 -0900

    Setup flask server to commincate between js and python code

Date:   Sun Feb 25 15:54:45 2018 -0900

    Split classes up into seprate files

Date:   Sun Feb 25 15:22:58 2018 -0900

    refactor ship draw function

    Also fixed positioning bug where row, col were not getting multiplied by
    size

Date:   Sun Feb 25 15:06:21 2018 -0900

    Start work on graphics

    About 2 hours of work sofar.

Date:   Sat Feb 24 21:55:13 2018 -0900

    Remove battle ship class in favor of just game class

Date:   Sat Feb 24 21:48:32 2018 -0900

    Move position class into seprate file

Date:   Sat Feb 24 21:43:35 2018 -0900

    Move tile creation method into position object

Date:   Sat Feb 24 21:37:47 2018 -0900

    Ship positions are handled by object

Date:   Sat Feb 24 21:22:30 2018 -0900

    Add is_vertical to position object

Date:   Sat Feb 24 21:18:25 2018 -0900

    Refactor position into simple object

Date:   Sat Feb 24 21:02:02 2018 -0900

    Turn battle ship class into factory function

    Also did some refactoring with how arguments are passed

Date:   Sun Feb 18 17:50:51 2018 -0900

    Fix broken directory/file structure

Date:   Sun Feb 18 17:40:12 2018 -0900

    Remove pycache folders

    These files should not ever be commited.

Date:   Fri Feb 16 18:52:54 2018 -0900

    Fix bug in set_position test

Date:   Fri Feb 16 18:48:37 2018 -0900

    Testing that direction can be set on ships

Date:   Fri Feb 16 18:43:26 2018 -0900

    Extreme positional values throw errors.

Date:   Fri Feb 16 17:58:28 2018 -0900

    Run tests with tests.py

Date:   Fri Feb 16 17:56:21 2018 -0900

    Test whether ship is out of bounds or not

Date:   Fri Feb 16 17:53:00 2018 -0900

    Pass in x, y coordinates to set ships position.

Date:   Fri Feb 16 17:51:45 2018 -0900

    Testing if position can be set

Date:   Fri Feb 16 17:48:00 2018 -0900

    Ships have a position keyword argument

Date:   Fri Feb 16 17:44:03 2018 -0900

    Test for ships having a position

Date:   Fri Feb 16 17:38:10 2018 -0900

    Make players have the right type of ships.

Date:   Fri Feb 16 17:30:14 2018 -0900

    Test players have ships of correct size.

Date:   Fri Feb 16 17:26:08 2018 -0900

    Test players have right number of ships.
