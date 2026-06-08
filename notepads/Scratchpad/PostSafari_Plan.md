# Post-Safari Zone Route & Progression Plan

## Historical Progress & Verification
- **Turn 73908**: Entered the real Warden's House (Map 0_155) at Fuchsia City (27, 27). Inside, the Warden is at (2, 3), and a pushable boulder is at (8, 4) blocking an item at (8, 3).
- **Turn 73918**: Talked to the Warden and delivered his Gold Teeth. Received **HM04 Strength**.
- **Turn 73929**: Taught HM04 Strength to ROCKY (GEODUDE) in our party.
- **Turn 73938**: Attempted to use ROCKY's STRENGTH field move from the Pokémon party menu while standing at (7, 4) in front of the boulder.
  - *Result*: The game displayed the text: "No! A new BADGE is required."
  - *Verification*: We currently possess 5 badges (Thunder Badge, Cascade Badge, Marsh Badge, Soul Badge, and Boulder Badge) but lack the Rainbow Badge. In Generation 1, the Rainbow Badge (obtained from Erika in Celadon City) is required to use Strength in the overworld.
  - *Conclusion*: We cannot push the boulder at (8, 4) yet. We must obtain the Rainbow Badge first.
- **Turns 74185-74198**: Challenged and defeated Erika at Celadon Gym, obtaining the **Rainbow Badge** and TM21 (Mega Drain).
- **Turns 74245-74267**: Successfully tested and documented Strength overworld boulder mechanics inside the Warden's House. Collected the blocked item at (8, 3), which was a **RARE CANDY**. Verified map transitions reset boulder positions and deactivate Strength.

## Next Target: Route 19, Route 20, and Cinnabar Island
- [x] **Locate Route 19 Entrance** (Completed Turn 74300)
- [x] **Use SURF on Route 19** (Completed Turn 74330)
- [ ] **Navigate to Seafoam Islands & Cinnabar Island**: Swim South along Route 19, then West along Route 20. Navigate through Seafoam Islands (Route 20) and continue West to Cinnabar Island.
- [ ] **Defeat Blaine**: Secure our 7th badge (Volcano Badge) at Cinnabar Gym.

## Water Routes & Seafoam Islands Strategic Plans (Turn 74313)
- **Water Combat Tactical Plan**:
  - *GEMMY (Level 59 BLASTOISE)*:
    - **BITE**: Physical Normal-type in Gen 1. Deals neutral, extremely high damage against Water-types. This is our primary, reliable "brute-force" sweeping move.
    - **DIG**: Physical Ground-type in Gen 1. Deals 2x super-effective damage against Poison/Water dual-types (e.g., Tentacool, Tentacruel), which are extremely common on these routes!
  - *SPARKY (Level 25 PIKACHU)*:
    - **THUNDERBOLT**: Electric-type special move. Deals 2x super-effective damage against all Water-types.
    - **THUNDER WAVE**: Useful for paralyzing faster or high-level wild Pokémon/trainers.
    - *Training Strategy*: Since water routes are packed with Swimmers and Water-types, this is the perfect opportunity to level up SPARKY. We can switch-train SPARKY or lead with him against trainers to net massive super-effective EXP, using GEMMY's physical BITE/DIG as a robust safety net.

- **Seafoam Islands Systematic Puzzle Tracking Pattern**:
  - We will create a dedicated notepad `Locations/SeafoamIslands` upon entry.
  - To prevent getting lost, disoriented, or accidentally resetting solved puzzle rooms, we will systematically track our state floor-by-floor (1F, B1F, B2F, B3F, B4F):
    1. **Coordinate Directory**: List the default coordinates of all pushable boulders and pits on each floor.
    2. **Active State Logs**: For each boulder, record its current position and whether it has been successfully pushed into a pit.
    3. **Reset Monitoring**: Note that leaving the Seafoam Islands map or fainting resets all boulders to their starting coordinates. We must strictly avoid leaving the cave once we begin a multi-floor boulder puzzle until it is completed.
- **Turn 74482**: Tested collision on Row 53 buoy barrier by pressing 'Down' from (17, 52). Walk failed (visited 0 tiles, position remained at (17, 52)). This confirms that the buoy wall on Row 53 is completely solid and impassable across Route 19.
- **Strategic Pivot**: Since Route 19 is blocked to the South, we will pivot to Route 21. We will use FLY to travel to Pallet Town, then use SURF on the water at the southern edge of Pallet Town to proceed south to Cinnabar Island.

## Cinnabar Gym Blaine Matchup Preparation Strategy
- **Opponent Profile**: Gym Leader Blaine utilizes a Fire-type lineup (typically Growlithe, Ponyta, Rapidash, Arcanine, all around Level 42-47).
- **Type Effectiveness**: Fire is weak to Water, Ground, and Rock (taking 2x damage).
- **GEMMY (Level 59 BLASTOISE) Offensive Plan**:
  - **Priority Move 1: SURF** (Water, Special, Power 95, 100% Accuracy).
    - *Calculation*: Benefitting from same-type attack bonus (STAB), base power becomes 142.5. Against Blaine's Fire-types, it deals 2x super-effective damage, yielding an effective base power of **285** with 100% accuracy.
    - *Utility*: This is our ultimate sweeping move. At Level 59, GEMMY's Special stat will guarantee a one-shot KO on every single member of Blaine's team, entirely eliminating combat RNG.
  - **Priority Move 2: HYDRO PUMP** (Water, Special, Power 120, 80% Accuracy).
    - *Utility*: While even more powerful (effective base power 360), its 80% accuracy introduces unnecessary miss risk. We will only use this if SURF PP is fully depleted.
  - **Priority Move 3: DIG** (Ground, Physical, Power 100, 100% Accuracy).
    - *Utility*: Ground is also 2x super-effective against Fire, but in Gen 1 DIG is a 2-turn move, giving opponents a turn to act or use status moves. SURF is infinitely more efficient.