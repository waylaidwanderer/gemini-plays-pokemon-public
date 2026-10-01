# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Investigation Status & Active Hypotheses (Updated Turn 12481)
- **Verified Game State**:
  - Metro Turnstile at (19, 21): Displays "I should find dad first!" (Repels South).
  - Route 2 Exit at (52, 19-22): Displays "I can't go yet... I have things to do!" (Repels West).
  - Professor Ivo's Lab Stairs at (12, 7): Displays "I probably shouldn't head down here..."
  - Sovio Sewers Storage Room at (37, 14): Displays "Its a simple storage room..."
  - Active Quest: NONE (verified free for new side quests or event triggers).
  - *Core Fact*: Jackson remains MISSING following the seismic tremor (Turn 1437). Every primary progression gate confirms finding Jackson is mandatory to advance.

## Settled / Falsified Hypotheses (Condensed)
- **Hypothesis A (Karate House & Machop's Toy)**: Falsified Turn 12132. Residents and 2F audited 100% ambient flavor; cancelling quest cleared slot with no progression impact.
- **Hypothesis B (Sewers Storage Room)**: On hold. Room at (37, 14) currently inert ("Its a simple storage room...").
- **Hypothesis C (Surface NPCs with Unexamined Conditions)**: On hold pending new story triggers.
- **Hypothesis D (Northwest Clearing Rows 14-22)**: Traversed & Connected. Clearing extends east along row 10/13 connecting seamlessly to Bug Catcher Duke and the Eastern Highway (resolved via Hypothesis G).
- **Hypothesis E (HuPhone Menu Inspection)**: Falsified Turn 12410. Item Storage, Mailbox, Quest Log, and World Map verified empty/static; passive digital checks do not trigger story progression.
- **Hypothesis F (Cottage East Ledge Northbound)**: Falsified Turns 12444, 12455. Row 20 ledge strictly prevents northward traversal from Cottage yard (0 tiles visited on 3 Up inputs).
- **Hypothesis G (Route 1 Two-Way Connection)**: Verified Turn 12564. Confirmed two-way foot route between Lancio Town and Sovio City via row 10 meadow and Eastern Highway; documented in Locations/Route_1.md.



## Active Investigation: Jackson's Whereabouts & Progression Unlocks

### Sub-Hypothesis 1: Machop's Toy Quest -> Progression Unlock
- **Status**: Quest Accepted on Turn 12622 from Old Man at (51, 15).
- **Rationale**: Machop is associated with physical strength/rock manipulation. Sovio Sewers contains two cracked rock obstacles requiring HM Rock Smash (Dark Sector 22, 10 and Southwest corridor 10, 17). The Old Man stated the toy was lost in the sewers.
- **Immediate Plan**:
  1. Inspect the Quest Log entry for Machop's Toy to obtain developer hints.
  2. Search accessible sewer sectors (walkways, puddles) to locate the toy.
  3. Return toy to Old Man to test reward.
- **Explicit Falsification Criteria**:
  - If the quest awards an ordinary item (e.g. consumable, berry, Poké Doll, minor cash) and does NOT grant HM Rock Smash, a key/keycard, or open a story event flag, Sub-Hypothesis 1 is IMMEDIATELY FALSIFIED and closed without further search.

### Sub-Hypothesis 2: Sovio City Exterior Boundary Triggers
- **Status**: Secondary priority if Sub-Hypothesis 1 is falsified.
- **Rationale**: Jackson fled outside after the tremor (Turn 1437). Systematic perimeter check of exterior alleys and building boundaries.
- **Verified Facts**:
  - Metro Turnstile at (19, 21): strictly active ('I should find dad first!').
  - Route 2 Exit at (52, 19-22): strictly active ('I can't go yet... I have things to do!').
  - Sewers Storage Room at (37, 14): displays 'Its a simple storage room...' with south void collision. Zero evidence of a lock or voice.
