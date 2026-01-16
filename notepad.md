# Strategic Status
- **Goal:** Catch Raikou (#243) & Entei (#244).
- **Session Start:** Turn 40947.
- **Current Strategy:** "Blind Gatehouse Shuffle" on Route 37.
    - Repel Trick: Lead Lv37 > Wilds (Lv ~20) but < Roamers (Lv 40).
    - Status: Max Repel Active.
    - Loop: Wiggle in grass -> Shuffle Ecruteak/Rt 37 -> Repeat.
- **Status:** Resuming Patrol (Turn 41543). Call Finished.
- **Strategy:** Wiggle in grass using `patrol_area`. If no encounter, use `enter_ecruteak_from_route37` tool.
- **Observation:** Resuming hunt after interruption. Repel Active.

# Mechanics
- **Roamers:** Move to an adjacent route when player transitions maps.
- **Repel:** Prevents encounters with wild Pokemon lower level than the lead.
- **Battle Cursor:** Remembers last move.
- **Gatehouses:** "Sticky" warps require moving *into* travel direction.

# Tile Mechanics
- **WARP_CARPET_RIGHT/LEFT:** Walk off map edge.
- **LEDGE_HOP:** One-way.
- **TALL_GRASS:** Encounters.