# Current Strategy: Resupply via Kanto Border
- **Timestamp:** Turn 26012 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Status:** Fly directly to Indigo Plateau failed (Map selection issue).
- **Immediate Goal:** Enter Kanto region via Route 27 to enable Kanto Fly map.
- **Plan:**
    1. Surf East from New Bark Town (Water at 18,6).
    2. Travel along Route 27 until the map registers as Kanto.
    3. Fly to Indigo Plateau.
    4. Buy 20 Full Restores, 20 Revives.
    5. Return to Mt. Silver for Red rematch.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.