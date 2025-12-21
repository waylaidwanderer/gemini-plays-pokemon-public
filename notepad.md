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
- Turn 9862: Fly map cursor at Cherrygrove City. Moving Left to target Violet City, then Goldenrod.
- Current Status: Traveling to Goldenrod to ask Webster to rewrite Kenya's mail.
- Quest Note: Fisher rejected "Dark Cave leads to another road." (Mixed case, period). Likely requires original flag or specific hidden byte, OR I messed up the text slightly. Webster is the reliable fix.