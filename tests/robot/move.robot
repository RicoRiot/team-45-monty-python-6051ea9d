*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
https://github.com/level-up-program/team-45-monty-python-6051ea9d/blob/main/tests/robot/images/DesignClassDiagram.png
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***          StartingX   StartingY   StartingMoveCount	Direction   EndingX EndingY	EndingMoveCount
Move in middle of board N   5           5          	1				NORTH       5       6		2
Move on south edge of board 5           0          	2				SOUTH       5       0		3
Move on north edge of board 5           9          	3				NORTH       5       9		4
Move on east edge of board  0           9          	4				EAST        0       9		5
Move in middle of board S   5           5          	5				SOUTH       5       4		6
Move in middle of board E   5           5          	6				EAST        6       5		7
Move in middle of board W   5           5          	7				WEST        4       5		8
Move on west edge of board  0           5          	8				WEST        0       5		9


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