(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }

  function countPlan(plantsWanted, germinationPct) {
    if (!(plantsWanted > 0) || !(germinationPct > 0) || !(germinationPct <= 100)) return { error: "plants and germination rate must be positive, rate at most 100" };
    var seeds = Math.ceil(plantsWanted * 100 / germinationPct);
    var spare = seeds - plantsWanted;
    return { seeds: seeds, spare: spare };
  }

  function calendarPlan(daysUntilFrost, weeksBeforeFrost) {
    if (!(daysUntilFrost >= 0) || !(weeksBeforeFrost > 0)) return { error: "days until frost and weeks before must be positive" };
    var sowIn = daysUntilFrost - weeksBeforeFrost * 7;
    return { sowIn: sowIn };
  }

  function batchPlan(totalPlants, windowWeeks, intervalWeeks) {
    if (!(totalPlants > 0) || !(windowWeeks > 0) || !(intervalWeeks > 0)) return { error: "plants, window and interval must be positive" };
    var batches = Math.ceil(windowWeeks / intervalWeeks);
    var perBatch = Math.ceil(totalPlants / batches);
    return { batches: batches, perBatch: perBatch };
  }

  function renderCount(r, plantsWanted, germinationPct) {
    return "For " + plural(plantsWanted, "plant") + " at a labeled " + germinationPct + "% germination: sow " + plural(r.seeds, "seed") + ", one a cell - " + plural(r.spare, "spare seedling") + " to thin or give away.";
  }

  function renderCalendar(r, daysUntilFrost, weeksBeforeFrost) {
    if (r.sowIn > 0) return "With " + plural(daysUntilFrost, "day") + " to the last frost and a labeled " + weeksBeforeFrost + "-week head start: sow in " + plural(r.sowIn, "day") + ".";
    if (r.sowIn === 0) return "With " + plural(daysUntilFrost, "day") + " to the last frost and a labeled " + weeksBeforeFrost + "-week head start: sow this week.";
    return "With " + plural(daysUntilFrost, "day") + " to the last frost and a labeled " + weeksBeforeFrost + "-week head start: " + plural(-r.sowIn, "day") + " past the ideal - sow today and pick a faster variety.";
  }

  function renderBatch(r, totalPlants, windowWeeks, intervalWeeks) {
    return plural(totalPlants, "plant") + " across " + windowWeeks + " weeks of harvest at " + intervalWeeks + "-week intervals: " + plural(r.batches, "batch", "batches") + " of " + plural(r.perBatch, "plant") + ".";
  }

  var api = { countPlan: countPlan, calendarPlan: calendarPlan, batchPlan: batchPlan, renderCount: renderCount, renderCalendar: renderCalendar, renderBatch: renderBatch };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.SeedlingMath = api;
})(this);
