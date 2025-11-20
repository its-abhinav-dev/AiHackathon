# 🧠 Competitive Agents – AI Mini Hackathon  
### Complete Project Documentation (Extended Edition)

This README contains detailed explanations of **all 10 AI competitive simulations**, including:

- Algorithms used  
- Theory  
- Important explanations  
- Viva questions & answers  
- Step-by-step logic  
- ASCII diagrams of concepts  
- Simulation summaries  

This is the **exact documentation for your practical / viva submission**.

---

# 📌 **List of the 10 AI Problems Implemented**

1. Treasure Grab  
2. Capture the Flag  
3. Resource War  
4. Smart Snake AI Duel  
5. Grid Racing AI  
6. Market Trader Duel  
7. Predator–Prey Simulation  
8. Maze Domination  
9. Competitive Cleaner  
10. Bidding War AI  

Each section contains:

✔ Problem summary  
✔ Algorithm used  
✔ Techniques used  
✔ Explanation (from earlier messages)  
✔ Viva questions & answers  

---

---

# 🟦 **1. Treasure Grab**  
Two agents race to collect coins on a grid.  
Agents use **BFS to locate the nearest coin** each turn.

## ✔ Algorithm Used  
- **Breadth-First Search (BFS)**  
- BFS finds the **nearest coin** in an unweighted grid.

### Why BFS?
Because BFS guarantees shortest path in equal-cost grid environments.

### BFS Diagram (ASCII)
- Start → Explore neighbors → Expand layer-by-layer → Find first coin = nearest coin


## ✔ Concepts Explained Earlier
- Agents do **not block each other**  
- If both reach same coin: both get +1  
- Used **deepcopy()** so BFS uses the old grid state  
- Fixed scoring bug using old_grid instead of updated grid  
- Grid rebuilt every step to prevent overlapping bugs

## ✔ Viva Questions

**Q1: Why BFS?**  
A: BFS gives the shortest path in an unweighted grid, so it always finds the nearest coin.

**Q2: Why use deepcopy?**  
A: So scoring is checked on the old grid, avoiding race condition errors.

**Q3: What type of agent?**  
A: Goal-based agent using path-planning (BFS search).

**Q4: Why can both collect the same coin?**  
A: Both reach simultaneously → both get +1 because they arrived at the same step.

---

---

# 🟧 **2. Capture the Flag (A*)**

Two agents defend their flag while attacking the opponent.

## ✔ Algorithm Used  
- **A\* Pathfinding**

### Why A\*?
Because the grid contains **obstacles (#)** and A* uses:
- G = cost so far  
- H = Manhattan distance to goal  
- F = G+H (priority queue)  

### A* Diagram  
Start
├─ Explore cheapest F = G+H
├─ Avoid walls (#)
└─ Reach flag in optimal cost


## ✔ Key Concepts from Earlier Explanations
- Agents switch mode between **ATTACK** and **DEFEND**  
- Defense is triggered if enemy < 2 steps from flag  
- Path chosen using A*  
- Winner is the first to reach opponent’s flag  
- Logs maintained for each step  

## ✔ Viva Questions

**Q1: Why A* instead of BFS?**  
A: Because obstacles require optimal cost pathfinding.

**Q2: What is the heuristic used?**  
A: Manhattan distance.

**Q3: What happens if both reach flags?**  
A: The first capture event returns winner.

---

---

# 🟩 **3. Resource War (BFS + Random Spawn)**

Agents collect resources from a shared environment.

## ✔ Algorithm Used  
- **BFS to find nearest resource**  
- **Random resource spawning**

## ✔ Concepts Explained Earlier
- Once a resource is taken, it disappears  
- If both reach the same resource → both get point  
- Resources spawn every 3 steps  
- Grid updated after every movement  

## ✔ Viva Questions

**Q1: Why BFS?**  
A: To locate the nearest resource quickly.

**Q2: Why random spawning?**  
A: Introduces stochasticity and competitive unpredictability.

**Q3: What kind of environment?**  
A: Shared, non-cooperative multi-agent environment.

---

---

# 🟥 **4. Smart Snake AI Duel**

Two snakes compete to survive and collect food.

## ✔ Techniques Used  
- **Rule-based movement**  
- **Greedy heuristic towards food**  
- **Collision detection**  
- **Safe move filtering**  
- **Guaranteed winner logic**

## ✔ Concepts from Earlier Messages
- Snake chooses moves that avoid:
  - Walls  
  - Its own body  
  - Opponent’s body  
- If no move → snake dies  
- Tie broken using score  
- Full explanation included earlier  

## ✔ Viva Questions

**Q1: Why not BFS for snake?**  
A: Because we need quick decisions every step; greedy heuristic is faster.

**Q2: How do you avoid collisions?**  
A: Check if the next cell is inside bounds and not occupied.

**Q3: Why guaranteed winner logic?**  
A: To avoid both dying simultaneously.

---

---

# 🟨 **5. Grid Racing AI (A*)**

Agents race through obstacles to reach the goal.

## ✔ Algorithm Used  
- **A\* pathfinding**  
- Random obstacle generation

## ✔ Concepts Previously Explained
- Both A and B compute path using A*  
- Movement is done step-by-step  
- Time taken recorded  
- Winner is fastest to reach goal  

## ✔ Viva Questions  
**Q1: Why A* here?**  
A: Obstacles require shortest-cost search.

**Q2: What happens if path doesn’t exist?**  
A: That agent gets DNF (Did Not Finish).

---

---

# 🟪 **6. Market Trader Duel**

Two agents buy/sell stocks for profit.

## ✔ Techniques Used  
- **Basic Trading Logic**  
- **Heuristic: Momentum Strategy** (Agent A)  
- **Stochastic Random Strategy** (Agent B)  
- **Line Graph using Matplotlib**

## ✔ Concepts Previously Explained
- Price fluctuates randomly  
- Momentum: buy when rising, sell when falling  
- Mean reversion: buy when below average  
- Profit tracked every turn  

## ✔ Viva Questions  

**Q1: What type of agents?**  
A: Rule-based vs random agent.

**Q2: What environment?**  
A: Stochastic economic simulation.

**Q3: Why graph?**  
A: To visualize profit trend.

---

---

# 🟫 **7. Predator–Prey Simulation**

Predator moves randomly; prey uses smart escape.

## ✔ Techniques Used  
- **Random agent (predator)**  
- **Greedy maximizing distance (prey)**  
- **Oscillation avoidance**  

## ✔ Concepts Previously Explained
- Prey avoids going back to last position  
- If no better escape → fallback movement  
- Predator catches prey on same cell  

## ✔ Viva Questions  

**Q1: Why predator is random?**  
A: To simulate uncertainty.

**Q2: What algorithm used for prey?**  
A: Greedy maximization of Manhattan distance.

**Q3: Why avoid oscillation?**  
A: Otherwise prey moves back and forth endlessly.

---

---

# 🟦 **8. Maze Domination**

Agents expand territory each step.

## ✔ Techniques Used  
- **Grid expansion**  
- **Conflict resolution**  
- **Blocking cells (X)**  

## ✔ Concepts From Earlier Messages
- Both agents expand into neighbors simultaneously  
- If both target same cell → conflict → mark as X  
- Runs for fixed steps  
- Winner is agent with more cells  

## ✔ Viva Questions  
**Q1: Why conflict cell marked X?**  
A: Because both claim same cell, so no one gets it.

**Q2: Is this pathfinding?**  
A: No, it is territory growth simulation.

---

---

# 🟧 **9. Competitive Cleaner**

Agents clean dirty cells using BFS.

## ✔ Algorithm Used  
- **BFS to nearest dirt**  
- **One-step movement**  
- **Matplotlib leaderboard**  

## ✔ Concepts Previously Explained
- If both reach same cell → both get +1  
- Dirt removed only after scoring  
- Leaderboard uses bars or matplotlib  
- BFS ensures nearest dirt gets priority  

## ✔ Viva Questions  
**Q1: Why BFS?**  
A: To minimize time to nearest dirt.

**Q2: How scoring works?**  
A: Checked on original grid before update.

---

---

# 🟩 **10. Bidding War AI**

Agents compete for items with limited budget.

## ✔ Techniques Used  
- **Rule-based bidding (Agent A)**  
- **Random bidding (Agent B)**  
- **Auction simulation**  

## ✔ Concepts Previously Explained
- High-value items bid higher  
- Budgets updated after each win  
- History tracked per round  

## ✔ Viva Questions  
**Q1: What type of agent is Agent A?**  
A: Rule-based decision agent.

**Q2: Why randomness for Agent B?**  
A: To simulate unpredictable competitor.

**Q3: Is this a search problem?**  
A: No, it’s economic decision-making.

---

---

# 🧩 **How to Run All Simulations**

```bash
python treasure_grab.py
python capture_flag.py
python resource_war.py
python snake_duel.py
python grid_racing.py
python market_trader.py
python predator_prey.py
python maze_domination.py
python competitive_cleaner.py
python bidding_war.py
