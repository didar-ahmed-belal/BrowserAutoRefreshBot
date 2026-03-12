#!/usr/bin/env python3
import asyncio
from playwright.async_api import async_playwright
import time

async def main():
    async with async_playwright() as p:
        # ব্রাউজার লঞ্চ করুন
        browser = await p.chromium.launch(headless=False)  # GUI দেখতে
        page = await browser.new_page()
        
        # এখানে আপনার ওয়েবসাইট URL লিখুন
        website_url = "https://www.facebook.com/didar.ahmed.belal"  # এটা পরিবর্তন করুন
        await page.goto(website_url)
        
        print(f"Website opened: {website_url}")
        print("You have 10 seconds to click if needed...")
        time.sleep(10)  # 10 সেকেন্ড অপেক্ষা করুন
        
        # এখন থেকে auto refresh করবে
        while True:
            await page.reload()
            print("Refreshed active tab")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())