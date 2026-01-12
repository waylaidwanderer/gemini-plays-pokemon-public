# Strategic Plan: Kanto Badges & Cinnabar Island
- **Primary Goal:** Defeat the remaining Kanto Gym Leaders (Blaine and Blue).
- **Current Objective:** Reach Cinnabar Island.
- **Strategy (The HOW):**
    1. Navigate south through Viridian City to reach Pallet Town.
    2. Visit Professor Oak's Lab in Pallet Town.
    3. Use LAPIS (Poliwag) with SURF at the southern edge of Pallet Town to enter Route 21.
    4. Navigate Route 21 south to reach Cinnabar Island.
    5. Find and defeat Gym Leader Blaine (Note: Cinnabar was destroyed, check Seafoam Islands if necessary).
    6. Return to Viridian City to challenge the final Gym Leader (Blue).

# Game Mechanics & Systems
## Tile Traversal (Global)
- FLOOR: Standard walkable.
- WALL: Impassable.
- WATER: Requires SURF.
- TALL_GRASS: Wild encounters.
- DOOR/WARP/STAIRS: Map transitions.
- LEDGE_HOP_DOWN: One-way North to South.
- CUT_TREE: Impassable until CUT is used (KIMCHI).
- COUNTER: Blocks movement; allows NPC interaction. Verified in Trainer House 1F.
- BOOKSHELF: Verified wall-like collision.

## Inventory & Economy
- Item Pocket Limit: 20 unique items.
- Money Making: Selling Nuggets (found one at (15, 15) Route 2).

# Area Records (Kanto)
## Viridian City
- Entrance from Route 2 (South): (19, 0).
- Gramps (Object 1): Wandering near (18, 7). Expert catcher, loves espresso.
- Welcome Sign: (19, 1).
- Nickname Speech House (21, 9): Exploration complete.
- Trainer House (23, 15): 
    - 1F: Receptionist (0, 11), Cooltrainer M (7, 11), Cooltrainer F (6, 2).
    - B1F: Receptionist (7, 1). Daily practice battles available.
- Viridian Gym: Location to be confirmed.

## Route 2 (South)
- Picked up Elixir at (14, 50).
- Cut tree at (12, 50) cleared.
- Entrance to Viridian City at (7-9, 53).

## Diglett's Cave
- Exit to Route 2 (East): (15, 5).

# Battle & Pokémon Data
## Party Status
- Calcifer (Typhlosion Lv63): FLAMETHROWER, RETURN, SMOKESCREEN, THUNDERPUNCH.
- GNEISS (Graveler Lv54): EARTHQUAKE, DEFENSE CURL, STRENGTH, ROLLOUT.
- ICARUS (Pidgeotto Lv19): FLY, SAND-ATTACK, GUST, QUICK ATTACK.
- XENON (Haunter Lv44): HYPNOSIS, CONFUSE RAY, NIGHT SHADE, DREAM EATER.
- LAPIS (Poliwag Lv12): WATERFALL, SURF, HYPNOSIS, WHIRLPOOL.
- KIMCHI (Gloom Lv49): FLASH, PETAL DANCE, CUT, SLEEP POWDER.

## PC Storage (Box 1) (9/20)
- GORP (Snorlax Lv50), AAAAAAAAAA (Spinarak Lv13), GLAIVE (Scyther Lv14), SELKIE (Seel Lv24), DELTA (Mantine Lv20), RANGOON (Krabby Lv22), NOMURA (Tentacool Lv17), Ravioli (Krabby Lv10), Ouroboros (Dratini Lv15).

# Progress Log
- [Turn 42651] Defeated Trainer CAL in Trainer House. Earned ¥5000. Calcifer Lv63.
- Trainer House B1F: Daily battle completed.

# Strategy: Trainer House B1F Exploration
- Observed: Western side (X=0-3) is blocked by walls/counters from the central area.
- Observed: The unseen tiles (3, 2) through (3, 6) are adjacent to walls or counters.
- Hypothesis: The western section of B1F is inaccessible from the main floor and likely serves as the opponent's side of the battle arena.
- Conclusion: No further exploration possible in B1F.

# General Lessons
- Trainer House battles are limited to once per day.
- Arena layouts may have inaccessible "spectator" or "opponent" areas that remain unseen.
- Turn 42661: Daily battle completed, ¥5000 earned. Heading to Pallet Town next.

# Strategy: Navigating Viridian City South
- Observed: A horizontal wall/barrier exists at Y=31, extending from X=10 to at least X=27.
- Observed: A gap in the Y=31 wall exists at X=28-29, but it leads to a section blocked by vertical walls at X=27 and X=30.
- Observed: The pathfinder failed to go south at X=14 due to the wall.
- Hypothesis: There may be a path south on the far western side of the city (X < 10) or through a building.
- Plan: Explore the western edge of the city along Row 30 to look for a gap or alternate route.