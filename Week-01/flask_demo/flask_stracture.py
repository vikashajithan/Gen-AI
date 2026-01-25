from flask import Flask, render_template_string
import pyautogui
import time
import pyperclip

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>YouTube Automation</title>
</head>
<body>
    <h2>YouTube Automation with Flask</h2>
    <form action="/run" method="post">
        <button type="submit">Open YouTube & Search</button>
    </form>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/run", methods=["POST"])
def run_script():
    # Give time to switch focus
    time.sleep(2)

    # 1. Open Run dialog
    pyautogui.hotkey('win', 'r')
    time.sleep(1)

    # 2. Open Chrome
    pyautogui.typewrite('chrome')
    pyautogui.press('enter')
    time.sleep(4)

    # 3. Open YouTube
    pyautogui.typewrite('https://www.youtube.com')
    pyautogui.press('enter')
    time.sleep(5)

    # 4. Click on search box (adjust coordinates)
    pyautogui.click(800, 100)
    time.sleep(1)

    # 5. Type search query
    query = "The AI dude"
    pyperclip.copy(query)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(4)

    # 6. Click first video result (adjust coordinates)
    pyautogui.click(600, 500)

    return "Automation executed successfully!"

if __name__ == "__main__":
    app.run(debug=True)
