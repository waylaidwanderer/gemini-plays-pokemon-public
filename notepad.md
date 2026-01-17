# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026 at 5:08 PM PST

### Current Objectives & Strategy
- **Main Quest**: Begin the Gym Challenge (Violet City).
- **Immediate Goal**: Reach Cherrygrove City.
- **Healing**: Mom (New Bark) does NOT heal. Elm did NOT heal. Relied on Berries.
- **Status**: Party HP Critical. Need Pokemon Center.

### Route 29 Navigation
- **Finding**: 
  - Upper Lanes (Row 6-9) Westbound blocked by Ledge/Tree walls (x=43, x=45).
  - Middle Lane (Row 10-12) Westbound blocked by Cut Tree (x=21).
  - Lower Lane (Row 14) Westbound leads to Dead End (x=13).
- **Solution**: 
  1. Loop back East on Lower Lane (Row 14/16) to New Bark Town entrance.
  2. Go North to Row 6 (Upper Lane) from the far East side (x=50+).
  3. Traverse Upper Lane West to Cherrygrove.

### Tile Mechanics
- **TYPE_c453**: One-Way Ledge (East/South depending on context).
- **TYPE_2889**: Tree Wall (Solid).
- **TYPE_5519**: Cut Tree (Requires HM01).

### Key Locations
- **Cherrygrove City**: Pokemon Center, Mart.
- **Route 30**: Path to Violet City.

### Mechanics
- **Ledges**: Jump South (usually). Or East? Route 29 has specific directional ledges?
- **Cut Trees**: Require Badge 2 + HM01.
- Aide in New Bark Town (after Lab) gives Pokegear tutorial, NOT Potions.
- Confirmed: Must travel to Cherrygrove to heal.
### Route 29 Lane Analysis
- **Top Lane (Rows 4-9)**: Blocked by Cut Tree at (30, 9)? Needs verification.
- **Middle Lane (Rows 10-12)**: Blocked by Cut Tree at (21, 11).
- **Bottom Lane (Rows 14-17)**: Currently testing. Suspect Dead End at x=13.
- **Hypothesis**: If all lanes are blocked, there must be a diagonal switch or a specific gap I missed. 
- **Immediate Task**: Verify collision of 'TYPE_2889' (Tree texture) at (20, 16). If solid, x=0-12 on Row 14 is likely a wall.