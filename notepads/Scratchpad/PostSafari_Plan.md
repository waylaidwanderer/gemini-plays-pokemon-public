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

## Cinnabar Island & Pokémon Mansion Prep Strategy (Turn 74754)
- **Inventory Cleanup Protocol**: Before entering Cinnabar Mansion, we must free up inventory space to accommodate the Secret Key and various TMs/items inside.
  - *Current bag slots*: 19/20 filled.
  - *Deposit Plan (at Cinnabar PC)*: Deposit HM03, HM04, TM06, TM21, TM40, CARBOS, RARE CANDY, and TOWN MAP. This will reduce our filled slots from 19 to 11, leaving 9 open slots for mansion items.
  - *HM Overworld Move Verification Protocol (Turn 74802)*: Before fully committing to depositing HM03/HM04, we must empirically verify whether overworld HM moves (specifically SURF) can still be executed if the physical HM item is stored in the PC.
    - **Step 1**: Reach Cinnabar Pokémon Center, access the PC, and deposit HM03 (SURF) and HM04 (STRENGTH).
    - **Step 2**: Exit the Pokémon Center, walk to the shoreline, and attempt to use BLASTOISE's SURF move from the POKéMON party menu.
    - **Step 3**: If SURF executes successfully and we can move onto water, the hypothesis is confirmed. We can safely keep the HMs in the PC to maximize our bag slots. If not, we must withdraw HM03/HM04 immediately. This prevents any risk of softlocks or being unable to leave the island.
- **PP & HP Management**:
  - Heal the party fully at the Cinnabar Pokémon Center to restore all HP and PP.
  - Keep 7 Hyper Potions and 1 Full Restore in our bag for mid-exploration healing.
  - Retain the ELIXER to restore GEMMY's PP if needed during the deep exploration.
- **Cinnabar Mart Purchase Priorities**:
  - Purchase 2-3 **Escape Ropes** (for instant exit after finding the Secret Key).
  - Purchase 5-10 **Full Heals** (to cure status effects from wild Koffing/Weezing/Grimmer).
  - Purchase **Ultra Balls** (for high-level wild encounters).

## HM Verification Test Live Log
- **Turns 74853-74876**: Reached Cinnabar PC and successfully deposited:
  - TOWN MAP (Turn 74857)
  - TM06 Toxic (Turn 74862)
  - CARBOS (Turn 74864)
  - HM04 STRENGTH (Turn 74867)
  - TM40 Rage (Turn 74870)
  - HM03 SURF (Turn 74872)
  - TM21 Mega Drain (Turn 74874)
  - RARE CANDY (Turn 74876)
- **Active Hypothesis**: HM03 SURF can still be executed from the Pokémon menu even if the physical HM03 item is in the PC.
- **Verification Plan**: Exit the Pokémon Center, walk to the water, and attempt to SURF using GEMMY (BLASTOISE) to verify if the move can be executed.
- **Turn 74893**: Verified SURF works in the overworld even if the physical HM03 (SURF) item is stored inside the PC. Standing at (11, 13) facing Down towards water, we successfully selected GEMMY (BLASTOISE) from the party menu and executed SURF. Entered water at (11, 14). This proves overworld HM moves can be executed without the physical HM item in our Bag.
- **Turn 74921**: Moved west along Row 13 to (6, 13) to explore the western side of Cinnabar Island. Opened the Start menu to initiate SURF onto the western vertical water channel at Column 5.
- **Turn 74922**: Discovered that the Pokémon Lab building on the south-west of the island has its entrance door at (6, 9), replacing our previous assumption of (3, 11) which is water.
- **Hypothesis**: The western vertical water channel (Columns 1-3) can be surfed Northwards to directly bypass the central buildings and reach the northern side of Cinnabar Island where Cinnabar Mansion and Cinnabar Gym are.