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
- Fly Debugging (Turn 35687):
  - Current Location: Indigo Plateau (according to text).
  - Hypothesis: `Right` from Indigo is blocked.
  - Reset Strategy: Close Map (B) -> Open Map (A). Since player is at Cinnabar Island, cursor will reset to Cinnabar.
  - Probe: From Cinnabar, test `Right`.
  - Goal: Determine if Cinnabar -> Right leads to Fuchsia City.
  - If Fuchsia: Next step `Up` to Saffron.
  - If Indigo: Map wraps. Plan B: Fly to Pewter/Viridian and walk.