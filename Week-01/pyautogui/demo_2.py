import pyautogui
import time
import pyperclip

# Give time to switch to desktop
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
time.sleep(4)

# 4. Click on search box (approx position, adjust if needed)
pyautogui.click(800,100)
time.sleep(1)

# 5. Type search query
query = "The AI dude"
pyperclip.copy(query)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(4)

# 6. Click first video result (adjust coordinates)
pyautogui.click(600, 500)

print("Done! Opened first  The AI dude .")