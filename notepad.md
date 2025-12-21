# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.

## Quest: Deliver Kenya (Route 31)
- **Status:** Recovery & Manual Entry.
- **Context:** Automated tool failed and saved game. Checking Kenya's mail status.
- **Objective:** Ensure mail reads exactly: "Dark Cave leads to another road." (Mixed case, period at end).
- **Action Plan:**
    1. Inspect current mail on Kenya.
    2. If incorrect/garbage: Remove mail -> Pack -> Give Flower Mail -> Type MANUALLY.
    3. If correct (unlikely): Deliver.

## Knowledge Base
- **Fisher (Route 31):** Rejected all previous attempts. Requires exact text matching.
- **Wade (Route 31):** Called (Turn 9576). Waiting on Route 31.
- **Dark Cave:** Connects Route 31, 45, 46. Needs Flash.

## Mechanics Log
- **Mail:** Prevents deposit. PC Full -> Mail goes to Bag. Must hold nothing to attach.
- **Inputs:** Pressing Start in Mail menu triggers Printer Error. Use B.
- **Lesson:** Pressing 'Start' in the Mail menu causes a "Printer Error" loop or crash behavior. Use 'B' to exit or 'END' to finish.
- **Menu Nav:** Cursor positions are remembered. Always verify position before confirming.
- **Automation Lesson:** Do not use "fire and forget" tools for complex, state-sensitive menus like Mail without extreme error checking.

## Critical Recovery Note
- **Turn 9804:** Save file overwritten during tool failure.
- **Current Task:** Manual verification of Kenya's held item.
## Mail Strategy
- Hypothesis: The Fisher requires the exact phrase "Dark Cave leads to another road." (Mixed Case, with period).
- Attempt 1 (All Caps): Failed.
- Attempt 2 (Current): Writing mixed case message.
- Mechanism: Mail must be written before giving? Or can be edited? If 'GIVE' creates blank mail, must 'TAKE' -> 'WRITE' -> 'GIVE' or 'USE' -> 'WRITE' -> 'GIVE'.
- Mail Menu: Start button causes Printer Error. Use B to cancel.
- Status: Delivery Failed. Fisher rejected the forged mail.
- Diagnosis: I likely deleted the original mail message when depositing Kenya in the PC. The current mail is generic/wrong.
- Solution: Fly to Goldenrod City, talk to Webster (North Gate Guard), and get the mail rewritten. Then return to deliver.
- Turn 9854: Approaching Wade at (21, 13) for a battle. Moving Right to engage.
- Turn 9855: Initiating interaction with Wade at (21, 13). Expecting a battle or gift since he called.
- Turn 9856: Wade interaction finished. No battle initiated. Likely just a chat call. Proceeding to Goldenrod to fix mail via Webster.
- Turn 9857: System blocked mixed input (Up, A). Only Up executed. Using slow_press to enter menu and select Mistral (Slot 4).
- Turn 9858: Previous input failed to navigate to Mistral (inputs likely eaten during menu transition). Currently on Muscle's menu. Correcting: B (Back), Down x3 (Mistral), A (Select).
- Turn 9859: Selected FLY. Next step: Navigate map to Goldenrod City.
- Hypothesis: Re-visiting Webster might reset the mail or let me copy the exact text again.
- Turn 9866: Fly map cursor still at Violet City (Left input failed). Trying DOWN to find Goldenrod.
- Map Connectivity Observations: 
  - Cherrygrove -> Left: Blocked/New Bark?
  - Cherrygrove -> Up: Violet.
  - Violet -> Left: Blocked?
- Quest Note: Fisher rejected "Dark Cave leads to another road." (Mixed case, period). Webster is the reliable fix.
- Turn 9867: Fly Map. Cursor behavior inconsistent (Header: Violet, Body: Cherrygrove). Assuming Cherrygrove or Violet.
- Strategy: Moving UP x2 to reach northern cities (Ecruteak/Mahogany). From there, navigate to Goldenrod.
- Previous failures: Violet -> Left (Blocked). Cherrygrove -> Left (Blocked).
- Turn 9869: Fly Map currently at Azalea Town.
- Observation: 'Up' input from Violet moved cursor to Azalea.
- Hypothesis: 'Up' navigates the list forward (Violet -> Azalea -> Goldenrod?).
- Action: Pressing 'Up' to target Goldenrod City.
- Turn 9870: Selected Goldenrod City on Fly map. Executing Fly.
- Next Step: Go to North Gate (Route 35 entrance) and talk to Webster to reset/fix the mail.
- Turn 9873: Arrived in Goldenrod Center via Fly. Party healthy. Exiting to find Webster at North Gate.
- Turn 9875: Path blocked by Cooltrainer F at (19, 27). Adjusting route to use column 18 (left side of road) to bypass. Destination: North Gatehouse (19, 1).
- Turn 9876: Received phone call from Wade (Bug Catcher). He is on Route 31 and wants a rematch. Ignoring for now to prioritize Mail fix.
- Resuming navigation to North Gatehouse to find Webster. Pathing via column 18 to avoid Cooltrainer.
- Turn 9878: Path blocked by Youngster at (19, 18). Shifting to column 18 to bypass him.
- Destination: North Gatehouse (19, 1).
- Turn 9879: Shifting back to column 19 (Right) to avoid Lass at (17, 10) who oscillates between 17 and 18.
- Path: Right to (19, 11), then Up to North Gate (19, 1).
- Turn 9880: Reached North Gate entrance at (19, 1). Entering to find Webster.
- Turn 9881: Moving Right -> Up to enter the Gatehouse at (19, 1). Previous attempt failed due to trying to move Up into a wall.
- Turn 9882: Inside Route 35 Gatehouse. Moving to (2, 4) to talk to Webster at the counter.
- Turn 9884: Webster didn't fix the mail (only generic dialogue).
- Hypothesis: Webster might restore the mail if Kenya is holding NOTHING.
- Plan: Take Mail from Kenya -> Talk to Webster. If that fails, the quest might be broken due to lost Sender data.
- Turn 9885: Opening Party Menu to remove Mail from Kenya.
- Reasoning: Webster only gave generic dialogue while Kenya was holding the mail. I need to make Kenya hold NOTHING to potentially trigger a "lost mail" recovery script.
- Turn 9886: Correcting menu navigation. Currently in Muscle's menu.
- Action: B (Exit), Down x4 (Select Kenya), A (Open Menu).
- Goal: Reach Kenya's menu to remove the mail.
- Turn 9887: In Kenya's menu. Selecting 'MAIL' option to remove the letter.
- Sequence: Down x3 -> A.
- Turn 9888: In Kenya's Mail Menu. Cursor on READ.
- Action: Selecting TAKE (Down, A) to remove the mail.
- Expectation: Prompt "Send removed MAIL to your PC?"
- Turn 9889: Selected 'NO' to "Send to PC?". Next prompt should be "Message will be lost. OK?".
- Plan: Confirm message loss, ensure Kenya holds nothing, then talk to Webster.
- Turn 9890: Confirmed "YES" to remove mail message. Kenya is now holding nothing (Mail moved to Bag).
- Next Step: Exit menu and talk to Webster to trigger lost mail dialogue.
- Turn 9891: Exiting menus (B, B) and interacting with Webster (Left, A).
- Context: Kenya is now empty-handed. Expecting Webster to notice the missing mail and offer a replacement.
- Turn 9895: Giving Flower Mail to Kenya.
- Expectation: "Made KENYA hold FLOWER MAIL" -> Keyboard.
- Next: Type "Dark Cave leads to another road" (No period).
- Hypothesis: Fisher rejected the previous mail because of the period.
- Turn 9897: Navigating to 'END' on keyboard.
- Path: Right x6 (to 'j' column), Down x5 (to bottom row), A.
- Objective: Confirm mail text "Dark Cave leads to another road" (No period).
- Turn 9899: Mail forged ("Dark Cave leads to another road", no period).
- Current State: Inside Pack (Key Items). Exiting to Start Menu -> Party to Fly.
- Goal: Fly to Violet City -> Route 31 -> Deliver to Fisher.
- Turn 9900: Selecting Mistral to Fly to Violet City.
- Current Cursor: Kenya (Slot 5). Target: Mistral (Slot 4).
- Action: Up -> A. Then will select Fly.
- Turn 9903: Attempted to Fly inside Gatehouse -> Failed ("Can't use that here").
- Plan: Exit Gatehouse (South), then Fly to Violet City.
- Turn 9906: Exiting Gatehouse (Right to warp).
- Next Action: Fly to Violet City from Goldenrod.
- Turn 9912: Fly Map Open at New Bark Town.
- Action: Navigating to Violet City. Path: Up, Left (to Cherrygrove), Up (to Violet).
- Sequence: slow_press ['Up', 'Left', 'Up'].
- Goal: Verify cursor is on Violet City, then Fly.