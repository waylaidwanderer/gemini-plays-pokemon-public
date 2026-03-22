# Viridian Gym
[Navigation]
- Map ID: 0_45
- Entrance: (16, 17)

[Layout & Mechanics]
- Gym Guide at (16, 14) says trainers here use Ground-type Pokemon.
- Spin tiles (spinners) are present in this gym. Spotted at X=13, Y=16/17 (TYPE_55d0).
- Statues block direct North path at X=15 and X=18.
[Spinner Paths]
- (19, 11) [Up] -> shoots North, stops at yellow tile (19, 2).
- (19, 2) is a yellow stop tile in an enclosed corridor (X=18 to 19, Y=2 to 6).
- (19, 1) is a Left-pointing spinner.
- From (19, 2) stop tile, stepping Up hits (19, 1) [Left spinner].
- From (19, 2) stop tile, stepping Left hits (18, 2) [Down spinner].
- (19, 2) stop tile -> [Up] -> hits (19, 1) Left spinner. Pushes Left all the way to (11, 1) Down spinner.
- Black Belt `SPRITE_427f` at (11, 10) facing Up.
- Cooltrainer `SPRITE_e4ed` at (12, 8) facing Down (Defeated).
- Tamer `SPRITE_9238` at (10, 7) facing Down.
- Cooltrainer `SPRITE_e4ed` at (13, 5) facing Down.
- [Turn 49071 Reflection] Stopped on Down spinner at (11, 1). Likely because the Black Belt at (10, 1) (facing Right) spotted me and interrupted the spin.
- [Turn 49088] Defeated Blackbelt at (10, 1). The tile at (11, 1) is a Down spinner, and (11, 2) is a yellow stop tile. Stepping Down to continue.
- (11, 2) is a Right spinner (`TYPE_64a2`).
- Stepping Down from (11, 1) onto (11, 2) should push me Right along Y=2.
- (11, 2) Right spinner pushes all the way to (17, 2) yellow stop tile.
- No trainer at (17, 1). The stop at (17, 2) was just a stop tile.
- From (12, 1), the path Left hits the Down spinner at (11, 1), which loops back to the Right spinner at (11, 2) and pushes back to (17, 2).
- The correct path seems to be taking the Down spinner at (18, 2).
- Walking back to (17, 2) and stepping Right onto (18, 2).
- (18, 2) is a Down spinner (`TYPE_55cd`). Stepping onto it now.
- (18, 2) Down spinner pushes all the way South to the (18, 11) yellow stop tile.
- From (18, 11), the path South goes to Y=12, then West to another stop tile at (16, 12).
- (16, 9) is an Item Ball! It is blocked from the South by the Down spinner at (16, 10) and from the West by the wall at (15, 9). Must be accessed from the North.
- (16, 10) is a Down spinner, blocking the path North to the Cooltrainer at (16, 9).
- The path from (16, 12) continues West to (14, 12), North to (14, 9), then West to (12, 9) towards the Cooltrainer at (12, 7).