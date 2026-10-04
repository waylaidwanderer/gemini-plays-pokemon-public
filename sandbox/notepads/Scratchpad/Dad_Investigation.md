# Scratchpad: Post-Tremor Investigation & Progression Hypotheses

## Core Active Progression Barriers
- **Metro Turnstile (19, 21)**: Scripted barrier triggers verbatim "I should find dad first!" and forces Asher south to (19, 22). Gates train platform to Amor City.
- **Route 2 Eastern Exit (52, 19-22)**: Scripted barrier triggers verbatim "I can't go yet... I have things to do!" and forces Asher west.

## Distilled Physical Constraints & Verified Negative Facts
- **Metro Station Lobby**: Timetable, west seating, and scanner pillars are inert. Direct 'A' on turnstile from (19, 22) produces zero dialogue; barrier is strictly a walk-over tripwire on (19, 21).
- **Route 1**: All trainers (Duke, Sonia, Mike) and cottage resident have static pre-tremor dialogue.
- **Lancio Town**: Audited in post-sewer state (Turn 26052-26058); Professor Ivo repeats static starter inquiry, lab basement stairs remain restricted ("I probably shouldn't head down here..."), harbor pier has no boat.
- **Sovio City Exterior & Residents**: All residential interiors (Nana/granddaughter, elderly Wii man/son, Gumball family, Karate family/Machop, Name Rater) and outdoor NPCs (Bikers, Boy Rocky, Central Park dating couple, Jigglypuff family, Pokémon Center Camper/Boy) repeat static ambient dialogue.
- **Sovio Sewers**: Grunts retreated following Marie's radio directive; lower and upper corridors vacated. Eastern Storage Platform at (37, 14) has red downward arrow mat currently undergoing empirical entry testing under Hypothesis H9.
- **Sovio City Central Plaza Perimeter**: Stepped across all exterior plaza tiles (rows 14-16, columns 41-46) where the Siara confrontation occurred; confirmed 100% inert with zero active tripwires or story scripts.
- **HuPhone World Map**: Passive topological viewer; hovering displays location banners; START snaps to [X] (Close Map); button 'A' on location nodes is inert (no fast travel). Player location pin is dynamic.
- **Terrace Exterior**: Elevated terrace above Metro portal has no active NPCs or secret passages; manhole at (51, 16) is inert.

## Active Investigation
### Hypothesis H9: Sewer Storage Room Physical Collision & Entry Audit (Active)
- **Premise**: The red horizontal capsule mat with a downward arrow at (37, 14) in Sovio Sewers was labeled "impassable scenery fixture" based solely on reading the 'A' interaction text ("Its a simple storage room.."). In Pokémon Sors, all red arrow mats (Metro entrance at 18-19, 25; Dark Sector at 14-15, 9; building doors) function as warps entered by stepping DOWN off the mat into the adjacent tile. We must test whether walking South from (37, 14) into (37, 15) triggers a warp or encounters solid collision.
- **Test Protocol**:
  1. Enter Sovio Metro Station and descend via the red mat into Sovio Sewers.
  2. Navigate along catwalks to the Eastern Storage Platform (columns 36-38, rows 12-14).
  3. Stand at (37, 14) on the red mat and press Down to test if (37, 15) warps or collides.
  4. Test adjacent tiles (36, 14) and (38, 14).
- **Falsification Criteria**: If pressing Down from (37, 14) produces solid collision with 0 tile movement and no map transition occurs across all row 14 tiles, the storage room is conclusively confirmed as an impassable physical barrier.