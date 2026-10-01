---
type: llm
---

PASS if the response names the case of the user changing the scope (agency ↔ a client) while a save, an undo or a reset is still in progress, and at least one consequence of it: Undo or ↺ acting on the wrong level, the old scope's value showing in the new scope's table, or a cell staying locked in the scope just switched to. FAIL if the concurrency cases only cover two people editing at once or double clicks, without the scope changing mid-save.
