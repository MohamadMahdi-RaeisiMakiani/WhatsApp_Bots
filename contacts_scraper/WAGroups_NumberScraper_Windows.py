from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import win32com.client as comclt
import win32clipboard
import Contacts_VCF_Maker


def main():
    title = input("Enter the group title (group name)\n >")
    saved_numbers_file_name = input("Enter the file name\n >")
    try:
        number_of_members = int(
            input("Enter the index of the last member of this group\n >")
        )
        if number_of_members < 1:
            print("Please Enter the right number of group members!")
            quit()
    except:
        print("Please Enter Just Numbers!")

    driver = webdriver.Firefox()

    def pressing_a_key(num, key_to_press):
        for i in range(1, num + 1):
            ActionChains(driver).send_keys(key_to_press).perform()

    def pressing_two_keys(num, key1_to_press, key2_to_press):
        for i in range(1, num + 1):
            ActionChains(driver).key_down(key1_to_press).send_keys(
                key2_to_press
            ).key_up(key1_to_press).perform()

    def get_copied_text():
        win32clipboard.OpenClipboard()
        return win32clipboard.GetClipboardData()

    def text_saver(text):
        with open(
            f"info_{saved_numbers_file_name}.txt", "a+", encoding="utf-8"
        ) as text_file:
            text_file.write(f"{text}\n")
        text_file.close()

    driver.get("https://web.whatsapp.com/")
    sleep(90)

    group_selector_1 = driver.find_element(
        "xpath",
        f"//span[@title = '{title}']",
    )
    group_selector_1.click()
    group_info_selector_2 = driver.find_element(
        "xpath",
        "/html/body/div[1]/div/div/div[5]/div/header/div[2]/div[1]/div/span",
    )

    group_info_selector_2.click()
    group_members_list = driver.find_element(
        "xpath",
        "//*[contains(text(), 'View all')]",
    )
    group_members_list.click()
    pressing_a_key(2, Keys.TAB)

    for i in range(1, number_of_members + 1):
        try:
            if i != 1:
                pressing_a_key(1, Keys.DOWN)
            select_the_section = driver.switch_to.active_element
            wsh = comclt.Dispatch("WScript.Shell")
            ActionChains(driver).context_click(select_the_section).perform()
            wsh.SendKeys("{UP}")
            wsh.SendKeys("{ENTER}")
            sleep(1)
            wsh.SendKeys("^c")
            sleep(1)
            extracted_text = get_copied_text()
            index_of_number_starting = extracted_text.find(">+")
            string_from_the_number = extracted_text[index_of_number_starting:-1]
            index_of_ending_number_string = string_from_the_number.find("<")
            full_number_string = string_from_the_number[1:index_of_ending_number_string]
            print(full_number_string)
            text_saver(full_number_string)
            win32clipboard.CloseClipboard()
            sleep(1)
            wsh.SendKeys("^+i")
        except:
            try:
                continue
            except:
                print("Something is Wrong!!!")
    driver.quit()


if __name__ == "__main__":
    main()
    _next_step_1 = input("If you want to save the numbers as a VCF file enter make\n >")
    if _next_step_1 == "make":
        Contacts_VCF_Maker.vcf_maker()
    else:
        print(f"Numbers are stored in a txt file.")
