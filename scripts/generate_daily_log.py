import os
import datetime
from pathlib import Path
import random

TIPS = [
    "Clean code is not written, it's rewritten.",
    "The best way to get a project done faster is to start sooner.",
    "Before you code, think about the data structures first.",
    "Don't comment what the code does, comment why it does it.",
    "Always leave the code specialized and the data generalized.",
    "Simplicity is the soul of efficiency.",
    "The most dangerous phrase in the language is, 'We've always done it this way.'",
    "Testing is not about finding bugs, it's about gaining confidence.",
    "Refactor early, refactor often.",
    "A language that doesn't affect your way of thinking about programming is not worth knowing."
]

def update_readme(tip):
    readme_path = Path("README.md")
    if not readme_path.exists():
        return
        
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    start_marker = "<!-- START_SECTION:daily_tip -->"
    end_marker = "<!-- END_SECTION:daily_tip -->"
    
    if start_marker in content and end_marker in content:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_section = f"{start_marker}\n### 💡 Daily Dev Tip\n> {tip}\n\n<p align=\"right\"><i>Last updated: {timestamp}</i></p>\n{end_marker}"
        
        # Replace the entire section including markers
        import re
        pattern = f"{re.escape(start_marker)}.*?{re.escape(end_marker)}"
        updated_content = re.sub(pattern, new_section, content, flags=re.DOTALL)
        
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("Updated README.md with new tip.")

def generate_daily_log():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    log_path = Path(log_dir) / f"{today}.md"
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    daily_tip = random.choice(TIPS)
    
    template = f"""# 📝 Daily Dev Log | {datetime.datetime.now().strftime("%B %d, %Y")}

---

### 💡 Daily Dev Tip
> {daily_tip}

---

## 🧠 Learning & Discovery
- [ ] *What did you learn today?*

## 💻 Code & Implementation
- [ ] *Key features or bug fixes...*

## 📅 Plan for Tomorrow
- [ ] *Next steps...*

---
<p align="right">
  <i>Generated with ❤️ at {timestamp}</i>
</p>
"""

    if not log_path.exists():
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(template)
        print(f"Created new log: {log_path}")
    else:
        update_content = f"\n\n## Update @ {timestamp}\n- Automated system check-in."
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(update_content)
        print(f"Appended update to: {log_path}")
    
    # Also update the README
    update_readme(daily_tip)

if __name__ == "__main__":
    generate_daily_log()
