import random
import matplotlib.pyplot as plt

def market_trader_duel():

    capitalA = 1000
    capitalB = 1000

    inventoryA = 0
    inventoryB = 0

    price = 100  # starting price

    price_history = []
    profit_historyA = []
    profit_historyB = []

    print("\n--- MARKET TRADER DUEL ---\n")

    for step in range(1, 31):

        print(f"\nSTEP {step}")

        # Random market movement
        change = random.randint(-10, 12)
        prev_price = price
        price = max(10, price + change)

        price_history.append(price)
        print(f"Market Price: {price}")

        # ----------------------------
        # Agent A: Momentum Strategy
        # ----------------------------
        if price > prev_price:
            actionA = "BUY"
        elif price < prev_price:
            actionA = "SELL"
        else:
            actionA = "HOLD"

        # ----------------------------
        # Agent B: Mean Reversion
        # ----------------------------
        avg_price = sum(price_history) / len(price_history)

        if price < avg_price * 0.95:
            actionB = "BUY"
        elif price > avg_price * 1.05:
            actionB = "SELL"
        else:
            actionB = "HOLD"

        # -------------------
        # EXECUTE A's Action
        # -------------------
        if actionA == "BUY" and capitalA >= price:
            capitalA -= price
            inventoryA += 1
        elif actionA == "SELL" and inventoryA > 0:
            capitalA += price
            inventoryA -= 1

        # -------------------
        # EXECUTE B's Action
        # -------------------
        if actionB == "BUY" and capitalB >= price:
            capitalB -= price
            inventoryB += 1
        elif actionB == "SELL" and inventoryB > 0:
            capitalB += price
            inventoryB -= 1

        # Calculate profits
        profitA = capitalA + inventoryA * price
        profitB = capitalB + inventoryB * price

        profit_historyA.append(profitA)
        profit_historyB.append(profitB)

        print(f"Agent A: {actionA} | Capital={capitalA}, Inventory={inventoryA}, Profit={profitA}")
        print(f"Agent B: {actionB} | Capital={capitalB}, Inventory={inventoryB}, Profit={profitB}")

    # Winner
    print("\n--- FINAL RESULTS ---")
    print("Final Profit A:", profit_historyA[-1])
    print("Final Profit B:", profit_historyB[-1])

    if profit_historyA[-1] > profit_historyB[-1]:
        print("Winner: Agent A 🏆")
    elif profit_historyB[-1] > profit_historyA[-1]:
        print("Winner: Agent B 🏆")
    else:
        print("DRAW 🤝")

    # -----------------------
    # MATPLOTLIB GRAPH HERE
    # -----------------------
    plt.figure(figsize=(10,5))
    plt.plot(profit_historyA, label="Agent A Profit", linewidth=2)
    plt.plot(profit_historyB, label="Agent B Profit", linewidth=2)
    plt.xlabel("Step")
    plt.ylabel("Profit")
    plt.title("Market Trader Duel – Profit Chart")
    plt.legend()
    plt.grid(True)
    plt.show()


# Run simulation
market_trader_duel()
