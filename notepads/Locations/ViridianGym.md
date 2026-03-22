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
- Trainer `SPRITE_427f` (Black Belt) at (10, 1).
- Trainer `SPRITE_9238` (Tamer?) at (10, 7).
- Trainer `SPRITE_e4ed` (Cooltrainer?) at (13, 5).
- Trainer `SPRITE_e4ed` at (12, 7).
- [Turn 49071 Reflection] Stopped on Down spinner at (11, 1). Likely because the Black Belt at (10, 1) (facing Right) spotted me and interrupted the spin.
- [Turn 49088] Defeated Blackbelt at (10, 1). The tile at (11, 1) is a Down spinner, and (11, 2) is a yellow stop tile. Stepping Down to continue.