# Viridian Gym - Layout & Notes

## General Information
- Location: Viridian City (32, 7)
- Leader: Giovanni
- Specialty: Ground / Normal types
- Badge: Earth Badge (8th & Final Badge) + TM27 Fissure

## Entrance Area
- Entrance / Exit warp mat: (16, 17) / (17, 17)
- Gym Guide: Located at (16, 15)
- Statues: Located at (15, 14..15) and (18, 14..15)

## Spin Tile Connectivity Matrix
| Start Tile | Direction | Stop Tile / Landing | Notes |
| :--- | :--- | :--- | :--- |
| (16, 10) | Down | (16, 12) | Entrance sector bypass |
| (19, 11) | Up | (19, 2) | Entrance to North Sector |
| (19, 1) | Left | (11, 1) | North Sector to Northwest Sector (blocked by Karate King at (10, 1)) |
| (10, 2) | Left | Northwest Arena | Direct access to Giovanni's arena from corridor (10, 3..5) |
| (11, 2) | Right | (17, 2) | Northwest Sector to North-Central Sector |
| (18, 2) | Down | (18, 11) | North-Central back to Entrance Sector |
| (13, 16) | Left | (7, 16) | Entrance sector to Southwest sector |
| (1, 15) | Up | Northwest Arena | Direct Up-spin expressway into Giovanni's arena |
| (5, 13) | Right | (7, 16) | Southwest spin tile |
| (4, 14) | Right | (7, 16) | Southwest spin tile |

## Gym Trainers Roster & Defeats
- [x] Blackbelt (Karate King): (10, 1) facing Right [Defeated Turn 21748]. Roster: Machoke Lv 38, Machop Lv 38, Machoke Lv 38. Reward: ¥950.
- [x] Blackbelt: (11, 11) facing Left [Defeated Turn 21762]. Roster: Machoke Lv 40. Reward: ¥1000.
- [x] Cooltrainer / Tamer: (12, 7) facing Down [Defeated Turn 21769]. Roster: Sandslash Lv 39.
- [x] Cooltrainer: (13, 5) facing Up [Defeated Turn 21798]. Roster: Rhyhorn Lv 39.
- [x] Tamer: (10, 7) facing Down [Defeated Turn 21887]. Roster: Rhyhorn Lv 43.
- [x] Tamer: (4, 16) facing Right [Defeated Turn 21908]. Roster: Arbok Lv 39, Tauros Lv 39.
- [x] Blackbelt: (2, 7) / (3, 7) [Defeated Turn 21913]. Roster: Machoke Lv 43.
- [x] Cooltrainer♂: (6, 7) / (6, 5) [Defeated Turn 21920]. Roster: Nidorino Lv 39, Nidoking Lv 39.
- [x] Gym Leader Giovanni: Northwest arena (2, 1) [Defeated Turn 21973]. Roster: Rhyhorn Lv 45, Dugtrio Lv 42, Nidoqueen Lv 44, Nidoking Lv 45, Rhydon Lv 50. Reward: Earth Badge & TM27 (Fissure).

## Items in Gym
- Item Ball: Located at (16, 8).
## Verified Collision Layout & Navigation Graph
- (11, 4), (12, 3), (14, 8), (13, 6), (11, 6), (10, 6), (9, 6), (9, 5), (8, 4) are walls.
- (10, 5) -> (10, 4) -> (10, 3) -> (10, 2) is an open vertical hallway connecting row 5 to row 2.
- (10, 2) connects west along row 2: (10, 2) -> (9, 2) -> (8, 2) -> ... directly into Giovanni's arena at top-left.
- (11, 2) is a Right-spin tile carrying back to (17, 2).