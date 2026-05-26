# Route 24 & Route 25 Geographical Records

## Map Transitions & Connections:
- **Route 24 Southern Boundary**: Connects to Cerulean City at (21, 0) from Route 24 (11, 35).
- **Route 24/25 Transition**: Route 24 (19, 8) connects directly to Route 25 (0, 8).

## Active Overworld Blockades (Trainer Coordinates):
These coordinates represent solid overworld sprites of defeated trainers. They act as physical barriers that must be bypassed during routing.

### Route 24 (Nugget Bridge) Blockades:
- **Cale**: (11, 31) - blocks Column 11.
- **Ali**: (10, 28) - blocks Column 10.
- **Youngster**: (11, 25) - blocks Column 11.
- **Lass**: (10, 22) - blocks Column 10.
- **Bug Catcher**: (11, 19) - blocks Column 11.
- **Rocket Grunt**: (11, 15) - blocks Column 11.

### Route 25 Blockades:
- **Franklin**: (8, 4) - blocks Column 8.
- **Youngster**: (14, 3) - blocks Column 14 (on Row 3, leaving Row 4 clear).
- **Green-Vest**: (18, 5) - blocks Column 18 Row 5.
- **Lass**: (18, 8) - blocks Column 18 Row 8 (Note: Row 7 is clear between Green-Vest and Lass).
- **Nob**: (23, 9) - blocks Column 23.
- **Jr. Trainer ♂**: (24, 6) - blocks Column 24 Row 6.
- **Lass (Picnicker)**: (32, 3) - blocks Column 32.
- **Lass (Bug Catcher)**: (37, 4) - blocks Column 37.

## Nugget Bridge Defeated Trainer Bypass Routes (Going North):
To walk north up Nugget Bridge from the Cerulean City transition at (21, 0) to Route 25 while completely avoiding collisions with the solid, defeated trainer sprites:
1. Transition onto Route 24 at (11, 35).
2. Walk Left 1 step to (10, 35).
3. Walk Up 5 steps along Column 10 to (10, 30) (bypassing Bug Catcher Cale at (11, 31)).
4. Walk Right 1 step to (11, 30).
5. Walk Up 3 steps along Column 11 to (11, 27) (bypassing Lass Ali at (10, 28)).
6. Walk Left 1 step to (10, 27).
7. Walk Up 3 steps along Column 10 to (10, 24) (bypassing Youngster at (11, 25)).
8. Walk Right 1 step to (11, 24).
9. Walk Up 3 steps along Column 11 to (11, 21) (bypassing Lass at (10, 22)).
10. Walk Left 1 step to (10, 21).
11. Walk Up 13 steps along Column 10 to (10, 8) (bypassing Rocket Grunt at (11, 15) and Bug Catcher at (11, 19)).
12. Walk Right 1 step to (11, 8) and walk north into Route 25.

## Route 25 Ledge Bypass Route (Going North):
- **Column 9 Ledge Bypass**: Column 9 at Row 7 is a flat, clear grass tile (TYPE_3fe2) with no ledge.
- This provides a completely open, bidirectional path connecting the southern pathway (Row 8) and the northern grass area (Row 6), allowing players to walk back north/west to the tall grass patch (Columns 2-7, Rows 4-5) without walking all the way east to Column 17.
- Path: Stand at (9, 8) south of the ledge, walk Up 2 steps to (9, 6), then walk West as needed. Fully verified on Turn 12805.