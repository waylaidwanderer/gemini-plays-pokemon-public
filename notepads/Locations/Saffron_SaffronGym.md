# Saffron City Gym - Sabrina's Psychic Network (Map 0_178)

## Gym Overview
- **Gym Leader**: Sabrina (Psychic-type specialist, Level 38-43 expected).
- **Badge**: Marsh Badge (allows control of up to Level 70 Pokémon, and TM46 Psywave).
- **Gym Guide**: Located at the entrance room, gives advice.

## Teleporter Tile Network Mapping (Burden of Proof & Verification)
- Saffron Gym is famous for its confusing grid of 9 interconnected rooms with warp/teleporter tiles in each corner (top-left, top-right, bottom-left, bottom-right).
- **Rule of Movement**: We will systematically map each teleporter connection.
- **Warp Connection Map**:
  - SC Room 8 (Entrance Room):
    - Only warp at (11, 15) -> Room 9 (SE) at (19, 17) (SE warp). (Verified Turn 42549)
  - SE Room 9:
    - (19, 17) (SE warp) -> Room 8 (SC) at (11, 15). (Verified Turn 42549)
    - (19, 15) (NE warp) -> Room 6 (ME) at (19, 9) (NE warp). (Verified Turn 42556)
    - (15, 15) (NW warp) -> Room 3 (NE) at (21, 5) (NW warp). (Hypothesis)
    - (15, 17) (SW warp) -> Room 1 (NW) at (1, 7) (SW warp). (Hypothesis)
  - ME Room 6:
    - (19, 9) (NE warp) -> Room 9 (SE) at (19, 15) (NE warp). (Verified Turn 42556)
    - (19, 11) (SE warp) -> Room 4 (MW) at (1, 9) (NW warp). (Verified Turn 42565)
  - MW Room 4:
    - (1, 9) (NW warp) -> Room 6 (ME) at (19, 11) (SE warp). (Verified Turn 42565)
    - (1, 11) (SW warp) -> Room 1 (NW) at (5, 5) (SE warp). (Verified Turn 42568)
  - NW Room 1:
    - (5, 5) (SE warp) -> Room 4 (MW) at (1, 11) (SW warp). (Verified Turn 42568)
    - (5, 3) (NE warp) -> Room 2 (NC) at (11, 3) (NE warp). (Verified Turn 42575)
  - NC Room 2:
    - (11, 3) (NE warp) -> Room 1 (NW) at (5, 3) (NE warp). (Verified Turn 42575)
    - (11, 5) (SE warp) -> Room 7 (SW) at (1, 17) (SW warp). (Verified Turn 42577)
  - SW Room 7:
    - (1, 17) (SW warp) -> Room 2 (NC) at (11, 5) (SE warp). (Verified Turn 42577)
    - (1, 15) (NW warp) -> Room 3 (NE) at (19, 5) (SE warp). (Verified Turn 42581)
  - NE Room 3:
    - (19, 5) (SE warp) -> Room 7 (SW) at (1, 15) (NW warp). (Verified Turn 42581)
    - (19, 3) (NE warp) -> Room 9 (SE) at (15, 15) (NW warp). (Verified Turn 42583)

## Active Path to Sabrina (Room 5):
- **Path**: Room 8 (SC) -> Room 9 (SE) -> Room 6 (ME) -> Room 4 (MW) -> Room 1 (NW) -> Room 2 (NC) -> Room 7 (SW) -> Room 3 (NE) -> Loop back to Room 9 (SE)
- **Current Position**: Room 9 (SE) at (17, 15).
- **Next Step**: Finish the battle against the Psychic, then re-evaluate the warp connections to find the actual path to Sabrina's Room (Room 5 MC).