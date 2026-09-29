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
    return (f"Transaction: identifier={self.__identifier}, "
            f"transaction_type={self.__transaction_type}, amount={self.__amount}, "
            f"desc={self.__desc}, status={self.__status}")
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

## Week 4 Code Review
else
ordering

## Week 5 Code Review

repeatign code use healper method


## Week 6 Code Review

Difference beweteen protected and privete adn when to use when. does it have soemthign to do wiht inheritence 
does account_type needa be protected besit its beign overidden anyway
Transaction records should remain accessible without allowing the collection to be replaced directly.?
AND Record successful transactions.?


## Review your Project 1 checkpoint feedback.
Identify issues relating to the object model.
Identify issues relating to class responsibilities.
Identify issues relating to relationships.
Identify issues relating to encapsulation or visibility.
Identify issues relating to inheritance.
Identify issues relating to code quality or readability.

## AI vs Human class code
**Prompt:** Can you create a class for a new python banking project which is able to deposit, withdraw, and view account transaction which are found an an additional class transactions.

Identify similarities between the two solutions.
    Compare the classes created.
    Compare attributes.
    Compare methods.
    Compare relationships.
    Compare inheritance.
    Compare validation and encapsulation.
Identify differences between the two solutions.
For each important difference, consider why it occurred.
    Was information missing from the prompt?
    Did the AI make an assumption?
    Did it choose a different but valid design?
    Did it use a concept that has not been taught?
    Did it misunderstand part of the problem?
    Did it introduce unnecessary complexity?
Identify anything in the generated solution that would not meet the requirements of this course.
Decide which solution is stronger for the selected problem.
    Your solution may be stronger.
    The generated solution may contain a useful design decision.
    Different parts of each solution may be stronger.
Justify the comparison using OOP concepts rather than personal preference.


Task 4: Improve the prompt...
Task 5: Compare the Two AI Responses...
Task 6: Verify Before You Trust...



WEEK 7

order MRO

Diaminod order

1 -2- 1

usually be the left ro right ordergin