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
- **Session Start:** Turn 40832 (Repel Active).
- **Location:** Route 38 (Cycle #43).
- **Action:** Patrolling grass (Manual Path).
- **Pokedex Mode:** Old (National Dex). Target: #243 Raikou, #244 Entei.
- **Pokedex Status:** #243 (Raikou) & #244 (Entei) are UNSEEN.
- **Strategy:** Blind Gatehouse Shuffle.
    1. Shuffle (Route 38 <-> Gatehouse).
    2. Run in grass for ~20 steps (Use `get_route38_patrol_path`).
    3. If no encounter, repeat.
- **Anomaly:** Encountered Wild Rattata (Turn 40908) immediately after applying Max Repel (Turn 40903). Lead Pokemon is Gyarados Lv37. Repel should be active. Possible mechanic glitch or misunderstanding?
- **Anomaly Confirmed:** Encountered Level 16 Rattata on Turn 40908 despite using Max Repel on Turn 40903. Screen text confirmed usage. This suggests Repel might be malfunctioning or encounters on this specific tile/map behave oddly.
- **Anomaly #2:** Encountered Wild Raticate (Turn 40918) shortly after Rattata. Repel still ostensibly active. Confirms persistent issue with Repel in this area/session.