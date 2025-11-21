# Mechanics & Traversal
- Traversable Tiles: FLOOR (Standard), WARP_CARPET_DOWN/UP/LEFT/RIGHT (Map Exits), LADDER (Warps).
- To Verify: GRASS, WATER, DOOR, STAIRS. (Note: Visual "doors" are often just FLOOR tiles with Warp events).
- Impassable Tiles: WALL, COUNTER, PC, TV, WINDOW, SIGN, SHELVES.
- One-Way Tiles: LEDGES (HOP_DOWN=South, HOP_LEFT=West, HOP_RIGHT=East).
- Interaction Rules: Face the object or person. For NPCs behind counters, stand on the tile adjacent to the counter, face the NPC, and press A.
- UI Interaction: Dialogue boxes block movement. Press B to close or advance text.

# Strategic Plan
- Primary Goal: Earn Zephyr Badge in Violet City.
- Secondary Goal: Visit Mr. Pokémon on Route 30.
- Tertiary Goal: Buy Poké Balls at the Mart (Check if available before Route 30).

# Quests & Information
- Main Quest: Visit Mr. Pokémon (Go North from Cherrygrove to Route 30).
- Tips: Fisher suggested saving often. Guide Gent provided the Map Card.
- Route 30 is located North of Cherrygrove City.

# Encounters & Area Data
- Route 29: Rattata, Hoothoot (Night).
- Route 46: Rattata, Spearow, Geodude (Found in Grass).
- Party: Kaen (Cyndaquil) Lv6.

# Inventory & Resources
- Items: Potion x1.
- Key Items: Map Card.
- Money: ¥3000.

# Lessons Learned & Corrections
- Dialogue boxes halt movement; always clear them.
- Do not walk into NPCs; utilize `interact_direction` or `stun_npc`.
- Visual verification is useful, but the XML `type` attribute is the absolute source of truth for collision logic.
- Correction: 'GROUND' is not a valid XML type; 'FLOOR' is the standard type for walkable ground.
[Update] Exited Evolution House. Heading to Poké Mart.