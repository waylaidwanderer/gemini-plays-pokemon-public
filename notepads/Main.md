# Pokémon Blue Playthrough Dashboard

## Directory
- `Locations/PalletTown` - Permanently verified Pallet Town location records.
- `Locations/Route1` - Permanently verified Route 1 connections and layout features.
- `Locations/ViridianCity` - Permanently verified Viridian City connections and buildings.
- `Locations/PewterCity` - Permanently verified Pewter City location, gym, and connection records.
- `Locations/Route3` - Permanently verified Route 3 connections, pathing, and bidirectional ledge gaps.
- `Mechanics/General` - Verified game mechanics and controls.
- `Locations/SSAnne` - Verified S.S. Anne records, cabins, and trainers.

## Notepad Management Protocol (One-In, One-Out)
- To adhere to the 10 loaded notepad limit:
  1. Before loading a new region's notepad, audit current active notepads.
  2. If the loaded count is 9 or 10, identify completed/distant regions (e.g., SSAnne, VermilionCity) to unload.
  3. Execute `unload_notepads` to archive completed notepads before loading new ones.

## Active Progression Plan
- **Koga Defeated!** Obtained the Soul Badge. Overworld SURF is unlocked!
- **Erika Defeated!** Obtained the Rainbow Badge on Turn 74198. Overworld STRENGTH is unlocked!
- **Cinnabar Island Journey (Starts Turn 74291)**:
  - From Pallet Town, navigate South onto Route 21 water channel using GEMMY's SURF.
  - Surf South along Route 21, defeating Swimmers and Fishermen for experience.
  - Navigate directly to Cinnabar Island at the southern terminus of Route 21.
  - Retrieve the Secret Key from the Cinnabar Mansion (Pokémon Mansion) to unlock the Cinnabar Gym. See `Scratchpad/Mansion_B1F_Exploration` for B1F basement exploration records.
  - Defeat Gym Leader Blaine at Cinnabar Gym to secure the Volcano Badge.
  - Note: To reach B1F, we do NOT use Pit A at (11, 12) on 3F West as that drops us into an isolated pocket on 2F East South. Instead, we must use the 3F West North statue switch to toggle State A, walk through the open partition gap at (15, 5) to 3F East North, walk south to (16, 14), and fall through the giant pit there to land directly on 1F East Southeast at (16, 14), which has on-foot stairs down to B1F. Also note that on 3F West, Row 11 is permanently solid/impassable at Column 10 (Gate 2) under both State A and State B (Verified Turns 82928 & 89695), so we must navigate via the 3F West North upper corridor (Row 5/6) and the partition gap at (15, 5) to cross between the west and east sides. Also, note that on 1F East, the Northeast staircase at (27, 11) is permanently closed and impassable under both State A and State B (Verified Turns 92132 and 92164).