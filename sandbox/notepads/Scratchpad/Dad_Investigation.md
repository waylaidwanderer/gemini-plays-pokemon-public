# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher 1 step south to (19, 22). Attendant at (22, 18-19) is unreachable behind solid wall/turnstile structure.
- **Rugged Rocks (Sewers)**: (22, 10) and (10, 18) display "It's a rugged rock, but with some equipment, I could smash it." Field obstacle clearance requires specialized player equipment rather than traditional HM moves. Zero equipment currently in possession.

## Settled & Exhausted Inquiries
- **Sovio Sewers 100% Cleared**: Grunt 2 platform (18, 21-22), Western Terrace (cols 11-17, rows 11-12), Northern Gangway (row 5, cols 14-25), Eastern Storage Room platform (36-38, 12-14), column 23 vertical bridge, column 30 causeway, Dark Sector / Basement, Deep Subterranean room, Lower Eastern Walkway (cols 34-37, rows 28-32), and Southern Canal corridor (cols 10-22, rows 32-36). All grunts retreated on Turn 2682. Jackson is not present in the sewer corridors or storage room. No items, hidden triggers, or NPCs remain in Sovio Sewers. Sewers inquiry is permanently CLOSED.
- **Audited Domestic Buildings & Public Sector**: Karate House (14, 15), Gumball House (29, 14), North House (39, 7), Terrace House (49, 14), South Commercial Building (47-51, 20-22), Tan Building facade (32-37, 12), Bikers (13, 21-23), Rocky (24, 17), Metro lobby (cols 15-24). All confirmed static ambient entities.

## Active Hypotheses for Dad & Progression

### Hypothesis H14: Unexamined Mechanics & Attendant Interaction within Sovio City
- **Premise**: The turnstile ("I should find dad first!") and Route 2 barrier ("I can't go yet... I have things to do!") explicitly indicate unresolved tasks within Sovio City. Past assumptions that the Metro attendant at (22, 19) is 'unreachable' conflated walking collision with interaction capability. In subway stations, attendants are spoken to across counters. Testing direct 'A' interaction across the counter at columns 21-22 evaluates whether ticket issuance, dialogue, or story triggers exist.
- **Target Coordinates & Results**:
  1. Sovio Metro Station turnstile (19, 21): Confirmed locked by "I should find dad first!" with 1-tile downward pushback.
  2. Route 2 entrance barrier (52, 19): Confirmed locked by "I can't go yet... I have things to do!" with 1-tile leftward pushback to (51, 19).
  3. Metro Station Attendant: Visually verified present on platform side at (22, 19) in blue uniform. However, physically unreachable from lobby side across brick wall and blocked turnstile ('I should find dad first!').
  4. Sovio City Triggers & Investigation: Systematically probe unexamined tiles, script triggers, and objects in Sovio City to locate Jackson and resolve the progression block.
- **Pass Criteria**: Locate Jackson, trigger a cutscene/dialogue, or clear the turnstile/Route 2 barrier.
- **Fail Criteria**: Target entities remain non-interactable without state changes.