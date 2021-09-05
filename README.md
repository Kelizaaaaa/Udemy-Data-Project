# Udemy Data Project
 A data project to explore data collected from Udemy's webpage

## Files
/Data/Udemy_Raw.csv --> Contains raw data extracted from Udemy <br> 
/Data/Udemy_Clean.csv --> Cleaned version of raw data
Data Collection - Udemy Scrape.py --> Used for web scrapping of Udemy <br>
Data Cleaning.ipynb --> Clean raw data obtained


## Data Collection Method
Data was scrapped using a combination of Selenium and BeautifulSoup to obtain information from Udemy's webpage (https://www.udemy.com/). To obtain a variety of data, course details from various subcategories were scrapped, and it was ensured that these courses were from a good mix of filters used. These filters ranked courses based on popularity, highest ratings, newest courses and free courses. 

## Data Cleaning
The data was relatively clean because there was control and customization during the web scrapping. In general, cleaning of data was quite minimal. 

## Data Details
The data file (Udemy_Clean.csv) consists of the following columns: <br>
1. Title: Title of Udemy course
2. Overall_Rating: Overall average rating given by users who have taken the course
3. Best_Rating: Highest rating given by users who have taken the course
4. Worst_Rating: Lowest rating given by users who have taken the course
5. No_of_Ratings: Total number of ratings given for the course
6. Category: First level of categorization for course
7. Subcategory: Second level of categorization for course
8. Topic: Third level of categorization for course
9. Instructor: Name of instructor of course
10. Language: Original language in which course is conducted in
11. SkillsFuture: Indicates whether course is SkillsFuture Credit eligible 
    - For more information about SkillsFuture, you can refer to this link: https://www.myskillsfuture.gov.sg/content/portal/en/training-exchange/course-landing.html?cid=a1:Google%7Ca2:SEM%7Ca3:%2001062021_linkto_landing-courses
12. No_of_Practice_Test: Number of practice tests provided as part of the course materials
13. No_of_Articles: Number of articles provided as part of the course materials
14. No_of_Coding_Exercises: Number of coding exercises provided as part of the course materials
15. Video_Duration_Hr: Total duration of course videos (in hours)
16. Bestseller: Whether or not course is a bestseller
17. Price: Original price of course
18. Discounted_Price: Price of course after discount

