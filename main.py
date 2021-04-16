import pyautogui

x=0
while x<=100:
	pyautogui.write('Message', interval=0.03)
	pyautogui.press('enter')
	pyautogui.pause(1)
	x=x+1

