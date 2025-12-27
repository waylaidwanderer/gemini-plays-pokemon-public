# Kanto Campaign Status
- **Location:** Indigo Plateau (Route 23).
- **Objective:** Fly to Cerulean City to bypass Route 9 obstacles.

# Strategic Goals
1. **Restore Power:**
   - Investigate Power Plant (East of Cerulean, end of Route 9).
   - Fix the Generator (likely requires a part).
2. **Wake Snorlax:**
   - Requires Poke Flute functionality.
   - Requires Power restored.
3. **Collect Kanto Badges:**
   - [x] Vermilion (Thunder)
   - [x] Saffron (Marsh)
   - [ ] Cerulean (Cascade)
   - [ ] Celadon (Rainbow)
   - [ ] Fuchsia (Soul)
   - [ ] Pewter (Boulder)
   - [ ] Viridian (Earth)
   - [ ] Cinnabar (Volcano)

# Active Quests & Leads
- **Bill's Grandpa (Route 25):** Wants to see a Lickitung. Reward: Everstone.
- **Power Plant:** Located at the end of Route 9.
- **Copycat Girl (Saffron):** Missing doll.

# Discovery Log
- **Cerulean City:**
  - Gym located at (30, 23).
  - Cooltrainer M mentions trainers at Cerulean Cape (Route 25).
- **Saffron City:**
  - Magnet Train station exists but no power.
- **Route 9:**
  - Land route (x=20-41) is a trap/dead end due to impassable ledges/walls.
  - Must access Power Plant via water (Surf from Route 24/25).

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a WALL from the North. Cannot be jumped. (Confirmed Route 9).

# Active Plans
- **Escape to Cerulean:**
  - **Status:** Fly Map Open. Cursor on Saffron City.
  - **Action:** Pressing 'Up' to select Cerulean City (North of Saffron).
  - **Execution:** Up -> A (Fly).
  - **Next:** Land in Cerulean -> Heal -> Route 24 -> Surf to Power Plant.
- **Restore Power Route:**
  - Fly to Cerulean -> Heal -> Route 24 -> Surf South-East -> Power Plant.
- Navigation Error: Mistook Overworld movement for Fly Map navigation.
- Result: Walked back inside Indigo Plateau Center.
- Action: Exiting Center (Down) to retry Fly sequence from scratch.
- Lesson: Verify menu state visually before inputting directional commands.