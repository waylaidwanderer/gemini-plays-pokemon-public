# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher 1 step south to (19, 22). Attendant at (22, 18-19) is unreachable behind solid wall/turnstile structure.
- **Rugged Rocks (Sewers)**: (22, 10) and (10, 18) display "It's a rugged rock, but with some equipment, I could smash it." Field obstacle clearance requires specialized player equipment rather than traditional HM moves. Zero equipment currently in possession.

## Settled & Exhausted Inquiries
- **Sovio Sewers 100% Cleared**: Grunt 2 platform (18, 21-22), Western Terrace (cols 11-17, rows 11-12), Northern Gangway (row 5, cols 14-25), Eastern Storage Room platform (36-38, 12-14), column 23 vertical bridge, column 30 causeway, Dark Sector / Basement, Deep Subterranean room, Lower Eastern Walkway (cols 34-37, rows 28-32), and Southern Canal corridor (cols 10-22, rows 32-36). All grunts retreated on Turn 2682. Jackson is not present in the sewer corridors or storage room. No items, hidden triggers, or NPCs remain in Sovio Sewers. Sewers inquiry is permanently CLOSED.
- **Audited Domestic Buildings & Public Sector**: Karate House (14, 15), Gumball House (29, 14), North House (39, 7), Terrace House (49, 14), South Commercial Building (47-51, 20-22), Tan Building facade (32-37, 12), Bikers (13, 21-23), Rocky (24, 17), Metro lobby (cols 15-24). All confirmed static ambient entities.

## Active Hypotheses for Dad & Progression

### Hypothesis H12: Unvisited or Uninteracted Surface Triggers in Sovio City & Route 1
- **Premise**: Following Team Siara's retreat, Jackson was not found in the accessible sewer areas. Since Jackson is not inside the sewers or the Metro platform, the progression trigger must reside in an unfulfilled overworld requirement or an overlooked NPC interaction.
- **Sub-hypothesis H12b (Quest Engine / Side Quest Prerequisite)**:
  - In Pokémon Sors, the HuPhone tracks quests. Lost Pidgey and Lost Toy are completed.
  - Check whether starting/completing another side quest (or speaking to specific quest givers like the Camper with poisoned Weedle, or Professor Ivo, or the Fisherman) advances the world state or unlocks equipment.
- **Sub-hypothesis H12c (Re-checking Metro Platform Attendant & Exterior)**:
  - Examine the exact triggers in the Metro lobby and Central Plaza surrounding the station.

### Hypothesis H13: Unresolved Jackson Rescue in Sovio Sewers
- **Premise**: In Turn 1666-1707, Team Siara grunts held Jackson captive in a sewer storage room. The context summary for Turn 2279-2716 claimed Jackson was freed, but the physical game state continues to block the train turnstile ("I should find dad first!") and Route 2 ("I can't go yet... I have things to do!"). This discrepancy indicates Jackson was never actually rescued or the rescue sequence was never completed.
- **Test Coordinates**:
  1. Metro lobby (cols 18-19, row 25): Re-enter Sovio Sewers.
  2. Sewer storage room platform (cols 36-38, rows 12-14): Audit tile (37, 14) and surrounding platform for dropped keys, missed interaction triggers, or uncompleted event scripts.
  3. Grunt positions and pathways in Sovio Sewers.
- **Pass Criteria**: Locate Jackson, trigger a dialogue/cutscene advancing the rescue, or find an item/key that opens the storage room door.
- **Fail Criteria**: Platform and sewer entities remain static with no new interactions or items found.