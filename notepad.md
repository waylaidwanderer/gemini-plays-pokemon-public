# Mechanics & Traversal
- Traversable Tiles: FLOOR (Standard), WARP_CARPET_DOWN/UP/LEFT/RIGHT (Map Exits), LADDER (Warps), TALL_GRASS.
- To Verify: GRASS, WATER, DOOR, STAIRS. (Note: Visual "doors" are often just FLOOR tiles with Warp events).
- Impassable Tiles: WALL, COUNTER, PC, TV, WINDOW, SIGN, SHELVES.
- One-Way Tiles: LEDGES (HOP_DOWN=South, HOP_LEFT=West, HOP_RIGHT=East).
- Interaction Rules: Face the object or person. For NPCs behind counters, stand on the tile adjacent to the counter, face the NPC, and press A.
- UI Interaction: Dialogue boxes block movement. Press B to close or advance text.

# Strategic Plan
- Primary Goal: Earn Zephyr Badge in Violet City.
- Secondary Goal: Return the Mystery Egg to Professor Elm in New Bark Town.
- Tertiary Goal: Buy Poké Balls (Check availability after errand).

# Quests & Information
- Main Quest: Return the Mystery Egg to Professor Elm in New Bark Town.
- Key Items: Mystery Egg, Pokédex.
- Note: Mr. Pokémon healed the party.
- Key Items: Mystery Egg, Pokédex.
- Note: Mr. Pokémon healed the party.
- Tips: Fisher suggested saving often. Guide Gent provided the Map Card.
- Route 30 Encounters: Caterpie (Morning/Day), Hoothoot (Night).
- Route 30 is located North of Cherrygrove City.

# Encounters & Area Data
- Route 29: Rattata, Hoothoot (Night).
- Route 46: Rattata, Spearow, Geodude (Found in Grass).
- Route 30: Caterpie (Morning/Day), Hoothoot (Night).
- Party: Kaen (Cyndaquil) Lv7.

# Inventory & Resources
- Items: Antidote x1, Berry x2, Potion x1.
- Key Items: Map Card, Mystery Egg, Pokédex.
- Money: ¥3000.

# Lessons Learned & Corrections
- Dialogue boxes halt movement; always clear them.
- Do not walk into NPCs; utilize `interact_direction` or `stun_npc`.
- Visual verification is useful, but the XML `type` attribute is the absolute source of truth for collision logic.
- Correction: 'GROUND' is not a valid XML type; 'FLOOR' is the standard type for walkable ground.