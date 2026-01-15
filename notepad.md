# Mechanics
- **Battle Cursor:** Remembers last move used.
- **Fly Map:** Visual Map (Cursor based). Use D-pad to select city. **Cursor persists:** Verify destination text.
- **Pokegear Map:** Visual. (Does NOT track Roamers in Crystal - Use Pokedex).
- **Menu Memory:** Start Menu and Pokegear cursors remember their last position. Always verify state.
- **Repel Safety:** Always re-apply Repel IMMEDIATELY upon expiration.

# Tile Mechanics
- **WARP_CARPET_RIGHT:** Usually requires walking off the map edge.
- **Sticky Warps (Gatehouses):** Require walking *into* the wall/direction of travel while ON the warp tile (e.g., Double Tap Right to enter).
- **TALL_GRASS:** Wild encounters possible.
- **LEDGE_HOP:** One-way movement.

# Strategic Status
- **Current Task:** Gatehouse Shuffle (Route 38 <-> Gatehouse).
- **Session Start:** Turn 40947 (Max Repel Applied).
- **Location:** Route 38.
- **Action:** Returning to Gatehouse (Shuffle Cycle).
- **Tool Note:** `patrol_grass` failed with sandbox error (Turn 40985). Using `navigate`.
- **Pokedex Mode:** Old (National Dex). Target: #243 Raikou, #244 Entei.
- **Strategy:** Blind Gatehouse Shuffle.
    1. Shuffle (Route 38 <-> Gatehouse).
    2. Run in grass for ~20 steps (Use `patrol_grass`).
    3. If no encounter, repeat.
- **Mechanics Note:** Max Repel appears ineffective on Route 38 (observed Turns 40908, 40918, 40933). Encounters occurring below lead level. Monitoring.