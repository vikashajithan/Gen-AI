import pyautogui
import time
import pyperclip

# Give you 5 seconds to focus on desktop
time.sleep(5)

# 1. Open Run dialog (Windows)
pyautogui.hotkey('win', 'r')
time.sleep(1)

# 2. Open Chrome (you can change to msedge or firefox)
pyautogui.typewrite('chrome')
pyautogui.press('enter')
time.sleep(5)

# 3. Go to Google
pyautogui.typewrite('https://www.chatgpt.com')
pyautogui.press('enter')
time.sleep(5)

# 4. Type search query
query = "India vs New Zealand last match"
pyperclip.copy(query)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)

# 5. Click first result (approximate position)

# Move mouse to first result area (adjust if needed)
pyautogui.moveTo(500, 350, duration=1)
pyautogui.click()

print("Done! Opened first Google result.")
