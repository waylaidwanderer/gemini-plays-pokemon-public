# Strategic Objectives
- **Primary:** Challenge the Pokémon League.
- **Secondary:** Defeat the Elite Four.
- **Tertiary:** Train team.

# Current Status
- **Location:** Will's Room (Elite Four).
- **Party:** Healthy. Muscle (Lv61) leading.
- **Inventory:** 6 Hyper Potions, 10 Revives, 2 Full Restores.
- **Money:** Low (¥589).

# Exploration Log
- **Victory Road:** Fully traversed.
- **Indigo Plateau:** Lobby explored. Shopping done.

# Plan
1.  **Battle:** Talk to Will and win.
    - **Strategy:** Muscle (Lv61) spams Strength.
    - **Reasoning:** Strength (Normal) is neutral vs all his dual-Psychic types (Flying, Ice, Grass, Water). Cross Chop (Fighting) is resisted by Psychic and Flying, making it poor vs Xatu, Exeggutor, Slowbro.
    - **Matchup:** Muscle outlevels by ~20 levels. Expect OHKOs.
2.  **Next:** Advance to Koga's room.

# Battle Log
- **Vs Will:**
  - **Xatu:** Defeated.
  - **Jynx:** Current opponent.
    - **Situation:** We are in a heal loop. Healing puts us at 205, Jynx hits us down to ~111.
    - **Game State Logic:** HP is 111/205. The "Recovered 94 HP" text is on screen, but the game has already calculated the *next* hit from Jynx.
    - **Trajectory:** Once text clears, Jynx attacks. We end up at 111 HP.
    - **Decision:** We MUST attack next turn. We can survive one hit (111 HP > ~94 Dmg). Healing again is futile.
    - **Action:** Advance text. Next turn: STRENGTH.