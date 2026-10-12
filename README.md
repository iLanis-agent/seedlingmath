# Seedling math

Seeds for the plant list, the sowing countdown to the last frost, and batches that keep the harvest coming. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/seedlingmath/

## The three tools

- **Count plan** - `countPlan(plantsWanted, germinationPct)`: seeds to sow and spare seedlings.
- **Calendar plan** - `calendarPlan(daysUntilFrost, weeksBeforeFrost)`: the sowing countdown - ahead, on time or past the ideal.
- **Batch plan** - `batchPlan(totalPlants, windowWeeks, intervalWeeks)`: succession batches and plants per batch.

## Labeled norms (illustrative estimates, not rules)

- Labeled germination: 80% for fresh tomato seed, 65% for older packets. Labeled head starts: 6 weeks for tomatoes, 8 for peppers. The seed packet's own instructions and your last frost date win.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (12 cases, 48 checks)

Regenerate the oracle expectations: `python3 oracle.py`
