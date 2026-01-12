# Hall of Fame Entry
- **Achievement:** **CHAMPION OF THE JOHTO LEAGUE!**
- **Date:** Turn 33314
- **MVP:** Muscle (Machoke) Lv88.

# Roamer Hunt Log
- **Session Start:** Turn 34090.
- **Goal:** Catch Raikou/Entei.
- **Current Phase:** Transit to Ecruteak City.
- **Strategy:** Fly to Ecruteak -> Check Pokegear -> Hunt/Shuffle.

# Current Problem: Fly Map Navigation
- **Status:** Map Cursor at Fuchsia City (Kanto).
- **Goal:** Fly to Saffron City to take Magnet Train.
- **Navigation:** Pressing UP from Fuchsia should lead towards Saffron.
- **Plan:**
  1. Navigate Cursor to Saffron City.
  2. Fly to Saffron.
  3. Walk to Station -> Take Train -> Arrive Goldenrod.
  4. Fly to Ecruteak from Goldenrod.

# Lessons Learned
- **Menu Hygiene:** Visual confirmation is required before entering complex sequences.
- **Economics:** Super Repels > Max Repels.
- **Fly Mechanics:** 'Select' button toggles map regions in Gen 2. Indigo Plateau is the connection point.
- Fly Debugging (Turn 35679):
  - State Conflict: Screenshot shows Party Menu, but Screen Text says "Fly Map: Viridian City".
  - Analysis: Screen Text updated from Cinnabar to Viridian after inputs, so Map Logic is active. Screenshot is likely stale/glitched.
  - Current Location: Viridian City (Map Cursor).
  - Navigation Plan: Viridian -> Up (Pewter) -> Right (Cerulean) -> Down (Saffron).
  - Action: Up -> Right -> Down.
  - Goal: Land cursor on Saffron City. Verify via Text next turn.