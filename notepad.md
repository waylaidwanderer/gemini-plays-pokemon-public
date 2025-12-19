# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Goal: Catch the bird to obtain HM01 (Cut).

## Puzzle Mechanics
- **Success Condition**: Interact from the tile directly behind the bird's facing direction.
- **Startle Logic**: Interacting from the front or side makes the bird fly ~6 tiles away.
- **Twig Logic**: Tiles with dark specs are noisy. Stepping on them makes the bird turn to face the player.
- **Verified Noisy Tiles (Specs)**: 
  - Row 26: (14, 26), (15, 26)
  - Row 28: (14, 28) to (18, 28)
  - Row 29: (17, 29), (18, 29)
- Row 30: (14, 30) is noisy. (15, 30) is clean.
- Row 31: (23, 31) to (29, 31) are noisy. (14, 31) and (15, 31) are clean.
- **Verified Clean Tiles**: Row 23, Row 24, Row 25, Row 27, Row 30 (except 14,30).

## Current Status
- Bird flew south. NPC movement path indicates it reached (15, 28).
- Target: Locate bird and check facing.
- Approach: Move south to (15, 27). Row 27 is clean. Row 26 is noisy.
- Note: Avoid (14, 26) and (15, 26) while moving south. I'll go around if needed.
- Wait, I'm at (15, 24). To get to (15, 27) without stepping on (15, 26), I must go: (15, 24) -> (14, 24) -> (14, 25) -> (13, 25) ... wait, (14, 25) is a tree.
- Let's check the map: (15, 24) to (15, 27). (15, 26) is noisy.
- I'll go (15, 24) -> (16, 24) ... wall. (14, 24) ... tree.
- I have to step on (15, 26) or take a huge detour. If I step on (15, 26), the bird at (15, 28) will turn to face me (UP).
- If it faces UP at (15, 28), I can catch it from (15, 29) (South).
- To reach (15, 29) silently: Go (15, 24) -> (20, 24) -> Row 34 passage -> (15, 29).
- This seems like the best plan. Make it face UP by stepping on (15, 26), then catch from the south.

## Tile Mechanics
- **FLOOR**: Passable. Clean ground.
- **TWIGS**: Noisy floor (specs). Alerts bird.
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.

## Locations & Progress
- **Charcoal Kiln**: Azalea (21, 13). Reward: Cut.
- **Badges**: Zephyr, Hive.

## Party Status
- Calcifer (QUILAVA) Lv22: Lead. Use 'battle_strategist_v3' for wild encounters.
- Team: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.