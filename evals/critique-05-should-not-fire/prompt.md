---
max_turns: 20
timeout_seconds: 600
allowed_tools: [Skill, Bash, Read]
---

My React modal won't close when I press Escape. Here's the component:

```jsx
function Modal({ open, onClose, children }) {
  useEffect(() => {
    const onKey = (e) => { if (e.key === "Esc") onClose(); };
    window.addEventListener("keydown", onKey);
  }, []);
  if (!open) return null;
  return <div role="dialog">{children}</div>;
}
```

What's wrong?
