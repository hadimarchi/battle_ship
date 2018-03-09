# battle_ship

## To Run Locally

### Setup Api
Install requirments for flask app

    pip3 install -r requirements.txt

Then start the flask app

    python3 app.py

### Setup Frontend
Start local server in graphics directory

    cd graphics
    python -m http.server


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

### William Horn (<wbhorn@alaska.edu>)

####    Sun Feb 25 18:33:27 2018 -0900

    Add endpoint to create game and save it in session

    The code to store the player/ships objects as dict's still needs to be
    implimented so the whole game object can be stored in the session as
    json.

####    Sun Feb 25 18:32:17 2018 -0900

    Add colors to for ascetics

    Also have a dummy request to create a game, and
    a none functioning button to switch players.

####    Sun Feb 25 17:14:51 2018 -0900

    Remove duplicat ship info

####    Sun Feb 25 17:03:55 2018 -0900

    Getting init ship types from backend

####    Sun Feb 25 16:15:22 2018 -0900

    Setup flask server to commincate between js and python code

####    Sun Feb 25 15:54:45 2018 -0900

    Split classes up into seprate files

####    Sun Feb 25 15:22:58 2018 -0900

    refactor ship draw function

    Also fixed positioning bug where row, col were not getting multiplied by
    size

####    Sun Feb 25 15:06:21 2018 -0900

    Start work on graphics

    About 2 hours of work sofar.

####    Sat Feb 24 21:55:13 2018 -0900

    Remove battle ship class in favor of just game class

####    Sat Feb 24 21:48:32 2018 -0900

    Move position class into seprate file

####    Sat Feb 24 21:43:35 2018 -0900

    Move tile creation method into position object

####    Sat Feb 24 21:37:47 2018 -0900

    Ship positions are handled by object

####    Sat Feb 24 21:22:30 2018 -0900

    Add is_vertical to position object

####    Sat Feb 24 21:18:25 2018 -0900

    Refactor position into simple object

####    Sat Feb 24 21:02:02 2018 -0900

    Turn battle ship class into factory function

    Also did some refactoring with how arguments are passed

####    Sun Feb 18 17:50:51 2018 -0900

    Fix broken directory/file structure

####    Sun Feb 18 17:40:12 2018 -0900

    Remove pycache folders

    These files should not ever be commited.

####    Fri Feb 16 18:52:54 2018 -0900

    Fix bug in set_position test

####    Fri Feb 16 18:48:37 2018 -0900

    Testing that direction can be set on ships

####    Fri Feb 16 18:43:26 2018 -0900

    Extreme positional values throw errors.

####    Fri Feb 16 17:58:28 2018 -0900

    Run tests with tests.py

####    Fri Feb 16 17:56:21 2018 -0900

    Test whether ship is out of bounds or not

####    Fri Feb 16 17:53:00 2018 -0900

    Pass in x, y coordinates to set ships position.

####    Fri Feb 16 17:51:45 2018 -0900

    Testing if position can be set

####    Fri Feb 16 17:48:00 2018 -0900

    Ships have a position keyword argument

####    Fri Feb 16 17:44:03 2018 -0900

    Test for ships having a position

####    Fri Feb 16 17:38:10 2018 -0900

    Make players have the right type of ships.

####    Fri Feb 16 17:30:14 2018 -0900

    Test players have ships of correct size.

####    Fri Feb 16 17:26:08 2018 -0900

    Test players have right number of ships.


### Hal DiMarchi(<hadimarchi@alaska.edu>)

#### Date:   Wed Feb 28 15:15:47 2018 -0900

    made set sound watery
#### Date:   Wed Feb 28 14:55:26 2018 -0900

    added an alternative sound for placing
#### Date:   Wed Feb 28 14:52:56 2018 -0900

    added engine start sound for placing a boat
#### Date:   Wed Feb 28 14:23:47 2018 -0900

    game now uses turns

    Player who is not in play will have no effect if/when using
    the GUI.
#### Date:   Tue Feb 27 23:11:54 2018 -0900

    fixed merge conflicts and implemented placement
#### Date:   Tue Feb 27 23:06:25 2018 -0900

    can place ships through gui

    Backend logic is responsive to ship placement
    Some error handling is done in the frontend but most
    is done in the backend.
#### Date:   Tue Feb 27 20:25:35 2018 -0900

    swap players endpoint in app.py written
#### Date:   Tue Feb 27 16:25:12 2018 -0900

    fixed conflicts
#### Date:   Tue Feb 27 16:23:59 2018 -0900

    grabbing and returning status of ship (alive or dead)
#### Date:   Tue Feb 27 16:23:00 2018 -0900

    getting placement in the backend to work
#### Date:   Tue Feb 27 13:57:03 2018 -0900

    fire shot endpoint better

    Ironed out a bug that was causing shots to effect
    tiles they were not placed at.
#### Date:   Tue Feb 27 13:36:31 2018 -0900

    game from_dict function, flask app handles firing shots
#### Date:   Tue Feb 27 13:04:51 2018 -0900

    from and to dict functions for player, ship, and position with passing test cases

    From and to dict functions are for saving/loading the game state between
    requests using file I/O. 
#### Date:   Fri Feb 23 10:18:39 2018 -0900

    beginning work on battleship logic, and removing use of tkinter

    Tkinter seems to result in dirty code in my experience.
#### Date:   Thu Feb 22 15:38:37 2018 -0900

    refactor of player and gui
#### Date:   Wed Feb 21 15:26:51 2018 -0900

    lets call it refactoring
#### Date:   Mon Feb 19 10:07:30 2018 -0900

    fixing merge and allowing battle_ship module
#### Date:   Mon Feb 19 10:05:56 2018 -0900

    hopefully bringing in battle_ship module correctly
#### Date:   Sat Feb 17 15:27:34 2018 -0900

    fixing strange merge conflict
#### Date:   Sat Feb 17 15:26:36 2018 -0900

    fixed placement logic
#### Date:   Sat Feb 17 15:22:49 2018 -0900

    ships placed on board. bottom board is russia, top is america
#### Date:   Sat Feb 17 13:42:59 2018 -0900

    refactored position system and redid tests for that system. About to start setting ships with buttons
#### Date:   Sat Feb 17 12:31:29 2018 -0900

    all tests for BattleShip, Game, and GuiHelper classes passing
#### Date:   Sat Feb 17 12:29:07 2018 -0900

    all tests passing
#### Date:   Sat Feb 17 12:26:55 2018 -0900

    starting to implement gui and battleship game with players and ships. Some changes to ships include storing them in a dictionary, where keys are the type of ship, and removal of amount for the list of ship lengths
#### Date:   Fri Feb 9 16:07:01 2018 -0900

    formatting file structure of project, updating readme
#### Date:   Wed Feb 7 16:06:44 2018 -0900

    user stories
#### Date:   Wed Feb 7 15:50:25 2018 -0900

    .gitignore
#### Date:   Wed Feb 7 15:48:59 2018 -0900

    Merge branch 'master' of https://github.com/hadimarchi/battle_ship
#### Date:   Wed Feb 7 15:48:07 2018 -0900

    initial commit
#### Date:   Wed Feb 7 15:46:47 2018 -0900

    Initial commit
