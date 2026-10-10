# Abandoned Undersea Team Siara Laboratory (Location 3)

## Elevator Mechanics (`6, 15`)
- **Floor Selector (`5F, 4F, 3F, 2F, 1F`)**: Stepping into any elevator doorway (`5, 4` on `1F`, `36, 5` on `2F`) warps to `(6, 15)` inside the elevator and automatically opens the 5-floor menu (cursor defaults to `5F`).
  - Selecting a valid unlocked floor plays a ~5500ms elevator ride animation and **automatically warps Asher out of the elevator** onto the destination floor (verified Turns 34386-34388).
  - **Floor Access**:
    - `1F`: Entrance Stairwell (`5, 5`; connects south at `5, 15` to the Location 3 Cave Passage `28, 8`).
    - `2F`: Unlocked initially; warps to `(36, 6)` (verified Turn 34388).
    - `5F`: Displays *"UNAUTHORIZED PERSONEL / EC CARD IS REQUIRED"* until the **EC Card** is obtained (verified Turn 34385).

## Floor 2F (`36, 6` Elevator Exit)
- **Elevator Lobby (`33-38, 5-10`)**:
  - **Elevator Doorway (`36, 5`)**: Enters the elevator (`6, 15`).
  - **Locked Northern Security Door (`30-31, 6`)**: Unlocked using **Code Red (`0203`)** obtained from the B2F Southern Area console at `(36, 16)` (automatically steps Asher inside to `30, 5`; contains an **Eclite Shard** at `30, 4`, collected Turn 34431).
  - **Professor Ivo's HuPhone Briefing (`37, 6`, Turns 34389-34391)**:
    - Stepping onto `(37, 6)` triggers a HuPhone call from **Professor Ivo**, who explains that while the elevator is running on a backup generator, everything else in the facility is offline because the **main generator** is not running.
    - Because the security doors cannot be opened without power, Asher must **find the generator room and turn the main generator back on**.
    - Ivo also warns Asher that the abandoned laboratory is crawling with **Eclipsed Pokémon**.
  - **Purple Wall Plaque (`38, 5`)**: Reads *"B2F / Lobby"* (confirming `1F–5F` on the elevator panel correspond to subterranean undersea levels `B1F–B5F`, verified Turn 34391).
  - **Wild Eclipsed Pokémon Encounters**:
    - Floor tiles inside the Abandoned Undersea Laboratory can trigger wild **Eclipsed Pokémon** encounters (such as **Eclipsed Pikachu**♀ Lv40, which knows `Eclipse Zap`) even while a Repel / Super Repel is active (verified Turn 34393).
    - Wild Eclipsed Pokémon can be fled from normally via `Run` (*"Got away safely!"*, verified Turn 34396) or targeted with Poké Balls (verified Turn 34395).
  - **Western Corridor (`23-33, 8-9`)**:
    - **Purple Wall Plaque (`27, 7`)**: Reads *"Doors are password protected! / If you forgot the code for a door, find the computer displaying it."* (verified Turn 34398).
    - **Bookshelves (`23-26, 7-8`)**: Located along the northern wall.
    - **Purple Door Mat (`25, 9` <-> Western Stairwell Room `6, 7`)**: Stepping `Down` off `(25, 9)` warps into the **B2F Western Stairwell & Computer Room** at `(6, 7)` (doorway exit at `6, 6`; features a descending staircase with a red mat at the southwest corner and a computer/server station along the northern wall, verified Turn 34400).
  - **Southern Corridor (`34-35, 10-13+`)**: Extends south past the yellow crates at `(36, 12-13)`.
## B2F Western Stairwell & Computer Room (`6, 7` from B2F Lobby `25, 9`)
- **Doorway Exit (`6, 6`)**: Warps back to B2F Lobby at `(25, 9)`.
- **Northern Wall (`cols 8-13, rows 8-9`)**: Bookshelves at `(8-9, 8-9)` and `(13+, 8-9)`, blue computer desk at `(10-11, 8-9)`, and server tower at `(12, 8-9)`.
- **Cracked Floor Shadow (`5-7, 8-10`)**: 3x3 circular shadow centered on `(6, 9)` between the northern doorway (`6, 7`) and the southern floor (`row 10+`); `(7, 9)` has solid collision (verified Turn 34403).
- **Descending Staircase (`2-3, 10-11`)**: Accessed via the red mat at `(4, 11)`.
  - **Northern Computer Terminal (`10-11, 8-9`)**: Decorative wall terminal (`row 10` is completely walkable from `5, 10` to `10, 10`; verified Turn 34405).
  - **Blue Control Console (`13, 12`)**: Located on the eastern table below `(13, 11)`; displays *"Code Blue / Location: B3F Code: 0405"* and grants **Code Blue** (verified Turn 34454; triggers wild Lv40 **Eclipsed Quagsire** on floor tiles, verified Turn 34452).
  - **Staircase Warp (`3, 11` <-> B3F `12, 11`)**: Stepping onto `(3, 11)` from the red mat `(4, 11)` descends to **B3F** at `(12, 11)` (verified Turn 34406).

## Floor B3F (Western Stairwell Entry at `12, 11`)
- **Ascending Staircase (`13-14, 11`)**: Accessed via the red mat at `(12, 11)`; returns to the B2F Western Stairwell & Computer Room (`4, 11`).
- **Western Security Door (`3-4, 9-10`) & Descending Staircase (`2, 5`)**:
  - Approaching from the south along `row 11` (`12, 11 -> 4, 11`), step onto the walkable bottom half `(4, 10)` facing `(4, 9)` and press `A` to unlock the door with **Code Blue (`0405`)**, which automatically steps Asher through to `(4, 8)` (verified Turn 34454).
  - **Descending Staircase (`2, 5` via Red Mat `3, 5-6`)**: Descends from the B3F northwest corridor to the **B4F Western Corridor**.
- **Northern Elevator & Floor Plaque (`9, 5` & `11, 5`)**:
  - **Elevator Doorway (`9, 5`)**: Connects to the facility elevator (`6, 15`).
  - **Purple Wall Plaque (`11, 5`)**: Reads *"B3F / Machine Room"* (verified Turn 34409).
- **Southern Corridor (`cols 8-10, rows 11-19`)**:
  - Floor hole at `(10, 15)` (`col 9` is completely clear from `9, 6` to `9, 19`).
  - **Purple Door Mat (`9, 19` <-> B3F Machine Room `29, 4`)**: Stepping `Down` off `(9, 19)` enters the **B3F Machine Room** at `(29, 4)` (verified Turn 34411).
- **Eastern Branch (`cols 11-17, rows 15-19`)**:
  - **Purple Wall Plaque (`12, 17`)**: Reads *"V Generator Room V"* (verified Turn 34422).
  - **Ascending Staircase (`17, 18` via Red Mat `16, 18-19`)**: Ascends to the **B2F Southern Area** at `(30, 16)` (verified Turn 34423).

## B2F Southern Area (`30, 16` from B3F Eastern Staircase `17, 18` & B2F Lobby `34-35, 10-13`)
- **Descending Staircase (`28-29, 16-17` via Red Mat `30, 16-17`)**: Descends to the B3F Eastern Branch at `(16, 18)`.
- **Objects & Consoles**:
  - **Marie's Diary (`34, 18`)**: Dated *"2011. April 5th"*: *"This is it! I have finally set up the entire Laboratory. Here I'll fully develop out Eclipsing, so that Jackson will believe that it's safe. Can you believe he left with our 5 year old son?! I can't mess this up. If I prove this is completely safe we can be a family again..."* (verified Turns 34426-34429).
  - **Blue Control Console (`36, 16`)**: Displays *"Code Red / Location: B2F Code: 0203"* and grants **Code Red** to unlock the B2F northern security door (`30-31, 6`) (verified Turn 34429).
  - **Item (`38, 16`)**: **Full Restore** located in the eastern alcove behind the yellow crates at `(37, 15-16)` and `(38, 17-18)` (collected Turn 34429).

## B3F Machine Room (`29, 4` from B3F Corridor `9, 19`)
- **Doorway Exit (`29, 3`)**: Warps back to the B3F Corridor at `(9, 19)`.
- **Wild Eclipsed Pokémon**: Floor tiles trigger Lv40 wild Eclipsed Pokémon such as **Eclipsed Solrock** (verified Turn 34413).
- **Main Generator Switch (`29, 12`)**:
  - Reached via the western passage (`28, 4 -> 28, 7 -> 27, 7 -> 27, 13 -> 29, 13`).
  - Interacting with `(29, 12)` from `(29, 13)` flips the switch from red/blue to solid blue and restores main power to the facility (verified Turn 34415).
  - Immediately triggers a HuPhone call from **Professor Ivo**, who confirms power is restored, reports that the third energy signal is on the lowest floor (**B5F**, which requires an **Ec Card**), and warns Asher that something is approaching—triggering a scripted ambush by a wild **Lv40 Eclipsed Golem** at `(29, 13)` (OHKO'd by Sirius's `Aura Sphere` for `1011 EXP`, verified Turns 34415-34420).
- **Item**: **Ultra Ball** at `(32, 14)` in the southeast corner (collected Turn 34420).
## Floor B4F (`23, 6` Elevator Exit)
- **Elevator & Floor Plaque (`23, 5` & `25, 5`)**:
  - **Elevator Doorway (`23, 5`)**: Connects to the facility elevator (`6, 15`; exiting steps to `23, 7`).
  - **Purple Wall Plaque (`25, 5`)**: Reads *"B4F / Community Room"* (verified Turn 34435).
- **B4F Community Room (`cols 20-36, rows 6-18`)**:
  - **Wild Eclipsed Pokémon**: Floor tiles trigger Lv40 wild Eclipsed Pokémon such as **Eclipsed Gengar** (verified Turn 34440).
  - **Locked Security Door (`21-22, 17-18`)**: Password-protected security door in the southwest corridor. **2-Tile-Tall Security Door Mechanic**: For all 2-tile-tall vertical security doors (`30-31, 5-6` on B2F, `3-4, 9-10` on B3F, `21-22, 17-18` and `14-15, 15-16` on B4F), the top row (`row 17`) is a walkable overlap tile while the bottom row (`row 18`) is the solid interactive door tile; when approaching from the north, step onto the top half (`21, 17`) facing `Down` toward `(21, 18)` and press `A` to unlock it with **Code Green: `1115`** (verified Turn 34447).
  - **Marie's 2013 Diary (`30, 15`)**: Dated *"2013. September 1st"*: *"I adopted the little boy from two years ago and named him Frio. / I have also made a groundbreaking discovery because of him! / The gem he always kept with himself seemed to calm Eclipsed Pokémon down... / Normally they are really violent, but the gem caused them to be controlable. / The test subjects still can't be kept outside of tubes but we found out the reason. / The process is tied to a material called 'Eclite'. / We tried using chemicals similar to the components of Eclite. / However due to Eclite's unique origin, it's not possible with Earth elements... / We need Eclite to continue on... A lot of it!"* (verified Turns 34437-34438).
  - **Blue Control Console (`30, 17`)**: Displays *"Code Green / Location: B4F Code: 1115"* and grants **Code Green** (verified Turn 34442).
  - **Marie's 2014 Diary (`31, 17`)**: Dated *"2014. October 31st"*: *"I found out more of the origin of Eclipsing... / Apparently Frio is part of an Eclipser family... / A bloodline of people having the abillity to use Eclite as a way to channel their spirit and Eclipse Pokémon without technology. / I must train him here now! / I managed to make a test subject which doesn't require life sustaining equipment... / I can start training Frio's Eclipser power to get the full potential of the Eclite!"* (verified Turns 34442-34443).
  - **Item (`36, 15`)**: **Revive** located in the eastern alcove below `(36, 14)` (collected Turn 34443).
- **B4F Western Corridor & Storage Room (`13, 9` from B3F Staircase `2, 4`)**:
  - **Ascending Staircase (`11-12, 9-10` via Red Mat `13, 9-10`)**: Returns to B3F at `(3, 4)`.
  - **Locked Security Door (`14-15, 15-16`)**: Unlocked from `(15, 15)` facing `Down` toward `(15, 16)` using **Code Green (`1115`)**, stepping Asher into the room at `(15, 17)` (verified Turn 34457; triggers wild Lv40 **Eclipsed Excadrill** on floor tiles, verified Turn 34459).
  - **Blue Control Console (`17, 17`)**: Located above `(17, 18)`; displays *"Code Yellow / Location: B4F Code: 0420"* and grants **Code Yellow** (verified Turn 34458).
  - **Key Item (`11, 18`)**: **Ec Card** sitting on the broken table (interacted with from `12, 18` facing `Left` via `col 12` around the floor-hole ring at `13-15, 17-19`; collected Turn 34460).
  - **Marie's 2015–2016 Diary (`13, 20`)**: Dated *"2015. June 6th"* and *"2016. April 5th"*: *"2015. June 6th / I managed to make a quick and cheap way of Eclipsing Pokémon! / I also created a special band for Frio that he can use to Eclipse Pokémon, helping his training. / ... / ... / 2016. April 5th / This is bad! This is bad! / Eclipse Pokémon have gone berserk all over the Laboratory! / We can't control all of them... / We need to leave immediately and seal this lab away!"* (verified Turn 34461).
  - **Purple Wall Plaque (`9, 16`)**: Reads *"Number of failed experiments: 405 / Number of successful experiments: 1"* (verified Turn 34463).
- **B4F Ailing Room (`cols 16-38, rows 19-28`, behind Code Yellow Door `21-22, 17-18`)**:
  - Unlocked from `(21, 17)` facing `Down` toward `(21, 18)` using **Code Yellow (`0420`)**, stepping Asher into the corridor at `(21, 19)` (verified Turn 34466).
  - **Purple Wall Plaque (`28, 25`)**: Reads *"Ailing room"* (verified Turn 34470).