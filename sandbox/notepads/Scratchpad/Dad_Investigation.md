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

## Concluded Hypotheses
### Hypothesis H45: Sovio Sewers Physical Obstacles (Concluded Turn 18563)
- **Outcome**: Verified both southwest rock (10, 18) and Dark Sector rock (22, 10) require specialized equipment. Perimeter bounds transferred to Locations/Sovio_Sewers. Subterranean exploration gated until equipment obtained.

### Hypothesis H46: Commercial Building Roof Corridor Audit (Concluded Turn 18703)
- **Outcome**: Audited rows 20-22 across columns 47-51 beneath commercial building roof canopy. Confirmed row 23 is solid south wall; rows 20-22 form a continuous covered passageway terminating east at column 52 with the Route 2 story barrier ("I can't go yet... I have things to do!"). Zero interactive doors, switches, or hidden triggers exist beneath the roof canopy.

### Hypothesis H47: Metro Station Lobby Systematic Tile & Boundary Audit (Concluded Turn 18818)
- **Outcome**: Systematically stepped on all lobby floor coordinates across rows 22-25, columns 18-24. Probed west waiting chairs at (17, 22-24) (inert), west pillar at (18, 21) (inert), east pillar at (20, 21) (inert), and timetable at (21-23, 23) (flavor text). Turnstile at (19, 21) strictly triggers 'I should find dad first!'. Zero hidden triggers, items, or switches exist in the Metro lobby.

## Active Hypotheses for Progression
### Hypothesis H48: Regional Transit & Overworld Event Trigger Audit
- **Premise**: With sewers, Metro lobby, and town buildings audited, the departure blocker ('I should find dad first!') requires an external event trigger. We hypothesize Dad's whereabouts or the story progression flag is located along the Route 1 / Lancio Town regional axis or requires a specific overworld trigger.
- **Immediate Plan**:
  1. Exit Metro Station to Central Plaza (48, 18).
  2. Re-examine Central Plaza and Route 1 connection for story advancement triggers.