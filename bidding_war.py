import random

def bidding_war():

    # 10 items with base prices
    items = [50, 80, 40, 100, 60, 90, 30, 70, 120, 20]

    # Agent budgets
    budgetA = 500
    budgetB = 500

    winsA = 0
    winsB = 0

    history = []

    print("\n--- BIDDING WAR AI ---\n")

    for i, price in enumerate(items, start=1):

        print(f"Item {i} | Base Price: {price}")

        # --------------------------
        # Agent A: Rule-based bidder
        # --------------------------
        if price > 80:                # expensive item → bid aggressively
            bidA = min(budgetA, price + random.randint(20, 60))
        elif price > 50:              # medium item
            bidA = min(budgetA, price + random.randint(5, 30))
        else:                          # cheap item → bid low
            bidA = min(budgetA, price + random.randint(0, 10))

        # --------------------------
        # Agent B: Random bidder
        # --------------------------
        bidB = random.randint(0, budgetB)

        print(f"Agent A Bid: {bidA}")
        print(f"Agent B Bid: {bidB}")

        # --------------------------
        # Decide winner
        # --------------------------
        if bidA > bidB:
            print("Winner: Agent A")
            winsA += 1
            budgetA -= bidA
            history.append((i, "A", bidA, bidB))
        elif bidB > bidA:
            print("Winner: Agent B")
            winsB += 1
            budgetB -= bidB
            history.append((i, "B", bidA, bidB))
        else:
            print("TIE - No one wins this item")
            history.append((i, "TIE", bidA, bidB))

        print(f"Remaining Budget -> A: {budgetA}, B: {budgetB}")
        print("-----------------------------------------\n")

    # --------------------------
    # Final summary
    # --------------------------
    print("\n--- BIDDING SUMMARY ---")
    print("Item | Winner | A_bid | B_bid")
    for h in history:
        print(f"{h[0]:>4} |  {h[1]:<6} |  {h[2]:<5} |  {h[3]}")

    print("\n--- FINAL RESULT ---")
    print(f"Agent A Items Won: {winsA}")
    print(f"Agent B Items Won: {winsB}")

    if winsA > winsB:
        print("Final Winner: Agent A 🏆")
    elif winsB > winsA:
        print("Final Winner: Agent B 🏆")
    else:
        print("DRAW 🤝")

bidding_war()
