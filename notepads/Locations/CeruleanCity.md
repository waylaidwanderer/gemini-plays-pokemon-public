# Cerulean City - Locations, Landmarks & Barriers

## Overworld Layout & Navigation
- **West Entrance (from Route 4):** Connects to the paved brick road of Cerulean City at x=0, y=19. (Verified at Turn 4062).
- **Anomalous Warp (19, 17):** Door at (19, 17) has a "POKé" sign outside but warps inside to a Jynx's/Melanie's House interior containing a bed and plants (No Nurse Joy).
- **Anomalous Warp (13, 15):** Door at (13, 15) has a Jynx's House outside but warps inside to a Jynx's House interior containing a PC and Jynx's husband/wife (rendered with a misleading Pokémon Center tileset, but has no Nurse Joy or healing function).
- **Bike Shop:** Large building directly south of (19, 17). Roof spans row 24 on columns 18-28. Front of the building is on row 25.
- **Cerulean Gym:** Large building located on the east side, north of the Mart. Sign reads "GYM" at (26, 18) / (27, 18).
- **Poké Mart:** Building located south of the Gym. Sign reads "MART" at (26, 24) / (27, 24) with entrance at (25, 25).
- **Route 24 Bridge (Nugget Bridge Path):** Accessible from the north-center area.
- **Goal:** Explore the rest of Cerulean City to find a functional Pokémon Center or healing counter, as the standard entrances are swapped/anomalous.

## Northern Bypass to Route 24
- **Passage barrier at Row 15:** Fences and roofs block vertical transit across row 15 across all columns in Cerulean City, including column 0 which is blocked by a cliff and water.
- **Route 4 Map Connection Bypass:** Because of the Gen 1 Map Connection Alignment Offset (Route 4 offset is -8), walking Left from Cerulean City at y=16 transitions to Route 4 at y=8 (completely bypassing the river barrier on Route 4 which is at y=16+). From there, walk Up to y=4, then Right to transition back to Cerulean City at y=12, which is completely north of the horizontal barrier!
- **Route 24 Entrance:** Paved brick road at columns 20-21 on rows 10-13 is completely clear and leads north directly onto Route 24.

## Systematic Warp Swap Hypothesis & Testing Plan (Turn 4606)
- **Observed Swaps:**
  - Outside Door (19, 17) (standard Pokemon Center door) warps to **Bill Fan's House** interior (contains Bill Fan NPC talking about Bill, a bed, and plants).
  - Outside Door (13, 15) (standard Jynx's House door) warps to **Jynx's House** interior (contains Jynx husband/wife, rendered with a misleading Pokemon Center tileset but has no healing function).
  - Outside Door (25, 25) (standard Poké Mart door) warps to **Jynx's House** interior too!
- **Hypothesis:**
  - The real **Cerulean Pokémon Center** is accessed from outside door **(19, 9)** (which is the standard Bill Fan's House door on the north side of the canal).
- **Systematic Testing Plan:**
  1. Exit current building to (19, 18) outside.
  2. Walk Left to (16, 18), then Up column 16 across the canal to (16, 12) (north side).
  3. Walk Right to (19, 12), then Up to (19, 9) and enter the door.
  4. Verify if inside is the functional Pokémon Center with Nurse Joy.
