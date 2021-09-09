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
This dataset consists of 16,429 observations (rows) and 20 variables (columns). <br> 
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


## Project 1: Price Mechanism 
### Exploratory Data Analysis 
An analysis of the Udemy data was conducted to investigate the relationship between various features and the target variable, "Price". Upon investigating, there were a few interesting observations which are as follows: 
- The number of practice tests has the lowest correlation of -0.08 with price. 
    - It is expected that more practice tests would translate to more course material that is provided, and hence a higher price. 
    - Furthermore, it is a negative relationship. This is shocking because it is logical that if more course materials are provided, the price would be higher. However, this is the opposite where more course materials translate to a lower price. This relationship could possibly be due to a confounder. 
- An interesting finding was that some of the free courses provided were relatively highly rated (3.7 and above). 
    - Based on the samples taken, the course content quality is good despite the fact that the course is free. 
- Safety & First Aid was the subcategory with the lowest average price. 
    - Safety and first aid are vital life-saving skills hence I would have expected that they would be quite popular and priced highly. 
    - One plausible explanation is that the nature of such causes would require in-person classes due to practical components such as CPR, hence it may not be as desirable online. 
    - Another possible reason would be that as a form of encouragement for users to pick up such important skills, Udemy would offer these courses for free. 
- Discounted courses had a lower average price compared to courses that are not discounted. 
    - Discounts could be given for more pricey courses in order to make them more affordable and encourage users to pick up these courses. 
    - But the other approach would be to create a price discrimination where customers are charged a premium for a quality course. Thus, this creates a wider variety for users where they can choose between the various classes of courses. 

### Model 
Objective: To build a model to determine the price mechanism of Udemy courses <br>
Models: Multiple Linear Regression, Random Forest Regression, Gradient Boosting Models (XGBoost, LightGM)
Evaluation metrics: Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE)
- RSME and MAE are commonly used metrics to evaluate models especially on platforms like Kaggle. 
- However, both metrics have limitations. 
    - RSME penalizes larger errors more than smaller errors which will inflate the mean error score. 
    - MAE doesn't differentiate between the types of errors and assumes a linear relationship with errors. 
- Hence, we can combine both and use them to evaluate the models, to provide second opinions. 

