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


def safe_find_text(driver, by, value, default="-1"):
    """Get text safely with WebDriver. Returns default if not found."""
    try:
        return driver.find_element(by, value).text
    except NoSuchElementException:
        return default


def safe_find_text_from(el, by, value, default="-1"):
    """Get text safely from an element. Returns default if not found."""
    try:
        return el.find_element(by, value).text
    except NoSuchElementException:
        return default


def get_jobs(keyword, num_jobs, verbose=False, slp_time=5, location=None):
    """
    Scrapes job listings from Glassdoor.
    Args:
        keyword (str): job title / keyword
        num_jobs (int): number of jobs to scrape
        verbose (bool): print details while scraping
        slp_time (int): sleep time to let page load
        location (str): optional location (e.g., "New York, NY"). If None → nationwide.
    """

    options = webdriver.ChromeOptions()
    # options.add_argument("headless")  # uncomment for headless run
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1400, 1000)

    # ✅ Build URL dynamically
    base_url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + urllib.parse.quote(keyword) + '"&jobType=all'
    if location:
        base_url += "&locKeyword=" + urllib.parse.quote(location)

    driver.get(base_url)
    jobs = []

    while len(jobs) < num_jobs:
        time.sleep(slp_time)

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
            print(f"Progress: {len(jobs)}/{num_jobs}")

            # ---- CARD FIELDS ----
            job_title_card = safe_find_text_from(card, By.CSS_SELECTOR, 'a[data-test="job-title"]')
            company_name_card = safe_find_text_from(card, By.CSS_SELECTOR, 'span.EmployerProfile_compactEmployerName__9MGcV')
            company_rating_card = safe_find_text_from(card, By.CSS_SELECTOR, 'span.rating-single-star_RatingText__5fdjN')
            location_card = safe_find_text_from(card, By.CSS_SELECTOR, 'div[data-test="emp-location"]')
            salary_card = safe_find_text_from(card, By.CSS_SELECTOR, 'div[data-test="detailSalary"]')
            job_snippet = safe_find_text_from(card, By.CSS_SELECTOR, 'div[data-test="descSnippet"]')
            date_posted = safe_find_text_from(card, By.CSS_SELECTOR, 'div[data-test="job-age"]')
            easy_apply = safe_find_text_from(card, By.CSS_SELECTOR, 'div.JobCard_easyApplyTag__5vlo5')

            # Optional logo
            try:
                company_logo = card.find_element(By.CSS_SELECTOR, 'img.avatar-base_Image__FZpQS').get_attribute("src")
            except NoSuchElementException:
                company_logo = "-1"

            # Job link
            try:
                job_link = card.find_element(By.CSS_SELECTOR, 'a[data-test="job-title"]').get_attribute("href")
            except NoSuchElementException:
                job_link = "-1"

            # ---- CLICK CARD TO LOAD DETAIL ----
            try:
                # driver.execute_script("arguments[0].click();", card)
                # WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, 'h1[id^="jd-job-title"]'))

                # Scroll into view so you can SEE it move
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
                time.sleep(0.5)

                # Click the card
                driver.execute_script("arguments[0].click();", card)

                # Wait for detail panel to update
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'h1[id^="jd-job-title"]'))
                )
                time.sleep(1)
            except Exception:
                print("⚠️ Could not click job card.")
                continue

            # ---- DETAIL PANEL FIELDS ----
            job_title_detail = safe_find_text(driver, By.CSS_SELECTOR, 'h1[id^="jd-job-title"]')
            company_name_detail = safe_find_text(driver, By.CSS_SELECTOR, 'h4.heading_Subhead__jiUbT')
            company_rating_detail = safe_find_text(driver, By.CSS_SELECTOR, 'span.rating-single-star_RatingText__5fdjN')
            location_detail = safe_find_text(driver, By.CSS_SELECTOR, 'div[data-test="location"]')
            salary_detail = safe_find_text(driver, By.CSS_SELECTOR, 'div[data-test="detailSalary"]')
            median_pay = safe_find_text(driver, By.CSS_SELECTOR, 'div.SalaryEstimate_medianEstimate__fOYN1')
            job_description = safe_find_text(driver, By.CSS_SELECTOR, 'div.JobDetails_jobDescription__uW_fK')
            ceo_name = safe_find_text(driver, By.CSS_SELECTOR, 'div.JobDetails_ceoName__6FwKk')

            # ---- MERGE DATA ----
            jobs.append({
                "Job Title (Card)": job_title_card,
                "Company (Card)": company_name_card,
                "Company Rating (Card)": company_rating_card,
                "Location (Card)": location_card,
                "Salary (Card)": salary_card,
                "Job Snippet": job_snippet,
                "Date Posted": date_posted,
                "Easy Apply": easy_apply,
                "Company Logo": company_logo,
                "Job Link": job_link,
                "Job Title (Detail)": job_title_detail,
                "Company (Detail)": company_name_detail,
                "Company Rating (Detail)": company_rating_detail,
                "Location (Detail)": location_detail,
                "Salary (Detail)": salary_detail,
                "Median Pay": median_pay,
                "Job Description": job_description,
                "CEO Name": ceo_name
            })

            if verbose:
                print(f"✅ {job_title_detail} @ {company_name_detail} | {location_detail}")
                print(f"💰 {salary_detail} (Median {median_pay})")

        # ---- NEXT PAGE ----
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-test="pagination-next"]'))
            ).click()
        except Exception:
            print(f"Scraping terminated early: got {len(jobs)} jobs, target {num_jobs}")
            break

    driver.quit()
    return pd.DataFrame(jobs)
