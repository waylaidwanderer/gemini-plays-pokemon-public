# Strategic Status
- **Goal:** Catch Raikou (#243) & Entei (#244).
- **Session Start:** Turn 40947.
- **Current Strategy:** "Blind Gatehouse Shuffle" on Route 37.
    - Repel Trick: Lead Lv37 > Wilds (Lv ~20) but < Roamers (Lv 40).
    - Status: Max Repel Active.
    - Loop: Wiggle in grass -> Shuffle Ecruteak/Rt 37 -> Repeat.
- **Status:** Optimization & Shuffle (Turn 41611).
- **Strategy:** Define `check_route37_grass` -> Exit Ecruteak -> Use new tool if at (8,0).
- **Observation:** Created tool to automate grass check. Resuming shuffle.

# Mechanics
- **Roamers:** Move to an adjacent route when player transitions maps.
- **Repel:** Prevents encounters with wild Pokemon lower level than the lead.
- **Battle Cursor:** Remembers last move.
- **Gatehouses:** "Sticky" warps require moving *into* travel direction.

# Tile Mechanics
- **WARP_CARPET_RIGHT/LEFT:** Walk off map edge.
- **LEDGE_HOP:** One-way.
- **TALL_GRASS:** Encounters.