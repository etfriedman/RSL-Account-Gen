# RSL Account Generator


## What does it do?

A python script that generates accounts for raid shadow legends

![Alt Text]()


## Dependencies:
1. selenium

## Setup/Install:
1. pip install selenium
2. git clone https://github.com/etfriedman/RSL-Account-Gen/
3. cd RSL-Account-Gen
4. Replace URL with refferall URL
5. Replace username, password, email, submit, accept, XPaths with XPaths from your page (may vary from page to page)
Example XPath: '//*[@id="root"]/div/div/div[2]/div/button[2]'
6. See gif below on how to get XPath
7. python accountgen.py

## How to get XPath
![Alt Text](https://i.gyazo.com/0595b5e16419870778108c9ddb19881d.mp4)

## How to get XPath for last button
![Alt Text](https://i.gyazo.com/2e6ea47cdd11f5c043f315ec31787bfb.mp4)

## Common Errors:
- issue with XPath, make sure you have the correct one
- if you are sure you have the right one and are still getting an error, increase the time.sleep() but a few hundred milliseconds to acount for slower internet speeds. (Most common with the last button from the pop-up)
