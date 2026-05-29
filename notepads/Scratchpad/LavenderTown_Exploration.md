# Lavender Town Active Exploration & Mapping Log

## Socratic Mapping Protocol
To systematically discover, identify, and map Lavender Town's structures without blind movement:
1. **Perimeter and Grid Sweeping**:
   - We will systematically explore the town grid row-by-row and column-by-column starting from our entry point at (8, 0).
   - Any door or entrance we encounter will be treated as an unverified warp hypothesis.
2. **Identification Protocol**:
   - When we stand adjacent to a building door, we will document its external coordinates.
   - We will enter the building (warp) and record the internal Map ID.
   - We will speak to the NPCs inside to identify the building's function:
     - "Welcome to our POKéMON CENTER!" -> Pokémon Center.
     - "Welcome! May I help you?" -> Poké Mart.
     - Gravestones / channeled ghosts / channelers -> Pokémon Tower.
     - Mr. Fuji's associates / letters / orphans -> Volunteer House.
   - We will then exit and immediately place a highly descriptive map marker on the door (e.g. 🏥 for Poke Center, 🛒 for Poke Mart, 🗼 for Pokemon Tower, 🏠 for residential/houses).
3. **Pristine Record Integrity**:
   - All discoveries will be recorded in this scratchpad first with Turn numbers and Coordinates.
   - Once the town is fully mapped and verified, we will use `lavender_database_agent` to compress and migrate the final verified records to `Locations/LavenderTown`, keeping this scratchpad for active notes.

## Live Exploration Logs
- Turn 28826: Entered Lavender Town at (8, 0) from Route 10 South.
- Turn 28833: Standing at (8, 0) facing Down. Verified signpost at (9, 3). Planning to read the signpost.
- Turn 28846: Entered Pokémon Center door at (3, 5) on Map 0_4 (Lavender Town), warped to (3, 7) on Map 0_141.
- Turn 28849: Healed full party at the left counter tile (3, 3) facing Up.
- Turn 28853: Fully healed. Exiting Pokémon Center to place map marker and continue systematic exploration.
- Turn 28860: Entered Volunteer House (Map 0_149). Currently at (2, 7). Planning to check the NPC dialogue.
- Turn 28867: Standing at (4, 5). Spoke to NPC at (3, 5) who said "That's odd, MR.FUJI isn't here. Where'd he go?" Confirmed this is the Pokémon Volunteer House (Map 0_149).
- Path to girl NPC at (6, 3): From (4, 5), go Down to (4, 6), Right to (5, 6), Right to (6, 6), Up to (6, 5), and face Up to speak to her. Let's do this to catalog her dialogue.
- Turn 28875: Spoke to girl at (6, 3) who says "This is really MR.FUJI's house."
- Turn 28877: Spoke to Psyduck at (6, 4) who says "Gwappa!"
- Turn 28885: Spoke to Nidorino at (1, 3) who says "NIDORINO: Gaoo!"
- Turn 28887: Completed speaking to all NPCs in Map 0_149. Planning to exit through the door at (2, 7) / (3, 7).