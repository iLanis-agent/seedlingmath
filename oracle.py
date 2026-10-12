import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))

def count_plan(plantsWanted, germinationPct):
    if not (plantsWanted > 0) or not (germinationPct > 0) or not (germinationPct <= 100):
        return {"error": "plants and germination rate must be positive, rate at most 100"}
    seeds = math.ceil(plantsWanted * 100 / germinationPct)
    return {"seeds": seeds, "spare": seeds - plantsWanted}

def calendar_plan(daysUntilFrost, weeksBeforeFrost):
    if not (daysUntilFrost >= 0) or not (weeksBeforeFrost > 0):
        return {"error": "days until frost and weeks before must be positive"}
    return {"sowIn": daysUntilFrost - weeksBeforeFrost * 7}

def batch_plan(totalPlants, windowWeeks, intervalWeeks):
    if not (totalPlants > 0) or not (windowWeeks > 0) or not (intervalWeeks > 0):
        return {"error": "plants, window and interval must be positive"}
    batches = math.ceil(windowWeeks / intervalWeeks)
    return {"batches": batches, "perBatch": math.ceil(totalPlants / batches)}

def render_count(r, plantsWanted, germinationPct):
    return ("For " + plural(plantsWanted, "plant") + " at a labeled " + fmt(germinationPct) + "% germination: sow "
            + plural(r["seeds"], "seed") + ", one a cell - " + plural(r["spare"], "spare seedling") + " to thin or give away.")

def render_calendar(r, daysUntilFrost, weeksBeforeFrost):
    head = "With " + plural(daysUntilFrost, "day") + " to the last frost and a labeled " + fmt(weeksBeforeFrost) + "-week head start: "
    if r["sowIn"] > 0: return head + "sow in " + plural(r["sowIn"], "day") + "."
    if r["sowIn"] == 0: return head + "sow this week."
    return head + plural(-r["sowIn"], "day") + " past the ideal - sow today and pick a faster variety."

def render_batch(r, totalPlants, windowWeeks, intervalWeeks):
    return (plural(totalPlants, "plant") + " across " + fmt(windowWeeks) + " weeks of harvest at " + fmt(intervalWeeks)
            + "-week intervals: " + plural(r["batches"], "batch", "batches") + " of " + plural(r["perBatch"], "plant") + ".")

cases = []
for a in [(24, 80), (50, 65), (12, 90), (0, 80)]:
    r = count_plan(*a)
    cases.append({"fn": "countPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_count(r, *a)})
for a in [(42, 6), (60, 6), (21, 8), (-1, 6)]:
    r = calendar_plan(*a)
    cases.append({"fn": "calendarPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_calendar(r, *a)})
for a in [(24, 12, 2), (30, 10, 2), (40, 8, 2), (0, 12, 2)]:
    r = batch_plan(*a)
    cases.append({"fn": "batchPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_batch(r, *a)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
