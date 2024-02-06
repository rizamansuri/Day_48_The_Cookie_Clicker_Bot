import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# to leave browser opened after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get('https://orteil.dashnet.org/experiments/cookie/')

# get the cookie
cookie = driver.find_element(By.ID, value='cookie')

# get ids of the upgrade items
all_ids = driver.find_elements(By.CSS_SELECTOR, value="#store div")
ids = [item.get_attribute("id") for item in all_ids]

# variable to count time
five_minutes = time.time() + 60 * 5  # 5 minutes from now
five_seconds = time.time() + 5  # 5 seconds from now

# print('all item's data is ....')
# print(all_items_data)
while True:
    # click the cookie
    cookie.click()

    # every 5 seconds :

    if time.time() > five_seconds:

        # get the current cookie count
        cookie_cnt = driver.find_element(By.CSS_SELECTOR, value="#money")
        cookie_count = int(cookie_cnt.text.replace(",", ""))
        print(f"Total money is : {cookie_count}")

        # get all the prices of the items from the store
        all_prices = driver.find_elements(By.CSS_SELECTOR, value='#store b')
        all_prices.pop(len(all_prices) - 1)

        # Create dictionary of store items and prices
        i = 0
        all_upgrades = []
        for x in all_prices:
            all_upgrades.append(
                {
                    "name": x.text.split('-')[0].strip(),
                    "price": int(x.text.split('-')[1].strip().replace(",", "")),
                    "id": ids[i]
                }
            )
            i += 1

        # Find upgrades that we can currently afford
        affordable_upgrades = []
        for cost in all_upgrades:
            if cookie_count > cost['price']:
                # print(x['name'])
                affordable_upgrades.append(cost['price'])
        print(f"Affordable upgrades are...")
        print(affordable_upgrades)
        if not affordable_upgrades:
            print("There are no affordable upgrades..")
            continue
        else:
            # Purchase the most expensive affordable upgrade
            highest_affordable_upgrade = max(affordable_upgrades)
            print("Highest of affordable price is ...")
            print(highest_affordable_upgrade)
            to_purchase_id = ""
            for upgrade in all_upgrades:
                if highest_affordable_upgrade == upgrade['price']:
                    print(f"Max affordable price found for item {upgrade['id']} with price {upgrade['price']}")
                    to_purchase_id = upgrade['id']
            # print(purchase_item)

            # Purchase from store
            purchase_item = driver.find_element(By.ID, value=to_purchase_id).click()

            # Add another 5 seconds until the next check
            five_seconds = time.time() + 5
            print('5 seconds')

    if time.time() > five_minutes:  # counts 5 minutes
        cookie_per_second = driver.find_element(By.ID, value="cps").text
        print(cookie_per_second)
        break
