# Suicune Hunt Strategy & Status
- Strategy: Repel Trick (Lead KIMCHI Lv 21 vs Wild Lv 13-16).
- Method: Pacing (Grass Dance) in grass at (28, 7) on Route 38.
- Battle Plan: Turn 1 Sleep Powder. Use `suicune_capture_analyst_v2`.
- Active Status: Restocked (10 Super Repels). Turn #12733.
- Safeguard: Re-verify Suicune location via Pokédex after crossing map boundaries.
- Tracking: Suicune located on Route 42 (Turn #12771).

# Route 38 Specific Notes
- TALL_GRASS at (28, 7): Pacing spot for Suicune.
- Gatehouse to Ecruteak City: Warp at (35, 8).

## Roaming Pokémon Reference
- Tracking: Do NOT use Fly to chase (randomizes location). Walk across map boundaries (gatehouses/warp carpets) to shift position predictably.
- Encountering: Repel Trick + pacing in grass.
- Capture: Sleep status on Turn 1.
- Movement: Shift routes ONLY when player crosses a map boundary (warp carpet, gatehouse) or after a battle with the roamer. Phone calls and other events do NOT move roamers.
- Trackable via Pokédex "AREA" map if previously seen.

## Tile Mechanics
- TALL_GRASS: Traversable. Triggers wild encounters.
- FLOOR: Traversable. Standard ground.
- WALL: Impassable. Collision blocking.
- HEADBUTT_TREE: Impassable. Can be interacted with from adjacent tile if player has Headbutt.
- LEDGE_HOP_DOWN: One-way traversable (South/Down only).
- LEDGE_HOP_LEFT: One-way traversable (West/Left only).
- LEDGE_HOP_RIGHT: One-way traversable (East/Right only).
- WARP_CARPET: Traversable. Triggers map transition.
- MART_SHELF: Impassable. Standard shop shelf.
- COUNTER: Impassable. Can interact with NPCs across it.

# PC Storage (Box 1)
- ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# General Lessons Learned
- Navigation Buffer: After using a warp, move 3+ tiles away before starting a new path.
- Repel Refresh: If game incorrectly claims Repel is active after wearing off, move 1 step to reset state.
- Phone Calls: Interrupt gameplay but do not affect Repel count or Roamer location.
- Overworld Interaction: Do not mix directional and action buttons in the same `press_buttons` call. Move adjacent first, then interact.

# Menu Navigation
- Pokédex AREA: Press 'A' on entry -> move to 'AREA' -> press 'A'.

# Mart Locations & Inventories
- Azalea: Poke Ball, Potion, Super Potion, Escape Rope, Repel, Antidote, Parlyz Heal, Flower Mail.
- Olivine: Great Ball, Super Potion, Hyper Potion, Antidote, Parlyz Heal, Awakening, Ice Heal, Super Repel.
- Ecruteak (4_6): POKé BALL, GREAT BALL, POTION, SUPER POTION, ANTIDOTE, PARLYZ HEAL, AWAKENING, BURN HEAL, ICE HEAL, REVIVE. (No Repels).
- Restock Goal: Buy 10+ Super Repels in Olivine. Current Funds: ¥6821. Started: Turn #12668.

# Suicune Capture Strategy Detail
- Lead: Gloom (KIMCHI) with Sleep Powder.
- Move 1: Sleep Powder. Suicune often flees on turn 1.
- Move 2: If Suicune is asleep, it cannot flee. Use Mean Look (not available yet) or just start throwing balls.
- Ball Choice: Great Balls (40 in inventory).
- Status: Sleep is the best status for increasing catch rate.
- Analyst: Use `suicune_capture_analyst_v2` to check probabilities.

# Navigation Strategy: Finding Suicune
1. Restock Super Repels (Olivine is best).
2. Use Pokédex to locate Suicune.
3. Move to a route adjacent to Suicune's location.
4. Cross map boundary to try and "trap" Suicune on the same route.
5. Apply Repel Trick.

# Boundary Dance Tracking
- Current Boundary: Route 38 (0, 10) < - > Route 39 (19, 10).
- Suicune Last Seen: Route 42.
- Strategy: Hop between 38 and 39 until Suicune is on one of them. Use Repel Trick with KIMCHI (Lv 21).