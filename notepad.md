# Tile Mechanics (Global)
- FLOOR: This tile can be traversed in all directions. Verified by walking.
- WALL: This tile is impassable. Solid obstacle. Verified by walking into it.
- TALL_GRASS: This tile can be traversed. Triggers wild encounters. Verified by walking and encountering Pokémon.
- WATER: This tile is impassable without Surf. It can be traversed with Surf. Verified by attempting to walk onto it.
- HEADBUTT_TREE: This tile is impassable. It interacts with the Headbutt move. Verified by walking into it.
- CUT_TREE: This tile is impassable. It requires the Cut move to clear. Verified by walking into it.
- LEDGE_HOP_LEFT: This tile can only be traversed by hopping over it from East to West. It is a one-way ledge. Verified by hopping over it.
- FLOOR_UP_WALL: This tile is a one-way barrier (Southward). It can be passed from North to South, but is impassable from the South. Verified by attempting to walk North into it.
- WARP / CAVE / WARP_CARPET: These tiles are map transition points. They can be traversed to move between different maps. Verified by usage.

# Item Usage Tracking
- Super Repel: Wore off Turn 16817. (Previous activation: Turn 16778)

# Lessons Learned
- Input Hygiene: NEVER mix action (A, B, Start) and directional buttons in the same press_buttons call. It causes input truncation and desyncs step tracking.
- Repel Trick: Lv21 lead on Route 42 isolates Suicune (Lv40) from wild mons (max Lv15).

# HM/TM Knowledge
- HM01 Cut: KIMCHI (Gloom)
- HM02 Fly: ICARUS (Pidgey)
- HM03 Surf: Ravioli (Krabby)
- HM04 Strength: GNEISS (Graveler)

# Suicune Tracking & Strategy
- Status: Roaming. Moves when player changes maps.
- Repel Trick Mechanic: Lead Pokemon level > wild max, but < roamer (Lv40).
- Level Targets: Lv21 (Route 42/43), Lv27 (Route 44).
- Encounter Strategy: Use Mean Look (Turn 1) to prevent fleeing, then Hypnosis.
- Cycling Start: Turn 16587 (Wednesday, Dec 24, 2025).
- Current Attempt: Suicune confirmed on Route 42. Leading with XENON (Lv21).

# PC Storage (Box 1)
- VORTEX (Poliwag): Lv22, Male.
- INTERCEPT (Yanma): Lv12, Female.
- ROCKY (Onix): Lv6, Male.
- EGG (Cleffa): Lv5, Female.
- XFDW (Meowth): Lv16, Male.
- FRITTATA (Togepi): Lv5, Male.
- SHUCKIE (Shuckle): Lv15, Female.
- Blarney (SUDOWOODO): Lv20, Male.

# Exploration Targets
- Explore unseen tiles on Route 44 (e.g., (51, 12), (33, 15), (24, 17)).

# Item Indices (Bag - Items Pocket)
- Super Repel: Index 12.