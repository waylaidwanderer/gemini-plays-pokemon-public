# persistent_knowledge
## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal. Jump down from lower Y to higher Y. Verified on Route 6.
- WARP_CARPET: Step on or walk off map edge to transition. Verified on Route 5/27.
- WARP_PANEL: Teleports between rooms. Verified in Saffron Gym.
- COUNTER: Impassable Wall. Must interact from an adjacent tile. Verified in Centers/Radio Tower.
- FLOOR_UP_WALL: Wall from the South. Potentially a ledge from the North, but currently blocking southward movement at (13, 25) in Rock Tunnel B1F. Testing other locations.

## Kanto Strategy
- **Primary Goal: Complete Kanto Region Journey.**
- **Current Objective: Resolve Power Plant Crisis.**
  - Plan: Find Mr. Fuji (Lavender) -> Route 10 -> Power Plant -> Cerulean Gym (Machine Part).

## PC Storage (Box 1)
1. GLAIVE (SCYTHER) Lv14, 2. SELKIE (SEEL) Lv24, 3. DELTA (MANTINE) Lv20, 4. RANGOON (KRABBY) Lv22, 5. NOMURA (TENTACOOL) Lv17, 6. Ravioli (KRABBY) Lv10, 7. Ouroboros (DRATINI) Lv15

## Lavender Town Notes
- (13, 11): Soul House (Mr. Fuji).
- Radio Tower: Ground floor only. Power crisis mentioned by Station Manager.

## Rock Tunnel Navigation
- Started: Turn 38914, Saturday, January 10, 2026.
- Strategy: Use Flash (KIMCHI). Head north for Power Plant exit.
- 1F Progress:
  - (10, 15): TM47 Steel Wing.
  - (4, 18): ELIXER.
  - (11, 14): FLOOR_UP_WALL blocks northern passage from entrance.
  - (27, 13) <-> B1F (3, 3).
  - (15, 9) <-> B1F (17, 9).
  - (5, 3) <-> B1F (23, 3).
  - (27, 3) <-> B1F (25, 23).
- Turn 38998: Navigating Rock Tunnel 1F. Current pos (27, 3).
- Observation: FLOOR_UP_WALL tiles at (13, 26), (8, 26), and (18, 26) are impassable from the North. Row 26 ledges function as walls in this area.
- Pathing: 1F (South) -> B1F (3, 3) -> B1F (17, 9) -> 1F (15, 9) -> 1F (5, 3) -> B1F (23, 3).
- Discovery: Ladder at (25, 23) in the southeastern section of B1F.

- Observed Pokemon (Kanto):
  - Rock Tunnel 1F: Geodude (Lv11-12), Zubat (Lv12), Haunter (Lv17).
  - Rock Tunnel B1F: Geodude (Lv14), Onix (Lv16) at (24, 16) and (16, 18).