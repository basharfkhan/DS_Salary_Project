from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import urllib.parse
import os

#  Author : Bashar , arapfaik 
#  url: https://github.com/arapfaik/scraping-glassdoor-selenium 

def safe_find_text_from(el, by, value, default="-1"):
    """Get text safely from an element. Returns default if not found."""
    try:
        return el.find_element(by, value).text
    except NoSuchElementException:
        return default


import random

def get_jobs(keyword, num_jobs, verbose=False, slp_time=3, location=None,
             save_every=25, out_prefix="glassdoor_jobs", resume=True):
    """
    Scrapes job listings from Glassdoor (card-level only).
    Auto-saves to CSV every `save_every` jobs.
    Resumes from last save and skips duplicates by Job Link.
    """

    jobs = []
    seen_links = set()

    # ✅ Resume if previous file exists
    final_file = f"{out_prefix}_final.csv"
    if resume and os.path.exists(final_file):
        print(f"📂 Found previous run → {final_file}, resuming from there")
        df_prev = pd.read_csv(final_file)
        jobs = df_prev.to_dict("records")
        seen_links = set(df_prev["Job Link"].dropna().tolist())

    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1400, 1000)

    # Build URL dynamically
    base_url = f'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="{urllib.parse.quote(keyword)}"&jobType=all'
    if location:
        base_url += "&locKeyword=" + urllib.parse.quote(location)

    driver.get(base_url)

    while len(jobs) < num_jobs:
        time.sleep(slp_time + random.uniform(0.5, 1.5))  # ⏳ human-like wait

        # ✅ Check for Glassdoor "Unexpected Error" or "Zzzzzzzz..." page
        if any(err in driver.page_source for err in ["Unexpected Error", "Zzzzzzzz"]):
            print("⚠️ Error/Zzz page detected. Refreshing...")
            driver.refresh()
            time.sleep(6)   # wait longer to let jobs reload
            continue

        # ✅ Get job cards
        try:
            job_cards = WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//div[starts-with(@class,"JobCard_jobCardContainer__")]')
                )
            )
        except TimeoutException:
            print("No job listings found, stopping.")
            break

        for card in job_cards:
            if len(jobs) >= num_jobs:
                break

            try:
                job_link = card.find_element(By.CSS_SELECTOR, 'a[data-test="job-title"]').get_attribute("href")
            except NoSuchElementException:
                job_link = "-1"

            if job_link in seen_links:
                continue  # 🚫 skip duplicate

            print(f"Progress: {len(jobs)}/{num_jobs}")

            job_title = safe_find_text_from(card, By.CSS_SELECTOR, 'a[data-test="job-title"]')
            company_name = safe_find_text_from(card, By.CSS_SELECTOR, 'span.EmployerProfile_compactEmployerName__9MGcV')
            company_rating = safe_find_text_from(card, By.CSS_SELECTOR, 'span.rating-single-star_RatingText__5fdjN')
            location_text = safe_find_text_from(card, By.CSS_SELECTOR, 'div[data-test="emp-location"]')
            salary = safe_find_text_from(card, By.CSS_SELECTOR, 'div[data-test="detailSalary"]')
            job_snippet = safe_find_text_from(card, By.CSS_SELECTOR, 'div[data-test="descSnippet"]')
            date_posted = safe_find_text_from(card, By.CSS_SELECTOR, 'div[data-test="job-age"]')
            easy_apply = safe_find_text_from(card, By.CSS_SELECTOR, 'div.JobCard_easyApplyTag__5vlo5')

            try:
                company_logo = card.find_element(By.CSS_SELECTOR, 'img.avatar-base_Image__FZpQS').get_attribute("src")
            except NoSuchElementException:
                company_logo = "-1"

            jobs.append({
                "Job Title": job_title,
                "Company": company_name,
                "Company Rating": company_rating,
                "Location": location_text,
                "Salary": salary,
                "Job Snippet": job_snippet,
                "Date Posted": date_posted,
                "Easy Apply": easy_apply,
                "Company Logo": company_logo,
                "Job Link": job_link
            })

            seen_links.add(job_link)

            # ✅ Auto-save every N jobs
            if len(jobs) % save_every == 0:
                df_partial = pd.DataFrame(jobs)
                filename = f"{out_prefix}_up_to_{len(jobs)}.csv"
                df_partial.to_csv(filename, index=False)
                print(f"💾 Saved progress: {len(jobs)} jobs → {filename}")

        # ---- Pagination or Load More ----
        try:
            # Try load more
            load_more = driver.find_element(By.CSS_SELECTOR, 'button[data-test="load-more"]')
            load_more.click()
            print("🔄 Clicked Load More button")
            time.sleep(3)
        except NoSuchElementException:
            # If no load more → try pagination
            try:
                next_btn = driver.find_element(By.CSS_SELECTOR, 'button[data-test="pagination-next"]')
                next_btn.click()
                print("➡️ Clicked Next Page button")
                time.sleep(3)
            except NoSuchElementException:
                print(f"✅ Reached end: scraped {len(jobs)} jobs total")
                break

    driver.quit()
    df = pd.DataFrame(jobs)

    # Final save
    df.to_csv(final_file, index=False)
    print(f"🎉 Finished scraping {len(df)} jobs → {final_file}")

    return df
