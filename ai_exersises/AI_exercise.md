# AI Literacy Exercise: Project 1 (Account and Transaction)

Files for this exercise (kept separate from the assessed Project 1 classes):
- `ai_classes.py`: AI response 1 (baseline prompt)
- `ai_classes_v2.py`: AI response 2 (improved prompt)

---

## Task 1: Respond to Checkpoint Feedback

- **Object model:** The UML marks methods that return nothing as void, but in Python it should say None. Methods like `get_accounts()` should state what the list holds (`list[Account]`).
- **Class responsibilities:** Methods did not consider the state of the object. `Branch.opened()` printed "We are now open!" even if the branch was already open. (My own Week 3 design review also noted that `Client` does more than one job.)
- **Relationships:** No feedback on this.
- **Encapsulation / visibility:** No feedback on this.
- **Inheritance:** No feedback on this.
- **Code quality / readability:** Some lines were too long for PEP8, and `updateInfo()` in `branch.py` was not snake_case. Comments were also not full sentences ending in a full stop, and many only restated the code instead of explaining why. Method names also differed between the UML and the code (`UpdateAccountInfo()` vs `update_account_info()`).

**Most important change:**
- Feedback: "Make sure to consider the state of the objects in your methods. If I open a branch, I'll get the message 'We are now open!', even if the branch was already open."
- Change I made: I added a check on the branch’s current state before opened() changes anything. If the branch is closed, it opens and prints “We are now open!”. If it is already open, nothing changes and it prints that the branch is already open. the same change where made to closed().
- Why the new design is stronger: The method now respects the object state meaning there is no misleading print statements. This rule also sits in the class Branch class not spread across the code. It is also easier to test where you can now demonstrate that that the branch is either open or closed depending on the  

## Task 2: Baseline Prompt

**Area chosen:** The Account and Transaction relationship.

**Prompt:**
Can you create a class for a new python banking project which is able to deposit, withdraw, and view account transaction which are found an an additional class transactions.

The response is saved in `ai_classes.py`.

---

## Task 3: Evaluate the Baseline Response

### Similarities
- Both have an account class and a separate Transaction class.
- Both have `deposit` and `withdraw`, and both reject amounts that are 0 or less.
- Both stop a withdrawal bigger than the balance.
- Both keep a list of transactions inside the account.
- Both print messages when an operation succeeds or fails.
- Both give each transaction a type and an amount.

### Differences and why they happened

**Validation.** My code checks types with isinstance in every constructor and method, but the AI only checks that the amount is above 0, so something like `deposit("abc")` would crash it. This happened due to my prompt never asked for type checking.

**Encapsulation.** My attributes are protected or private and accessed through properties, whereas the AI's are all public. This means anyone could set `account.balance = 999999` directly. The prompt never mentioned encapsulation, so the AI had no reason to add it. My `.transactions` property also returns a copy of the list therefore outside code can't edit it, while the AI exposes the real list. This is another gap caused by the simplicity of the prompt.

**Transaction contents.** My transactions store an identifier, type, amount, description and status. The AI's store a type, amount and `balance_after`. The AI made its own assumption about what a transaction should hold. Mine also get unique ids from a shared counter, while the AI's have no ids at all.

**Repeated code.** I use one `_record_transaction` helper for both deposit and withdraw. The AI creates the `Transaction` separately in each method, which repeats code. This is a different design choice, where mine avoids the repetition.

**Inheritance and extra classes.** Mine has an account hierarchy with `SavingsAccount` and `EverydayAccount`, each with its own withdraw rule, plus `Client` and `Branch` classes. The AI has a single account class and nothing else, because the prompt only asked for a basic account with deposits, withdrawals and viewing transactions.

**Viewing transactions and output.** The AI has a `view_transactions()` method that prints the history, whereas mine exposes a `.transactions` property and `main.py` does the printing. These are different but both valid designs. The AI also formats its output more neatly, with aligned columns, a `$` sign and two decimal places, where mine prints plain text.

**Other conventions.** I include a `__repr__` on my classes, but the AI only has `__str__` on `Transaction`. It does add an `if __name__ == "__main__"` demo, which I don't use.

### Anything that would not meet this course's requirements
- Public attributes with no properties.
- No `isinstance` validation on inputs.
- No `__repr__`.

### Which is stronger? 
I think my solution is stronger. It uses encapsulation, so the balance and transactions can only be changed through the deposit and withdraw functions, while the AI's public attributes can be overwritten from anywhere. It also validates input with `isinstance` and reuses the `_record_transaction` helper, but the AI version does not. The AI's version is simpler and its `balance_after` parameter is a useful idea, although overall its simpler design leaves out validation and encapsulation.

---

## Task 4: Improved Prompt

The first prompt left out many key areas such as validation, visibility and more. the improved prompt uses teh required structure and fills those gaps.

The response is saved in `ai_classes_v2.py`.

**Context:**
I am building a small banking system for a university object-oriented programming course in Python. It models bank accounts and the transaction records that those accounts create.

**Goal:**
The goal is to implement an Account class hierarchy (a parent Account with SavingsAccount and EverydayAccount subclasses) and a Transaction class, where each account creates and owns its own transactions.

**Existing Design:**
- Account is the parent class. SavingsAccount and EverydayAccount inherit from it.
- Account creates and owns its Transaction objects (composition). Transactions are never created outside Account.

**Requirements:**
- Account: number (positive int/float), name (str), balance (int/float, 0 or more), and a list of transactions.
- Account has read-only properties for number, name and balance. `account_type` is a property worked out from the class name, not stored and `transactions` returns a copy of the list.
- `deposit(amount)` and `withdraw(amount)` only accept positive numbers. Withdraw cannot take the balance below 0.
- Each successful deposit or withdrawal creates one Transaction through a single private helper method. Failed operations create nothing.
- Transaction has an identifier (unique positive int), type, amount, description and a status of Pending, Processed or Cancelled, all with read-only properties with `processed()` and `cancelled()` methods.
- SavingsAccount has an interest rate and a constant minimum balance. It overrides `withdraw` to refuse withdrawals below the minimum, and completes valid ones with `super().withdraw()`.
- EverydayAccount has a constant maximum single withdrawal. It overrides `withdraw` to refuse amounts above it, and completes valid ones with `super().withdraw()`.

**Constraints:**
- Python 3 only.
- Use `_` protected attributes where subclasses need access and `__` private attributes where they do not.
- Use `@property` instead of `get_x()` methods.
- Validate with `isinstance` (and reject bool). On invalid input print a message and use a safe default or leave the state unchanged. Do not raise exceptions.
- Do not use abstract classes, dataclasses, enums or any decorator other than `@property`.
- Do not copy the parent's `withdraw` code into the subclasses.

**Output:**
One Python file with all classes. Each class gets a short docstring. Add a short demo at the bottom that shows deposits, withdrawals and rejected operations.

---

## Task 5: Compare the Two AI Responses

### What changed from response 1 to response 2
- **Class structure:** 
    Response 1 only had `Transaction` and `BankAccount`. 
    Response 2 has `Transaction`, `Account`, `SavingsAccount` and `EverydayAccount`.
- **Visibility:** 
    Response 1 had everything public. 
    Response 2 uses private attributes in `Account``Transaction` and subclasses.
- **Relationships:** 
    Response 1 made transactions separately inside deposit and withdraw. 
    Response 2 uses a helper method, so `Account` creates and owns its transactions.
- **Method responsibilities:** 
    In response 2, `deposit` and `withdraw` return True or False so you can tell if they worked. Response 1 returned nothing.
- **Inheritance:** 
    Response 1 had none. 
    Response 2 has `SavingsAccount` and `EverydayAccount` overriding `withdraw` and calling `super().withdraw()`.
- **Validation:** 
    Response 1 only checked that the amount was above 0. 
    Response 2 checks types with `isinstance`.
- **Naming:** 
    Response 1 used `owner`. 
    Response 2 uses `number`, `name` and `account_type`, which are closer to what the course uses.
- **Complexity:** 
    Response 1 is around 55 lines.
    Response 2 is around 220 lines.

### Requirements followed more accurately in response 2
- Private Variables
- `isinstance` validation with set defaults.
- `account_type` comes from the class name.
- Clear constants for `MIN_BALANCE` and `MAX_WITHDRAW`.
- Inheritance used for `super().withdraw()` instead of copying the parent code.
- `.transactions` returns a copy.

### Problems that remain
- The `isinstance` check is repeated in almost every method and constructor.
- `SavingsAccount.withdraw` and `EverydayAccount.withdraw` check the amount is a number before calling `super()`, and then the parent checks it again.
- It added things I did not ask for: `apply_interest()`, a `__str__` on `Account` and `Transaction`, and True/False return values.
- The transaction id counter is shared class-level state, so it is a hidden global.
- `Transaction.VALID_STATUSES` is a public list that could be edited from outside.
- It lost `balance_after` and `view_transactions()` from response 1.

### Did the prompt become over-constrained?
Yes, my improved prompt listed everything that needed to be added and overridden, and even where co call .super(). Because of this response 2 ended up being almost my own solution written by AI. this made it much more accurate, although the AI was left to make no decisions because i describe teh solution rather than the problem.

### Was the improved prompt better? Why?
Yes, teh improved prompt did result in a better response. The new prompt followed teh course requirements much more closely, using private properties, validation, and inheritance, as well as creating helper methods in transaction. This is primarily due to teh prompt for response 2 being much more in depth, although despite this details were also lost in response 2 such as teh apply_interest and `__str__`. response 2 also had a lot of repetition in validation.

---

## Task 6: Verify Before You Trust

I reviewed `ai_classes_v2.py` as if it came up in a code review.

- **Does it satisfy the prompt's requirements?** Yes, every class, property, constant and override from the prompt is there.
- **Does it run as written?** Yes. I ran it: the demo shows the savings minimum balance and the everyday limit both rejecting withdrawals, the invalid deposit is rejected, and only the valid operations create transactions. `withdraw("abc")` and `withdraw(-5)` also print a message and don't crash.
- **Assumptions that were not asked for:** `__str__` methods returning True/False, and a global id counter.
- **Missing requirements:** None that I found.
- **Unnecessary complexity:** The repeated validation blocks, and the double validation in the subclass `withdraw` methods.
- **Things I would need to understand before trusting it:** `type(self).__name__`, why `transactions` returns `list(self._transactions)`, and how `super().withdraw(amount)` reaches the parent.

**One design decision to discuss (pick one, or choose another):** the shared transaction id counter.
- **What does it do?** Every transaction from every account takes the next number, so ids are unique across all accounts.
- **Why might the AI have chosen it?** The prompt said ids must be unique, and a class-level counter is the simplest way to do that.
- **Is it appropriate for this project?** Yes, as every transaction needs a unique id, and the counter is a sufficient and simple way to do so.
- **Would I keep, change or remove it, and why?** 
I would keep it with small changes. The counter is shared at as class level variable, so code can change it causing duplicate ID's. Making the variable private would restrict its access and make the solution work well. This is what i used in my own solution.

