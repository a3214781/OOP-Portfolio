# Week 2 Code Review
**Date:** Monday, 9 August
**Reviewed with:** Lance
**Reviewed:** `__str__` and `__repr__` methods across Transaction, Client, Account, and Branch

**Question:** What's the actual difference between `__str__` and `__repr__`, and why does a class need both instead of just one?

**Answer:** `__str__` controls what `print(obj)` shows — it's meant to be readable, for a person looking at output. `__repr__` controls what the programmer wants to see on the backend and its meant to be unambiguous, showing the object's internal state whereas the `__str__` shows what the user wants/needs to see, not all information.

**Why it mattered:** Every class in the project implements both methods, so it was worth confirming I had the distinction right rather than just copying the pattern without understanding it. Getting it backwards would mean debug-style output ending up in `__str__` or plain-English output ending up in `__repr__`, which defeats the point of having both.

**Resulting development:** I checked my `__repr__` implementations against this distinction and confirmed they follow the convention of naming the class and every constructor argument, e.g.:
```python
def __repr__(self):
    return (f"Transaction: identifier={self.__identifier}, "
            f"transaction_type={self.__transaction_type}, amount={self.__amount}, "
            f"desc={self.__desc}, status={self.__status}")
```
This confirmed `__str__` and `__repr__` weren't accidentally duplicating the same output — `__str__` reads as a sentence, `__repr__` reads as a labelled dump of internal state.

---

# Week 3 Code Review
**Date:** Thursday, 20 August
**Reviewed with:** Lance
**Reviewed:** `isinstance()` validation across all four class constructors and setters

**Question:** At what point does validation become over-engineering? Using password/username rules as a comparison (minimum length, character requirements, duplicate checks) — how much validation is actually necessary before it's just adding checks because more validation is technically possible?

**Answer:** Validation should match what the current task actually requires — type checks and sensible fallback values to protect object state, not exhaustive input filtering. Rules like enforcing exact email formats via regex, minimum age limits, or strict phone number formats go beyond what's been asked for at this stage, and adding them just because they're possible is solving a problem the project doesn't have yet.

**Why it mattered:** This connects directly to Task 3's validation requirements, which ask for `isinstance()` checks and reasonable fallback values, not production-grade input filtering. It's easy to keep layering on rules without them adding real value at this stage of the project.

**Resulting development:** I reviewed my existing validation — e.g. the `Client` email check is just `isinstance(email, str) and "@" in email`, not a full email-format regex — and decided this was the right level for the brief rather than something to "harden" further. This reinforced a KISS-style principle for the design review: match validation complexity to what's actually required, not to what's theoretically possible.