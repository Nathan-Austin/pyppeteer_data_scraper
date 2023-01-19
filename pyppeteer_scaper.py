import asyncio
from pyppeteer import launch


links_list = ['your list of links']
search_list = ['things you want to search']

async def main():
    """Scrape data from {your website} and insert into dataBase
    launch Chromium browser in the background
    open a new tab in the browser"""
    browser = await launch({"headless": False}, executablePath="/usr/bin/google-chrome")
    page = await browser.newPage()

    await page.goto(f"https://www.google.com")
    await page.setViewport({"width": 1600, "height": 900})
    await page.waitFor(2000)
    """if the page has a cookies button you can get past it here.
    to find the script right click on the button and click inspect then insert the html script.
    if you have a second button to push such as only selected cookies use the following lines"""
    await page.click('button[ html script]')
    await page.waitFor(1000)
    await page.click('button[second script]')
    """if you have a list of links you can now have the page open all the links """
    for i in links_list:
        await page. waitFor(1000)
        await page.goto(i)
        await page.waitFor(3000)
        """now you need to scrape your data"""
        selector = await page.querySelectorAll('[html script"]')
        what_you_want = ([await page.evaluate('(element) => element.textContent', a) for a in selector])

        """if you want to uptade a table you can do it here otherwise delete these lines"""
        sql_query = f"""UPDATE table 
                                VALUES(f'{what_you_want})
                                WHERE link_list = '{i}';"""
        print(sql_query)
        """you need to make a function to insert you query to your database"""
        #commit_to_dataBase(sql_query)
    """or if you want to search the website using its own search function"""
    await page.click('button[ html script]')
    for i in name_list:
        await page.waitFor(1000)
        """click on the search box"""
        await page.click('[placeholder="Search Google or type a URL"]')
        """enter string into search box"""
        await page.waitFor(2000)
        await page.keyboard.type(i)
        await page.keyboard.type('Enter')
        await page.waitFor(2000)
        """now the page should open up to whatever you searched
        you now need get the info you need """
        selector = await page.querySelectorAll('[html script"]')
        what_you_want = ([await page.evaluate('(element) => element.textContent', a) for a in selector])
    """close the browser"""
    await browser.close()

if __name__ == '__main__':
    print("Starting...")
    asyncio.get_event_loop().run_until_complete(main())
