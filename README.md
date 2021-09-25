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

## Exploratory Data Analysis 
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


## Project 1: Price Mechanism 
### Model 
Objective: To build a model to determine the price mechanism of Udemy courses <br>
Models: Multiple Linear Regression, Random Forest Regression, Gradient Boosting Models (XGBoost, LightGM) <br> 
Evaluation metrics: Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE) <br> 
- RSME and MAE are commonly used metrics to evaluate models especially on platforms like Kaggle. 
- However, both metrics have limitations. 
    - RSME penalizes larger errors more than smaller errors which will inflate the mean error score. 
    - MAE doesn't differentiate between the types of errors and assumes a linear relationship with errors. 
- Hence, we can combine both where MAE will be used for adjustments within models for optimization and RSME will be used to evaluate the different models. 

### Evaluation 
The root mean squared error (RMSE) of log(observed price) and log(actual price) is used to ensure that the errors for the more costly and less costly courses will affect the results to the same extent. 
Model Scores (RMSE)
- Multiple Linear Regression: 0.633
- Random Forest Regression: 0.574
- XGB Regression: 0.571
- LightGBM Regression: 0.561

Best performing model: Light Gradient Boosting Machine Model 

Note: However, RMSE is still relatively high and unsatisfactory. This could be due to limitations of the assumptions made for the project which we will discuss in a later section. 

## Project 2: Discount Classification
### Model 
Objective: To build a model to classify whether a course will be given a discount <br> 
Models: Decision Tree Classifier, Random Forest Classifier, Logistic Regression, Naive Bayes Classification, Support Vector Classifier <br> 
Evaluation metrics: Classification Accuracy, ROC Area Under Curve <br>
- ROC helps us understand the ability of the model to classify accurately based on probabilities 
    - Hence, we will use ROC area under curve to tune the various models and improve it
- Accuracy score shows us the number of predictions that have been accurately classified when compared with the actual value. 
    - This metric will be used for comparison between the models to compare the actual performance. 

### Evalution
Model Scores (Classification Accuracy)
- Decision Tree, Score: 90.99%
- Random Forest, Score: 85.19%
- Logistic Regression, Score: 92.35%
- Naive Bayes, Score: 23.21%
- Support Vector, Score: 92.96%

Best performing model: Support Vector Classifier 

## Project Limitations
One limitation of this project is related to the biggest assumption made, which is that is it assumed that Udemy's price mechanism follows a rational relationship where various related factors, such as rating of the course etc. However, this assumption fails to take into account the fact that Udemy uses discounts as a marketing scheme (Urgency marketing). They often aritificially change prices based on your browser cookie. More can be read on this website: https://skillscouter.com/how-often-does-udemy-have-sales/. <br> 
Therefore this shows that it is hard to estimate the actual pricing of courses because the actual price of Udemy courses can in reality be defined as the discounted price since it is a gimmick to entice consumers to buy the courses by having a decoy option. 











