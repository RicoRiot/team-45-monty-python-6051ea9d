*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     Direction     EndingX     EndingY    
Move in middle of board N   5           5           NORTH       5       6
Move on south edge of board 5           0           SOUTH       5       0
Move on north edge of board 5           9           NORTH       5       9
Move on east edge of board  0           9           east        0       9
Move in middle of board S   5           5           south       5       4
Move in middle of board E   5           5           east        6       5
Move in middle of board W   5           5           WEST        4       5
Move on west edge of board  0           5           WEST        0       5

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}