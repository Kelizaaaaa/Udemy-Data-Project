# # Udemy Scrapping
# This script aims to pull and scrape data from Udemy regarding the details and information of various courses offered by Udemy. 

# Library 
import time
import requests
import numpy as np
import pandas as pd
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

#################################################################################################
#-------------------------------------- Establish connection -----------------------------------#
#################################################################################################

main_url = "https://www.udemy.com"
page = requests.get(main_url)
soup = BeautifulSoup(page.content, "html.parser")
page.close()


#################################################################################################
#------------------------------------ Extract Subcategories ------------------------------------#
#################################################################################################
links = soup.find_all("a", class_="js-side-nav-cat js-subcat")

# Extract href of subcategories
sub_links = []
for link in links: 
    sub_links.append(link["href"])

    
#################################################################################################
#------------------------------------ Extract Course Links -------------------------------------#
#################################################################################################
# Initialise webdriver
delay = 15
driver = webdriver.Chrome("/Users/Desktop/chromedriver")
course_links = []
filters = ["popularity", "highest-rated", "newest"]

# Iterate through each subcategory
for sub_link in sub_links: 
    sub_url = main_url + sub_link
    
    # Loop through 5 pages
    for fil in filters:
        # Apply filters 
        for i in range(1, 4):
            courses_url = "{0}?p={1}&sort={2}".format(sub_url, str(i), fil)
            driver.get(courses_url)
            try: 
                WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 
                                                                                   "course-list--container--3zXPS")))
            except TimeoutException: 
                print("Loading exceeds delay time")
            else: 
                course_soup = BeautifulSoup(driver.page_source, "html.parser")
                course_list = course_soup.find("div", class_="course-list--container--3zXPS")
                courses = course_list.find_all("a", class_="udlite-custom-focus-visible browse-course-card--link--3KIkQ")

                for course in courses: 
                    course_links.append(course["href"])

            # Sleep
            time.sleep(np.random.randint(1,5))

    # Free courses
    free_url = "{0}?p=1&price=price-free".format(sub_url)
    driver.get(courses_url)
    try: 
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 
                                                                           "course-list--container--3zXPS")))
    except TimeoutException: 
        print("Loading exceeds delay time")
    else: 
        course_soup = BeautifulSoup(driver.page_source, "html.parser")
        course_list = course_soup.find("div", class_="course-list--container--3zXPS")
        courses = course_list.find_all("a", class_="udlite-custom-focus-visible browse-course-card--link--3KIkQ")

        for course in courses: 
            course_links.append(course["href"])

            
#################################################################################################
#------------------------------------ Cleaning Course Links ------------------------------------#
#################################################################################################

# Remove duplicated courses within course links 
course_links_unique = list(set(course_links))

df_all = pd.DataFrame()


#################################################################################################
#------------------------------------ Extract Course Details -----------------------------------#
#################################################################################################

# Iterating through each course link
for course_link in course_links_unique:
   
    # Parse course html
    course_url = "{0}{1}".format(main_url, course_link)
    course_page = requests.get(course_url)
    course_soup = BeautifulSoup(course_page.content, "html.parser")
    course_page.close()
    
    # Ensuring valid links
    if course_soup is None: 
        continue
    else: 
        
        # Extract details part 1
        details = json.loads(course_soup.find('script', type='application/ld+json').string.replace("\n", "").strip())

        # Title 
        title = details[0]["name"]

        # Ratings
        try: 
            overall_rating = details[0]["aggregateRating"]["ratingValue"]
            best_rating = details[0]["aggregateRating"]["bestRating"]
            worst_rating = details[0]["aggregateRating"]["worstRating"]
            num_of_ratings = details[0]["aggregateRating"]["ratingCount"]
        except: 
            overall_rating = "0"
            best_rating = "0"
            worst_rating = "0"
            num_of_ratings = "0"

        # Categories
        category = details[1]["itemListElement"][0]["name"]
        subcategory = details[1]["itemListElement"][1]["name"]
        try: 
            topic = details[1]["itemListElement"][2]["name"]
        except: 
            topic = ""

        # Instructor 
        instructor = details[0]["creator"][0]["name"]

        
        try: 
            # Extracting details part 2
            details_1 = json.loads(course_soup.find("div", class_="ud-component--course-landing-page-udlite--sidebar-container").                                   get("data-component-props"))

            # SkillsFuture
            skillsfuture = details_1["componentProps"]["incentives"]["is_skills_future"]

            # No. of Practive Tests
            num_of_practice_tests = details_1["componentProps"]["incentives"]["num_practice_tests"]

            # No. of articles 
            num_of_articles = details_1["componentProps"]["incentives"]["num_articles"]

            # No. of coding exercises
            num_of_coding_exercises = details_1["componentProps"]["incentives"]["num_coding_exercises"]

            # Video duration 
            video_duration = details_1["componentProps"]["incentives"]["video_content_length"]

            # No. of additional resources 
            num_of_additional_resources = details_1["componentProps"]["incentives"]["num_additional_resources"]
        
        except: 
            skillsfuture = "False"
            num_of_practice_tests = "0"
            num_of_articles = "0"
            num_of_coding_exercises = "0"
            video_duration = np.nan
            num_of_additional_resources = "0"
            
            

        # Bestseller 
        bestseller_soup = course_soup.find("span", class_="udlite-badge udlite-badge-bestseller udlite-heading-xs")
        if bestseller_soup == None: 
            bestseller = "No"
        elif "Bestseller" in bestseller_soup.text: 
            bestseller = "Yes"

            
#################################################################################################
#------------------------------------- Extract Course Price ------------------------------------#
#################################################################################################

        # Obtain course ID
        course_id = course_soup.find("body").get("data-clp-course-id")
        price_api = "https://www.udemy.com/api-2.0/pricing/?course_ids=" + course_id +         "&fields[pricing_result]=price,discount_price,list_price,price_detail,price_serve_tracking_id"
        prices_page = requests.get(price_api)
        prices = prices_page.json()

        price = prices["courses"][course_id]["list_price"]["amount"]
        discounted_price = prices["courses"][course_id]["discount_price"]
        prices_page.close()

        
#################################################################################################
#-------------------------------------- Combining details --------------------------------------#
#################################################################################################
        course_df = pd.DataFrame([{
            "ID": course_id, 
            "Title": title, 
            "Overall_Rating": overall_rating, 
            "Best_Rating": best_rating, 
            "Worst_Rating": worst_rating, 
            "No_of_Ratings": num_of_ratings,
            "Category": category, 
            "Subcategory": subcategory, 
            "Topic": topic, 
            "Instructor": instructor,
            "Language": language, 
            "SkillsFuture": skillsfuture, 
            "No_of_Practice_Test": num_of_practice_tests, 
            "No_of_Articles": num_of_articles, 
            "No_of_Coding_Exercises": num_of_coding_exercises,
            "Video_Duration": video_duration, 
            "No_of_Additional_Resources": num_of_additional_resources, 
            "Bestseller": bestseller, 
            "Price": price, 
            "Discounted_Price": discounted_price
        }])
        df_all = pd.concat([course_df, df_all])
        
        # Sleep
        time.sleep(np.random.randint(1,5))
                
print("done")

#################################################################################################
#---------------------------------------- Exporting Data ---------------------------------------#
#################################################################################################

# Ensure no duplicated courses within df
df_all.drop_duplicates(subset=["ID"], inplace=True)

# Export data to raw csv file 
df_all.to_csv("Udemy_Raw.csv")




