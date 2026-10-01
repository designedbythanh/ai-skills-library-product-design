---
type: llm
---

PASS if the recommended handling for a scope change during a save ties each request to the scope it was sent from: for example, ignore or cancel answers that come back for a scope no longer on screen, bind Undo to the level the change was made at, or hold the scope switch until pending saves finish. FAIL if the handling is only generic ("show a loading state", "disable the button") with nothing about which scope the result belongs to.
