# Strategic Status
- **Goal:** Catch Raikou (#243) & Entei (#244).
- **Session Start:** Turn 40947.
- **Current Strategy:** "Blind Gatehouse Shuffle" on Route 37.
    - Repel Trick: Lead Lv37 > Wilds (Lv ~20) but < Roamers (Lv 40).
    - Status: Max Repel Active.
    - Loop: Wiggle in grass -> Shuffle Ecruteak/Rt 37 -> Repeat.
- **Status:** Patrolling Route 37 Grass (Turn 41563). Repel Active.
- **Strategy:** Move to grass -> Wiggle. If no encounter, shuffle using `enter_ecruteak_from_route37` & `exit_ecruteak_to_route37`.
- **Observation:** Back on Route 37 at (8,0). Moving to grass manually.

# Mechanics
- **Roamers:** Move to an adjacent route when player transitions maps.
- **Repel:** Prevents encounters with wild Pokemon lower level than the lead.
- **Battle Cursor:** Remembers last move.
- **Gatehouses:** "Sticky" warps require moving *into* travel direction.

# Tile Mechanics
- **WARP_CARPET_RIGHT/LEFT:** Walk off map edge.
- **LEDGE_HOP:** One-way.
- **TALL_GRASS:** Encounters.