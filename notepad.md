# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Current Status
- **Location**: New Bark Town (Map 24_4).
- **Goal**: Fly to Olivine City.
- **Current Action**: Manually navigating Fly menu to avoid cursor errors.
- **Plan**: Open Menu -> Select Pokemon -> Select Topaz -> Fly.

### Navigation Logic
- **Start Menu**: POKEDEX, POKEMON, PACK, POKEGEAR, STATUS, SAVE, OPTION, EXIT.
- **Cursor Memory**: Likely on SAVE. Needs verification.

### Recent Reflection
- **Progress**: Arrived in Cianwood, defeated Chuck, got Storm Badge and Fly.
- **Correction**: The Pharmacist dialogue loop confirms I need to trigger the "Jasmine sent me" flag.
- **Plan**: Fly to Olivine -> Climb Lighthouse -> Talk to Jasmine -> Return to Cianwood.
- **Strategy**: Exit Pharmacy -> Fly to Olivine -> Climb Lighthouse -> Talk to Jasmine.

### Lighthouse Navigation (For Return)
- **Route to Top**:
  1. **1F -> 2F**: Stairs at (3,11).
  2. **2F -> 3F**: Stairs at (5,3).
  3. **3F -> 4F**: Stairs at (13,3) (Right Side).
  4. **4F -> 3F (Center)**: Drop down hole at (9,3) to reach 3F Center.
  5. **3F (Center) -> 4F (Center)**: Stairs at (9,5).
  6. **4F (Center) -> 5F (Center)**: Stairs at (9,7).
  7. **5F (Center) -> 6F**: Stairs at (9,15).
- **Interrupt**: Phone call from Chad interrupted the Pharmacist interaction. Must finish call and retry.
- **Suspicion**: Validated. Pharmacist loop confirmed missing flag.
- **Observation**: The Fly map cursor seems to wrap around. Pressing 'Right' from Cianwood (West edge) sent me to New Bark Town (East edge).
- **Navigation**: Trying 'Left' x4 from New Bark Town to reach Olivine City.
- **Mechanic Note**: The Pokémon menu remembers the last cursor position. Re-entering it does NOT reset to Slot 1. Always verify cursor start position.
- **Correction**: Misinterpreted menu state in Turn 18999, causing accidental SURF attempt. Corrected by backing out and manually selecting Topaz.
- **Navigation Update**: Pressing 'Left' from New Bark Town had no effect. It seems the map does not wrap West from the start. Trying 'Right' to move East towards Cherrygrove.
- **Navigation Hypothesis**: The Fly map might be controlled by a list selection (Up/Down) rather than spatial movement (Left/Right), indicated by the red arrows on the UI. Testing 'Up'.