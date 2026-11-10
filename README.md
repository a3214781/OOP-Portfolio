# Week 2 Code Review
**Date:** Monday, 9 August
**Reviewed with:** Lance
**Reviewed:** All classes (Transaction, Client, Account, and Branch) were reviewed throughout this code review, particularly looking at the outputs for select functions in each class.

**Question:** What's the difference between `__str__` and `__repr__`, and why does a class need both instead of just one?

**Answer:** 
`__str__` is used for users and is designed to be user friendly and readable output, whereas, `__repr__` is used by programmers and is designed for backend development, being unambiguous, and showing objects internal states. This is a difference of wants and needs for users and developers.

**Why it mattered:**
This is important as getting this backwards would mean debugging output ending up in `__str__` and plain english ending up in `__repr__`, defeating the point of both and result in poor usability on the user side and development on the programmers side. 

**Resulting development:** I updated all `__repr__` to be unambiguous and show clear outputs fro each variable. an example of this is here in the transaction class: 
```python
def __repr__(self):
    return (
        f"Transaction: identifier={self.__identifier}, "
        f"transaction_type={self.__transaction_type}, amount={self.__amount}, "
        f"desc={self.__desc}, status={self.__status}"
    )
```

**Improvements** This improved the comprehensiveness of the `__repr__` as well as giving me a better understanding of the usefulness of `__repr__()` functions compared to `__str__` for future projects.
---

# Week 3 Code Review
**Date:** Thursday, 20 August
**Reviewed with:** Lance
**Reviewed:** The entire project was reviewed throughout this code review, in particular `isinstance()` validation across all four class constructors was looked into and feedback was given.

**Question:** 
At what point does validation become over-filtering? for example using password/username rules as a comparison (minimum length, character requirements, duplicate checks) — how much validation is actually necessary before it's just adding checks because more validation is technically possible?

**Answer:** 
Validations should match what is required, type checks and else statements are usually essential in projects and should be the default. rules such as enforcing specific email formats, minimum age limits, or strict phone number formats go beyond what is needed and are unnecessary. Adding rules like these just because they are possible is solving problems that never needed to be solved.

**Why it mattered:** 
This directly connects to our portfolio where it asks us to add validation to all constructors and getters in the project using `isinstance()` checks and reasonable fallback methods.

**Resulting development:**
After this feedback all `isinstance()` methods where reviewed and fixed, for example the `Client` email check is just `isinstance(email, str) and "@" in email`, not a full email-format.

**Improvements** This has improved the filtering and over engineering of the project, resulting in a more refined code and filtering process as well as a better understanding of the usefulness of `isinstance()` in future projects.
---

## Design Review — Workshop 3-2
**Design concerns:**
- One duplicate responsibility I noticed was the use of:
    ```python
        if isinstance(identifier, int) and not isinstance(identifier, bool) and VARIABLE > 0:
    ```
  where this filtering is repeated across multiple constructors and multiple classes. This is a form of duplicated responsibility where each class is resolving the same problems.

**SOLID (SRP):**
- The Client class is currently doing arguably more than 1 job. it currently is responsible for representing a clients identity, holding their lists of accounts (which could be done in a separate class) and tracking preferences such as preferred branch. For now this is ok although as the project develops this could be messier and cause problems.
- The Account, Transaction, and Branch class are currently satisfying SRP reasonably well, with each one having a single, clear, responsibility with clear methods.


**What's working well:**
- the encapsulation and validation that was applied to all classes is consistent and protects its private attributes and validates parameters uniformly, so all invalid data can't infiltrate the system  

**What might need reconsidering later:**
- The validation logic, although working well, is duplicated across all four classes. In future iterations all classes can use a uniform filtering system rather than each class re-implementing the same isinstance() checks independently.


 # Week 4 Code Review
**Date:** Monday, August 31
**Reviewed with:** Lance
**Reviewed:** Inventory (`collect_resource`, `resource_requirements`, `spend_resource`) and SummoningRitual (`__init__`, `can_perform`, `consume_resources`)

**Question:** Why does ectoplasm need to be checked first, before the other resources and before the if/else checks, and should the code be ordered that way?

**Answer:** Ectoplasm needs to be checked first, as it is essential for everything, including the if/else checks. Every ritual costs at least 1 ectoplasm (`ectoplasm_cost` defaults to 1), so a summon can never succeed without it.

**Why it mattered:** Ectoplasm is needed for every ritual, so it should be the first thing the code should look at and be part of every check for resources.

**Resulting development:** In `Inventory.collect_resource` in inventory.py, I moved `ectoplasm` to the first parameter, so the parameter is now `collect_resource(self, ectoplasm, necrotic=0, spirit=0, bone=0, flesh=0)`.

**Improvements:** Ectoplasm is now listed first in the code that collects resources, which makes its importance clear to anyone reading it.


# Week 5 Code Review
**Date:** Monday, September 7
**Reviewed with:** Lance
**Reviewed:** Inventory, along with the `isinstance()` checks in all projects.

**Question:** What should I do with the repeated `isinstance` checks, is there a way to simplify them?

**Answer:** Keep the same rule, although use helper methods in every class to check the same things (for example `isinstance(x, int) and not isinstance(x, bool) and x > 0`), so the rule should live in one helper that each constructor calls. Behaviour will still stay the same, with invalid data still rejected and a default still used. Only the place where the rule is written changes.

**Why it mattered:** Repeated code should use a helper method. If the rule for a valid amount changes, every place has to be found and edited, and one missed copy lets invalid data in.

**Resulting development:** I moved the repeated check into one static helper, `Inventory.check_inventory(qty)` in inventory.py. The constructor now calls it for each of the five amounts, so the rule is written once and invalid amounts still become 0:
```python
self.__ectoplasm = Inventory.check_inventory(ectoplasm)
self.__necrotic = Inventory.check_inventory(necrotic)
self.__spirit = Inventory.check_inventory(spirit)
self.__bone = Inventory.check_inventory(bone)
self.__flesh = Inventory.check_inventory(flesh)
```

```python
@staticmethod
    def check_inventory(qty):
        if (
            isinstance(qty, int)
            and not isinstance(qty, bool)
            and qty >= Inventory.MIN_QUANTITY
        ):
            return qty
        else:
            return Inventory.MIN_QUANTITY
```

**Improvements:** Each constructor is shorter and easier to read, and the validation rule is in one place, which follows the Workshop 3-2 feedback about duplicated validation.
 
---
 
# Week 6 Code Review
**Date:** Monday, September 14
**Reviewed with:** Lance
**Reviewed:** Account, SavingsAccount, EverydayAccount, Client and Transaction (protected and private attributes, `account_type`, `transactions`, `withdraw`)
 
**Questions:**
1. What is the difference between protected and private, when should each be used, and does it relate to inheritance?
   **Answer:** A single underscore (`_balance`) is protected. it is used when attributes are for a class adn its subclass and note used outside of that purpose. A double underscore (`__interest_rate`) is private, Python renames it to `_SavingsAccount__interest_rate`, so subclasses can't reach it directly. Protected is used for Account's `_balance` and `_record_transaction`, which SavingsAccount and EverydayAccount both use. Private is used in SavingsAccount's interest rate, which only `apply_interest` uses.
2. Does `account_type` need to be protected, given it is overridden anyway?
   **Answer:** No. `account_type` is not stored in an attribute, and no subclass overrides it. It is a read-only property on Account so it is always correct for whichever class the object is. Storing it in a protected attribute would let it drift out of sync with the real type.
3. Should transaction records should stay accessible without allowing the collection to be replaced directly?
   **Answer:** The `transactions` property returns `list(self._transactions)`, so callers can read, count (`transaction_count()`) to filter the history, but they can't replace `self._transactions`. Therefore new records only get in through `_record_transaction`.
4. Record successful transactions.
   **Answer:** A transaction is only recorded after the change has happened. In `deposit` and `withdraw`, the balance is changed first and then `_record_transaction` is called. A rejected withdrawal raises an error before anything changes, so nothing is recorded for it.

**Why it mattered:** A history that holds failed attempts would show money moving that never did and mean accounts become out of sync with transactions causing a multitude of problems relating to the system as a whole.
 
**Resulting development:** `Account.transactions` returns a copy, `_record_transaction` is the only place that appends, and `withdraw` raises `InsufficientFundsError`, `MinimumBalanceError` or `WithdrawalLimitError` before changing the balance (account.py, savings_account.py, everyday_account.py).

```python
@property
def transactions(self):
    # Return a copy so the caller can't replace or mutate the real list.
    return list(self._transactions)
```

```python
def withdraw(self, amount):
    if isinstance(amount, (int, float)) and not isinstance(
        ...
        if self._balance - amount >= 0:
           ...
        else:
            raise InsufficientFundsError(
                f"Account {self._number}: cannot withdraw {amount}, "
                f"balance is only {self._balance}.")
    else:
        ...
```
 
**Improvements:** The history matches the real balance, and the balance can't be changed without a matching record.
 
---
 
# Week 7 Code Review
**Date:** Monday, September 21
**Reviewed with:** [name]
**Reviewed:** Account, SavingsAccount and EverydayAccount.
 
**Question:** How does Python decide which method to use when a class inherits from another, and why can't `Account` be created on its own?
 
**Answer:** Method resolution order, or MRO, is left to right. This means that python looks for a method in the class itself first, then in its parents in the order they are listed, and each class is only checked once. In this project the chain is `SavingsAccount` -> `Account` -> `ABC` -> `object`. So `SavingsAccount.withdraw` runs first, and `super().withdraw()` moves up to `Account.withdraw`. `Account` can't be created on its own because `withdraw` is marked `@abstractmethod`, so Python raises `TypeError: Can't instantiate abstract class Account without an implementation for abstract method 'withdraw'`. Every subclass has to provide its own `withdraw`.
 
**Why it mattered:** Knowing which `withdraw` runs decides whether the minimum balance and withdrawal limit rules are applied. Making Account abstract forces every kind of account to decide its own rules.
 
**Resulting development:** Made Account an ABC with an `@abstractmethod` `withdraw`. SavingsAccount and EverydayAccount override `withdraw` and call `super().withdraw(amount)` to reuse the shared steps.

```python
class Account(ABC): ...
```

```python
@abstractmethod
def withdraw(self, amount):
    if isinstance(amount, (int, float)) and not isinstance(
        ...
        if self._balance - amount >= 0:
           ...
        else:
            raise InsufficientFundsError(
                f"Account {self._number}: cannot withdraw {amount}, "
                f"balance is only {self._balance}.")
    else:
        ...
```
 
**Improvements:** It is clear which methods a subclass must write, and the shared withdraw logic is written once instead of copied.
 
---

# WEEK 8
**Date:** Monday, October 19
**Reviewed with:** Lance
**Reviewed:** Project 3, particularly the rating system.

**Question:** Is the current match system complex enough or should there be more variance though formulas or player ratings?

**Answer:** At the moment each player and manager has one rating, and `Team.rating()` is the average of the players' ratings. `Match.play` uses teh two teams ratings cubed, to scale the goals. Splitting the rating into "Attack" and "Defence" would give each player a separate attack rating and defence rating, and the team would average each one separately, with "Attack" contributing to goals scored, and "Defence" contributing to goals conceded. A multiplier or divide factor would control how strongly each one changes the result.

**Why it mattered:** A single rating means a striker and a defender count the same way, even though they do different jobs. Splitting the rating would let the two sides' strengths affect the score in different ways.

**Resulting development:** No code has been changed yet. I've recorded this as future development, to be added after the core rating and match system works to a realistic standard. The change would go in the Player and Manager classes, `Team.rating()` and `Match.play()`, and it's listed as an area to extend in my project_3.description.md file.

**Improvements:** Keeps the current single-rating system simple while the core mechanic is being built, and records the idea so it can be added later without losing track of it.

---

# Week 9 Code Review
**Date:** Thursday, October 29
**Reviewed with:** Not reviewed.
**Reviewed:** Not applicable.

**Question:** Do I need to separate all classes, even the smaller ones, into their own files, or can small ones stay in the main file with the bigger one?

**Answer:** This question was discussed in the Week 10 review with Lance, where the answer was to put every class in its own file.

**Why it mattered:** See Week 10.

**Resulting development:** See Week 10.

**Improvements:** See Week 10.

---
 
# Week 10 Code Review
**Date:** Monday, November 2
**Reviewed with:** Lance
**Reviewed:** All projects overview.
 
**Question:** Do I need to separate all classes, even the smaller ones, into their own files, or can small ones stay in the main file with the bigger one, for example Account with the Savings and Everyday inheritance?
 
**Answer:** Yes, put every class in its own file, including the small ones. The portfolio rubric asks for one class per module, and small class sharing a file with a bigger one still breaks that rule, and is also a safe practice as for future development these small project could turn into 1000+ line files, therefore separating classes makes each class harder to find, import and test on its own.
 
**Why it mattered:** The rubric requires one class per module, and one file per class makes it possible to test each class separately.
 
**Resulting development:** Moved SavingsAccount into `savings_account.py` and EverydayAccount into `everyday_account.py`, each importing `Account` from `account.py`. I also moved all undead creatures into their own files. For project 1, each exception additionally has its own file in the `errors/` folder.
 
**Improvements:** Each file has one job, and the tests in `tests/` can target one class at a time.
