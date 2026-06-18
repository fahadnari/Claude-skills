"""
Portfolio Investment Agent
Analyzes your current holdings and suggests Vanguard/Fidelity ETFs based on your short-term goals.

Usage:
    python agent.py

Requirements:
    pip install anthropic
    export ANTHROPIC_API_KEY=your_key_here
"""

import anthropic
from anthropic import beta_tool
import json

client = anthropic.Anthropic()

# ── Tools ──────────────────────────────────────────────────────────────────────

@beta_tool
def analyze_portfolio(holdings: str) -> str:
    """Parse and analyze the user's current portfolio holdings.

    Args:
        holdings: Description of current holdings, e.g. "$10k in VTSAX, $5k in FXAIX, $2k cash"
    """
    # In a real app you'd parse brokerage exports; here we return the raw text
    # so Claude can reason about it alongside fund suggestions.
    return json.dumps({
        "raw_holdings": holdings,
        "note": "Holdings parsed. Claude will assess allocation gaps and risk profile."
    })


@beta_tool
def get_vanguard_etfs(category: str) -> str:
    """Return popular Vanguard ETFs for a given investment category.

    Args:
        category: One of: 'us_equity', 'international', 'bond', 'balanced',
                  'sector', 'dividend', 'money_market'
    """
    catalog = {
        "us_equity": [
            {"ticker": "VTI",  "name": "Vanguard Total Stock Market ETF",      "expense_ratio": "0.03%", "description": "Broad US market exposure"},
            {"ticker": "VOO",  "name": "Vanguard S&P 500 ETF",                  "expense_ratio": "0.03%", "description": "Large-cap US stocks (S&P 500)"},
            {"ticker": "VUG",  "name": "Vanguard Growth ETF",                   "expense_ratio": "0.04%", "description": "US large-cap growth stocks"},
            {"ticker": "VTV",  "name": "Vanguard Value ETF",                    "expense_ratio": "0.04%", "description": "US large-cap value stocks"},
        ],
        "international": [
            {"ticker": "VXUS", "name": "Vanguard Total International Stock ETF","expense_ratio": "0.07%", "description": "All non-US developed and emerging markets"},
            {"ticker": "VEA",  "name": "Vanguard FTSE Developed Markets ETF",   "expense_ratio": "0.05%", "description": "Developed markets ex-US"},
            {"ticker": "VWO",  "name": "Vanguard FTSE Emerging Markets ETF",    "expense_ratio": "0.08%", "description": "Emerging market equities"},
        ],
        "bond": [
            {"ticker": "BND",  "name": "Vanguard Total Bond Market ETF",        "expense_ratio": "0.03%", "description": "US investment-grade bonds"},
            {"ticker": "VGSH", "name": "Vanguard Short-Term Treasury ETF",      "expense_ratio": "0.04%", "description": "1-3 year US Treasuries — low risk"},
            {"ticker": "VTIP", "name": "Vanguard Short-Term Inflation-Protected ETF","expense_ratio": "0.04%", "description": "TIPS — inflation hedge"},
        ],
        "balanced": [
            {"ticker": "VBIAX","name": "Vanguard Balanced Index Fund",           "expense_ratio": "0.07%", "description": "60/40 stocks and bonds"},
            {"ticker": "LifeStrategy", "name": "Vanguard LifeStrategy Funds",   "expense_ratio": "0.11-0.14%", "description": "Pre-mixed 20/40/60/80% equity options"},
        ],
        "dividend": [
            {"ticker": "VYM",  "name": "Vanguard High Dividend Yield ETF",      "expense_ratio": "0.06%", "description": "High-yield US dividend stocks"},
            {"ticker": "VYMI", "name": "Vanguard International High Dividend Yield ETF","expense_ratio": "0.22%", "description": "International dividend stocks"},
        ],
        "money_market": [
            {"ticker": "VMFXX","name": "Vanguard Federal Money Market Fund",    "expense_ratio": "0.11%", "description": "Highly liquid, capital preservation"},
        ],
        "sector": [
            {"ticker": "VGT",  "name": "Vanguard Information Technology ETF",   "expense_ratio": "0.10%", "description": "US tech sector"},
            {"ticker": "VHT",  "name": "Vanguard Health Care ETF",              "expense_ratio": "0.10%", "description": "US healthcare sector"},
            {"ticker": "VNQ",  "name": "Vanguard Real Estate ETF",              "expense_ratio": "0.12%", "description": "US REITs"},
        ],
    }
    funds = catalog.get(category, [])
    if not funds:
        return json.dumps({"error": f"Unknown category '{category}'. Choose from: {list(catalog.keys())}"})
    return json.dumps({"category": category, "funds": funds})


@beta_tool
def get_fidelity_funds(category: str) -> str:
    """Return popular Fidelity ETFs and zero-fee index funds for a given category.

    Args:
        category: One of: 'us_equity', 'international', 'bond', 'sector', 'dividend', 'money_market'
    """
    catalog = {
        "us_equity": [
            {"ticker": "FZROX","name": "Fidelity ZERO Total Market Index Fund", "expense_ratio": "0.00%", "description": "Zero-fee total US market (Fidelity-only)"},
            {"ticker": "FSKAX","name": "Fidelity Total Market Index Fund",      "expense_ratio": "0.015%","description": "Total US stock market"},
            {"ticker": "FXAIX","name": "Fidelity 500 Index Fund",               "expense_ratio": "0.015%","description": "S&P 500 index — among lowest fees anywhere"},
            {"ticker": "FBGRX","name": "Fidelity Blue Chip Growth Fund",        "expense_ratio": "0.48%", "description": "Actively managed large-cap growth"},
        ],
        "international": [
            {"ticker": "FZILX","name": "Fidelity ZERO International Index Fund","expense_ratio": "0.00%", "description": "Zero-fee international (Fidelity-only)"},
            {"ticker": "FSPSX","name": "Fidelity International Index Fund",     "expense_ratio": "0.035%","description": "Developed markets ex-US"},
        ],
        "bond": [
            {"ticker": "FXNAX","name": "Fidelity U.S. Bond Index Fund",         "expense_ratio": "0.025%","description": "US investment-grade bonds"},
            {"ticker": "FBNDX","name": "Fidelity Investment Grade Bond Fund",   "expense_ratio": "0.45%", "description": "Actively managed bond fund"},
            {"ticker": "FUMBX","name": "Fidelity Short-Term Bond Fund",         "expense_ratio": "0.45%", "description": "Short-duration bonds — lower rate risk"},
        ],
        "money_market": [
            {"ticker": "SPAXX","name": "Fidelity Government Money Market Fund", "expense_ratio": "0.42%", "description": "Capital preservation, daily liquidity"},
            {"ticker": "FDRXX","name": "Fidelity Government Cash Reserves",     "expense_ratio": "0.37%", "description": "Ultra-safe cash equivalent"},
        ],
        "sector": [
            {"ticker": "FSELX","name": "Fidelity Select Semiconductors",        "expense_ratio": "0.70%", "description": "Chip stocks — high growth, high risk"},
            {"ticker": "FHLC", "name": "Fidelity MSCI Health Care ETF",         "expense_ratio": "0.08%", "description": "Healthcare sector"},
        ],
        "dividend": [
            {"ticker": "FDVV", "name": "Fidelity High Dividend ETF",            "expense_ratio": "0.15%", "description": "High-dividend US stocks"},
        ],
    }
    funds = catalog.get(category, [])
    if not funds:
        return json.dumps({"error": f"Unknown category '{category}'. Choose from: {list(catalog.keys())}"})
    return json.dumps({"category": category, "funds": funds})


@beta_tool
def calculate_allocation(
    goal_amount: float,
    current_savings: float,
    months_to_goal: int,
    risk_tolerance: str,
) -> str:
    """Calculate how much to invest monthly and what equity/bond split fits the goal.

    Args:
        goal_amount: Target dollar amount (e.g. 50000).
        current_savings: Current total portfolio value in dollars.
        months_to_goal: Number of months until you need the money.
        risk_tolerance: 'conservative', 'moderate', or 'aggressive'.
    """
    gap = max(goal_amount - current_savings, 0)
    monthly_needed = round(gap / months_to_goal, 2) if months_to_goal > 0 else 0

    # Simple rule-of-thumb allocation table
    profiles = {
        "conservative": {"equity": 30, "bond": 50, "cash": 20},
        "moderate":     {"equity": 60, "bond": 30, "cash": 10},
        "aggressive":   {"equity": 85, "bond": 10, "cash": 5},
    }
    allocation = profiles.get(risk_tolerance.lower(), profiles["moderate"])

    # Short time horizons shift toward safety
    if months_to_goal <= 12:
        allocation = {"equity": 20, "bond": 40, "cash": 40}
        note = "Short time horizon (<= 12 months): shifted to capital preservation."
    elif months_to_goal <= 24:
        allocation["cash"] = max(allocation["cash"], 15)
        note = "Medium-short horizon (12-24 months): increased cash cushion."
    else:
        note = f"Horizon of {months_to_goal} months supports {risk_tolerance} allocation."

    return json.dumps({
        "goal_amount": goal_amount,
        "current_savings": current_savings,
        "gap_to_fill": gap,
        "monthly_contribution_needed": monthly_needed,
        "suggested_allocation_pct": allocation,
        "note": note,
    })


# ── Main agent loop ────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are a personal investment advisor agent. Your job is to:
1. Understand the user's current portfolio and short-term financial goals.
2. Use your tools to fetch Vanguard and Fidelity fund options in relevant categories.
3. Calculate the required monthly savings and recommend a specific allocation.
4. Produce a clear, actionable investment plan naming specific tickers with rationale.

Always call analyze_portfolio first, then calculate_allocation, then fetch funds.
Be specific — name tickers, percentages, and dollar amounts. Keep your final recommendation concise.
Remind the user you are not a licensed financial advisor and they should verify with a professional."""


def run_agent(user_input: str) -> None:
    print("\n🤖 Portfolio Agent thinking...\n")

    runner = client.beta.messages.tool_runner(
        model="claude-opus-4-8",
        max_tokens=8192,
        thinking={"type": "adaptive"},
        system=SYSTEM_PROMPT,
        tools=[analyze_portfolio, get_vanguard_etfs, get_fidelity_funds, calculate_allocation],
        messages=[{"role": "user", "content": user_input}],
    )

    final_text = ""
    for message in runner:
        # Print tool calls as they happen so the user sees progress
        for block in message.content:
            if hasattr(block, "type") and block.type == "tool_use":
                print(f"  → Calling tool: {block.name}({json.dumps(block.input, separators=(',', ':'))})")
            elif hasattr(block, "type") and block.type == "text" and block.text:
                final_text = block.text

    print("\n" + "─" * 60)
    print(final_text)
    print("─" * 60 + "\n")


# ── Interactive CLI ────────────────────────────────────────────────────────────

EXAMPLE_PROMPT = """
My current portfolio:
- $15,000 in FXAIX (Fidelity S&P 500)
- $5,000 in BND (bond ETF)
- $3,000 in cash (savings account)
Total: ~$23,000

My short-term goal:
I want to save $40,000 for a house down payment in 18 months.
I'm 32 years old and my risk tolerance is moderate.

Please analyze my portfolio and suggest how I should invest to reach my goal,
using Vanguard and/or Fidelity funds.
"""

if __name__ == "__main__":
    print("=" * 60)
    print("  Portfolio Investment Agent")
    print("  Powered by Claude Opus 4.8")
    print("=" * 60)
    print("\nPaste your portfolio and goals below.")
    print("(Press Enter twice when done, or leave blank to use the example)\n")

    lines = []
    try:
        while True:
            line = input()
            if line == "" and lines and lines[-1] == "":
                break
            lines.append(line)
    except EOFError:
        pass

    user_input = "\n".join(lines).strip()
    if not user_input:
        print("Using example portfolio and goals...\n")
        user_input = EXAMPLE_PROMPT

    run_agent(user_input)
