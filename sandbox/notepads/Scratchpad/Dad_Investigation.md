# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Bounded by solid pillars at (18, 21) and (20, 21).
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor display: "It's a rugged rock, but with some equipment, I could smash it." Specialized equipment not yet in possession.

## Audited Areas & Physical Boundaries
- **Sovio Sewers**: Accessible open walkways and eastern storage platform (37, 14 simple storage room) audited. However, subterranean branches behind rugged rocks at (22, 10) and (10, 18) remain physically blocked and unexplored.
- **Sovio City**: Residential interiors (houses at 14, 15; 29, 14; 31, 26; 39, 7; 49, 14), Central Plaza, and Central Park NPCs provide baseline ambient flavor. Blonde Girl at (43, 25) directly verified ambient "catfished" dialogue (Turn 18492).
- **Lancio Town**: Professor Ivo's Lab accessible 1F audited (basement stairs at 12, 7 trigger "I probably shouldn't head down here..."). Harbor pier vacant.
- **System & Inventory (Hypotheses H43 & H44 Complete)**: Audited Turns 18456-18515. Bag pockets (Items, Key Items, TMs, Balls), HuPhone (Item Storage: Nugget x 1; Mailbox empty; World Map; Quest Log 25 entries), and Someone's PC Box 1 (completely empty) confirmed devoid of keys, off-party Pokémon, rock-smashing equipment, or unread progression mail. Surface facilities and menus exhausted.

## Active Hypotheses for Progression
### Hypothesis H45: Sovio Sewers Physical Obstacle & Subterranean Branch Investigation
- **Premise**: With all surface facilities and menus conclusively exhausted, the only unpassed boundaries in the accessible game world are the rugged rocks gating subterranean branches in the Sovio Sewers (Dark Sector at 22, 10 and Southwest Corridor at 10, 18). Investigation must focus on testing these physical obstacles, auditing adjacent tiles, and determining how clearance is achieved.
- **Immediate Plan**:
  1. Exit Pokémon Center PC and building.
  2. Travel to Sovio Metro Station and descend via red mat at (18-19, 25) into Sovio Sewers.
  3. Deploy subagent `sewer_transit` for autonomous traversal to target obstacles.