from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

numbers_list_1 = []
title = input("Enter the group title (group name)\n >")
to_user_number = input("Enter the index of the last member of this group\n >")
driver = webdriver.Firefox()


def select_user(num):
    for i in range(num):
        ActionChains(driver).send_keys(Keys.DOWN).perform()


def text_saver(text):
    with open("users__info.txt", "a+", encoding="utf-8") as text_file:
        text_file.write(f"{text}\n")
    text_file.close()


driver.get("https://web.whatsapp.com/")
sleep(120)


for i in range(1, to_user_number + 1):
    user = driver.find_element(
        "xpath",
        f"//span[@title = '{title}']",
    )
    user.click()
    user_2 = driver.find_element(
        "xpath",
        "/html/body/div[1]/div/div/div[5]/div/header/div[2]/div[1]/div/span",
    )

    user_2.click()
    user_3 = driver.find_element(
        "xpath",
        "//*[contains(text(), 'View all')]",
    )

    user_3.click()

    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    select_user(i)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.DOWN).perform()
    ActionChains(driver).send_keys(Keys.DOWN).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    sleep(5)
    ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(
        Keys.SHIFT
    ).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(
        Keys.SHIFT
    ).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(
        Keys.SHIFT
    ).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(
        Keys.SHIFT
    ).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(
        Keys.SHIFT
    ).perform()
    sleep(1)
    ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(
        Keys.SHIFT
    ).perform()
    sleep(1)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    sleep(2)
    try:
        user_info_1 = driver.find_element(
            "xpath",
            "/html/body/div[1]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[2]/h2/span",
        )
        print(user_info_1.text)
        text_saver(user_info_1.text)
        user_info_2 = driver.find_element(
            "xpath",
            "/html/body/div[1]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[2]/div/span/span",
        )
        print(user_info_2.text)
        text_saver(user_info_2.text)
        sleep(2)
    except:
        try:
            user_info_3 = driver.find_element(
                "xpath",
                "/html/body/div[1]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[2]/h2/span",
            )
            print(user_info_3.text)
            text_saver(user_info_3.text)
            sleep(2)
        except:
            try:
                user_info_4 = driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[3]/div[1]/div[1]/span",
                )
                print(user_info_4.text)
                text_saver(user_info_4.text)
                user_info_5 = driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[3]/div[1]/div[2]/span",
                )
                print(user_info_5.text)
                text_saver(user_info_5.text)
                user_info_6 = driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[3]/div[2]",
                )
                print(user_info_6.text)
                text_saver(user_info_6.text)
                sleep(2)
            except:
                try:
                    user_info_7 = driver.find_element(
                        "xpath",
                        "/html/body/div[1]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[3]/div[1]/div[2]/span",
                    )
                    print(user_info_7.text)
                    text_saver(user_info_7.text)
                    user_info_8 = driver.find_element(
                        "xpath",
                        "/html/body/div[1]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[3]/div[1]/div[1]/span",
                    )
                    print(user_info_8.text)
                    text_saver(user_info_8.text)
                    user_info_9 = driver.find_element(
                        "xpath",
                        "/html/body/div[1]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[3]/div[2]",
                    )
                    print(user_info_9.text)
                    text_saver(user_info_9.text)
                    sleep(2)
                except:
                    try:
                        user_info_10 = driver.find_element(
                            "xpath",
                            "/html/body/div[1]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[3]/div[2]",
                        )
                        print(user_info_10.text)
                        text_saver(user_info_10.text)
                        sleep(2)
                    except:
                        print(f"Something Wrong for user {i} !")
