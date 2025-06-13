---

```markdown
# ⏱️ Pomodoro Timer using Python & Tkinter

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

A productivity timer that uses the Pomodoro technique to help you work in focused intervals. Built with Python and Tkinter for a simple GUI experience.

---

## 🍅 How It Works

- Work session: 25 mins *(currently set to 0.5 min for testing)*
- Short break: 5 mins *(set to 0.1 min for testing)*
- Long break: Every 4 work sessions

The app cycles through:
```

Work → Short Break → Work → Short Break → ... → Long Break

```

✔️ A checkmark appears after each completed work session.

---

## 🧠 Python Concepts Used

- **Tkinter**: GUI layout, buttons, canvas, labels
- **Timer Mechanism**: `after()` method to create a countdown
- **Function Chaining**: Auto-triggers next session after countdown
- **Global State**: Tracks work/break cycles via `reps` variable
- **Modular Constants**: For easy theme and time adjustments

---

## 📁 File Structure

```

pomodoro-timer/
├── main.py          # Main application logic
├── tomato.png       # Image asset for UI

````

---

## ▶️ How to Run

**Requirements**: Python 3.7+, Tkinter (preinstalled with Python)

```bash
python main.py
````

---

## 📄 License

MIT License — free to use, modify, and distribute.

---
