from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import win32com.client as comclt
import win32clipboard

driver = webdriver.Firefox()


def pressing_a_key(num, key_to_press):
    for i in range(1, num + 1):
        ActionChains(driver).send_keys(key_to_press).perform()


def pressing_two_keys(num, key1_to_press, key2_to_press):
    for i in range(1, num + 1):
        ActionChains(driver).key_down(key1_to_press).send_keys(key2_to_press).key_up(
            key1_to_press
        ).perform()


def get_copied_text():
    win32clipboard.OpenClipboard()
    return win32clipboard.GetClipboardData()


driver.get("https://www.time.ir/")
sleep(2)
pressing_a_key(5, Keys.TAB)
pressing_two_keys(1, Keys.SHIFT, Keys.TAB)
lookup_2 = driver.switch_to.active_element
wsh = comclt.Dispatch("WScript.Shell")
ActionChains(driver).context_click(lookup_2).perform()
wsh.SendKeys("{UP}")
wsh.SendKeys("{ENTER}")
sleep(3)
wsh.SendKeys("^c")
sleep(1)
extracted_text = get_copied_text()
print(extracted_text)
print(type(extracted_text))
print(extracted_text.find(">"))
win32clipboard.CloseClipboard()
sleep(3)
wsh.SendKeys("^+i")
# sleep(5)
# driver.quit()
# pressing_two_keys(1, Keys.CONTROL, "C")
# sleep(2)
# pressing_a_key(10, Keys.DOWN)
# pressing_a_key(1, Keys.ENTER)


# pressing_two_keys(1, Keys.LEFT_SHIFT, Keys.F10)
# pressing_a_key(1, Keys.UP)
# pressing_a_key(1, Keys.ENTER)
# win32clipboard.OpenClipboard()
# data = win32clipboard.GetClipboardData()
# win32clipboard.CloseClipboard()
# print(data)
# ------------------------------------------------
# Help Center
# ------------------------------------------------
# Keys.SHIFT
# Keys.TAB
# Keys.DOWN
# Keys.PAGE_DOWN
# Keys.CONTROL
# Keys.COMMAND
# send_keys("V")
# ActionChains(driver).context_click().perform()
# x = driver.find_element("xpath",f"//span[@title = 'GroupTitle']")
# x.click()
# driver.quit()
# driver.close()
# pressing_a_key(1, Keys.SHIFT + Keys.F10)
