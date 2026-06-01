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
    - (19, 15) (NE warp) -> Room 7 (SW) at (5, 17) (NE warp). (Hypothesis)
    - (15, 15) (NW warp) -> Room 3 (NE) at (21, 5) (NW warp). (Hypothesis)
    - (15, 17) (SW warp) -> Room 1 (NW) at (1, 7) (SW warp). (Hypothesis)
  - SW Room 7:
    - (5, 17) (NE warp) -> Room 9 (SE) at (19, 15) (NE warp). (Hypothesis)
    - (5, 19) (SE warp) -> Room 2 (NC) at (15, 7) (SE warp). (Hypothesis)
    - (1, 19) (SW warp) -> Room 4 (MW) at (1, 13) (SW warp). (Hypothesis)
    - (1, 17) (NW warp) -> Room 3 (NE) at (25, 7) (SE warp). (Hypothesis)
  - NC Room 2:
    - (15, 7) (SE warp) -> Room 7 (SW) at (5, 19) (SE warp). (Hypothesis)
    - (15, 5) (NE warp) -> Room 5 (MC - Sabrina) at (15, 11) (NE warp). (Hypothesis)
    - (11, 7) (SW warp) -> Room 5 (MC - Sabrina) at (11, 13) (SW warp). (Hypothesis)
    - (11, 5) (NW warp) -> Room 6 (ME) at (25, 13) (SE warp). (Hypothesis)

## Active Path to Sabrina (Room 5):
- **Path**: Room 8 (SC) -> Room 9 (SE) -> Room 7 (SW) -> Room 2 (NC) -> Room 5 (MC - Sabrina)
- **Current Position**: Room 9 (SE) at (19, 17).
- **Next Step**: Take (19, 15) (NE warp) by walking Up 2 steps from (19, 17).