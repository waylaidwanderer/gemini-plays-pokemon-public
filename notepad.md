# Gem's Pokémon Crystal Knowledge Base

## Tile Mechanics (Verified Traversability)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with SURF.
- TALL_GRASS / grass: Traversable.
- DOOR / WARP / CAVE: Entry points.
- LADDER / STAIRCASE: Moves between floors.
- COUNTER: Impassable. Interact from front.
- LEDGE_HOP_DOWN: One-way North to South.
- FLOOR_LEFT_WALL / FLOOR_RIGHT_WALL / FLOOR_UP_WALL: Impassable. These look like floor tiles but act as walls. Verified on Celadon Mansion Roof.
- OBJECTS (NPCs/Items): Impassable.
- WARP_CARPET_DOWN: Exit point.
- PC / BOOKSHELF: Impassable.

## Time Tracking
- Celadon City Exploration started: Turn 41410
- Celadon Mansion Exploration started: Turn 41442
- Secret Wing Exploration started: Turn 41569

## Progress Tracking
- **Find Misty Quest:** Completed Turn 41238.
- **Misty Defeated:** Turn 41351. Received Cascade Badge.
- **Cerulean Gym Cleanup:** COMPLETED Turn 41366.
- **Celadon City Arrival:** Turn 41410.

## Party Management
- Calcifer (Lv 60 Typhlosion): FLAMETHROWER, RETURN, SMOKESCREEN, THUNDERPUNCH.
- Gneiss (Lv 54 Graveler): EARTHQUAKE, DEFENSE CURL, STRENGTH, ROLLOUT.
- Icarus (Lv 19 Pidgeotto): FLY, SAND-ATTACK, GUST, QUICK ATTACK.
- Xenon (Lv 44 Haunter): HYPNOSIS, CONFUSE RAY, NIGHT SHADE, DREAM EATER.
- Lapis (Lv 12 Poliwag): WATERFALL, SURF, HYPNOSIS, WHIRLPOOL.
- KIMCHI (Lv 46 Gloom): FLASH, PETAL DANCE, CUT, SLEEP POWDER.

## Quest Log & Battle History
- **Kanto Gyms:** Pewter (Brock), Cerulean (Misty), Vermilion (Lt. Surge), Saffron (Sabrina): DEFEATED.
- Celadon (Erika): Next target.

## Celadon City Exploration Plan
1. Talk to NPCs in city [DONE].
2. Explore Celadon Mansion [DONE].
3. Locate Department Store, Game Corner [DONE].
4. Locate Celadon Gym [IN PROGRESS].
5. Defeat Erika.

## Celadon Mansion Investigation
- **Secret Wing Access:** Reached via back door at (16,3) in Celadon City. Passage behind mansion uses gaps in Row 3 at (24,3) or (25,3).
- **Vertical Path (Secret Wing):** 1F (3,0) -> 2F (0,0/1,0) -> 3F (0,0/1,0) -> Roof (1,1).
- **1F:** Granny (1,5), Clefairy (3,4), Nidoran (4,4), Meowth (2,6).
- **2F:** Meeting Room sign at (5,8). Bookshelf (2,3) has difficult books. Computer (0,3) has Kanto e-mail.
- **3F:** Graphic Artist (3,4) drew the player. Game Designer (3,6) talks about Pokedex. Fisher (0,4) talks about twins/Jasmine. Programmer (0,7) says play slots.
- **3F Details:** Game Program (1,6) (bug warning), Reference Material (1,3) (Poké Doll), Bookshelf (2,3) (magazines), Dev Room Sign (5,8).
- **Roof (Main):** Right side reached from 3F (7,0). Fisher (7,4) loves heights. Graffiti (6,1) moustache prank. Central wall structure (Cols 4-5) blocks all east-west movement except Row 8.
- **Roof House (Secret Wing):** Door at (2,5) on western roof leads here. Pharmacist (3,2) tells "terrifying tale" ONLY at night (currently 12:47 PM). TV (2,1), Bookshelves (0,1; 1,1), Radio (7,1), Map (3,0) checked.

## Celadon City Landmarks
- **Ladders:** (14, 16) and (15, 16) discovered. Blocked by water from the west.
- **Game Corner:** Entrance at (18, 19).
- **Celadon Restaurant?:** Entrance at (23, 19).
- **Trainer Tips (29, 21):** Ad for Dept Store (Guard Spec info).
- **Gym Search:** Likely in the southern part of the city. Gap in southern wall at Row 26 (Cols 16-19).

## Strategy & Lessons Learned
- **Celadon Pillars:** Column 12 (Rows 16-21) and Column 36 (Rows 22-26) are WALL tiles that block horizontal movement.
- **Water Obstacle:** Water at (13,18) to (15,21) blocks direct access to ladders from the west. Requires SURF.
- **NPC Interaction:**
    - Teacher (5,13): Talks about Dept Store selection.
    - Teacher (Game Corner area): Talks about girls playing slots now.
- **Hypothesis:** Gym is accessed via the southern gap at (16,26)-(19,26) or a western path.
- **Test:** Explore western side of Row 22.
- **Conclusion:** Pending.

## General Lessons & Error Log
- **Sprite Identity:** Sprites may not match their identity (e.g. Meowth looking like Growlithe). Check cries/dialogue.
- **Button Mixing:** Never mix directional and action buttons in overworld.
- **NPC Interaction:** Face the NPC (one turn) then press A (next turn) to ensure interaction.
- **Roof Walls:** Row 7 (Cols 0-4) and central structure (Cols 4-5) are impassable. Row 8 is a corridor.