# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher 1 step south to (19, 22). Attendant at (22, 18-19) is unreachable behind solid wall/turnstile structure.
- **Rugged Rocks (Sewers)**: (22, 10) and (10, 18) display "It's a rugged rock, but with some equipment, I could smash it." Field obstacle clearance requires specialized player equipment rather than traditional HM moves. Zero equipment currently in possession.

## Settled & Exhausted Inquiries
- **Sovio Sewers 100% Cleared**: Grunt 2 platform (18, 21-22), Western Terrace (cols 11-17, rows 11-12), Northern Gangway (row 5, cols 14-25), Eastern Storage Room platform (36-38, 12-14), column 23 vertical bridge, column 30 causeway, Dark Sector / Basement, Deep Subterranean room, Lower Eastern Walkway (cols 34-37, rows 28-32), and Southern Canal corridor (cols 10-22, rows 32-36). All grunts retreated on Turn 2682. Jackson is not present in the sewer corridors or storage room. No items, hidden triggers, or NPCs remain in Sovio Sewers. Sewers inquiry is permanently CLOSED.
- **Audited Domestic Buildings & Public Sector**: Karate House (14, 15), Gumball House (29, 14), North House (39, 7), Terrace House (49, 14), South Commercial Building (47-51, 20-22), Tan Building facade (32-37, 12), Bikers (13, 21-23), Rocky (24, 17), Metro lobby (cols 15-24), Pokémon Center PC (12, 1), and Central Park pond curb (39, 16). All confirmed static ambient entities.

## Active Hypotheses for Dad & Progression

### Hypothesis H21: Terrace Deck East Boundary & Signpost Bypass Audit
- **Premise**: In Sovio City, the east exit to Route 2 was documented as blocked at rows 19-22 ("I can't go yet... I have things to do!"). Directly north of the Route 2 road, tile (51, 17) is an open walkable tile behind the wooden signpost at (50-51, 18). While building collision was documented at (52, 15-16), the boundary at (52, 17) and (52, 18) directly behind the signpost has never been probed for collision, passage, or script triggers.
- **Target Coordinates**: Elevated terrace deck at (51, 17). Face East and test movement / interaction against (52, 17).
- **Pass Criteria**: Detect a walkable path to Route 2, a script trigger, or a hidden item behind the signpost.
- **Fail Criteria**: (52, 17) is solid obstacle/building collision with no interactive trigger.