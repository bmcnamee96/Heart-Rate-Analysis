# Health Data

## Check Out the [Dashboard Here](https://public.tableau.com/shared/NHTTPYNGP?:display_count=n&:origin=viz_share_link "Dashboard Here")

## Overview
- The purpose of this analysis was to examine my heart rate data while working at an elementary school. 
- After data cleaning a machine learning model was used to try and determine if the time of the day and the day of the week could be used to predict a heart rate. 

## Packages and Libraries
- Python
  - Jupyter Notebook
  - Pandas
  - Beautiful Soup
  - Datetime
  - Numpy
  - SkLearn (LinearRegression, RandomForestClassifier)
  - Matplotlib
  - Bioinfokit
 - Tableau

## The Data
- Heart rate data was calculated using an Apple Watch and was then exported using the Apple Health App as an xml file.
- Apple Health tracks a lot of different metrics but I was only interested in 'HKQuantityTypeIdentifierHeartRate'.
  - This data included: sourceName, device, unit (count/min), creationDate, startDate, endDate, value
  - creationDate and value were the only two variables that were kept
  - creationDate included the date in YYYY-MM-DD form and time in HH-MM-SS form.

![initial_df](https://github.com/bmcnamee96/health_data/blob/main/Pictures/initial_df.png)

The data was put into a dataframe after using Beautiful Soup to parse the xml file.  This dataframe was then exported to a csv file for easy retrieval in future use.

## Data Processing
- 125,156 rows were in the initial dataset dating back to 2015.  
- I was only interested in data ranging from 2022-03-28 to 2022-06-09 (the dates that I was working).

### Binning
#### Heart Rate Values
- Using the American Heart Association website I determined bins for the heart rate values
  - greater than 195 = Dangerous (age - 220)
  - 125-195 = High
  - 65-125 = Normal
  - less than 65 = Low

#### Time of Day
- My work day was separated into periods where I would work with different students and different age groups. I decided to split up the day into bins separating those periods.
  - 0 = time away from work
  - 1 = showing up to work and before my first period
  - 2 = first period
  - 3 = second period
  - 4 = lunch period
  - 5 = third period
  - 6 = fourth period
  - 7 = fifth period
  - 8 = sixth period
  - 9 = dismissal

#### Day of Week
- I was only interested in analyzing data from week days (Monday - Friday) because I did not work on the weekend.
  - 0 = Monday
  - 1 = Tuesday
  - 2 = Wednesday
  - 3 = Thursday
  - 4 = Friday

After all binning was completed, I used the date range that I worked to create a new dataframe called school_df. This dataframe only included days that I was at work. The length of the original dataframe to the school_df had been shortened to 11,294 rows.

![school_df](https://github.com/bmcnamee96/health_data/blob/main/Pictures/school_df.png)

## Statistical Analysis
Using bioinfokit's stat package a Tukey-Kramer test was run to determine significance between (< 0.05) all the day_sections and all day_of_week values.

A Tukey-Kramer test compares each group to each other (A-B, A-C, A-D, B-C, etc.) when there is an unequal sample size. 

### Day of Week
- There is a statistical significant difference in the average heart rate values and the day of the week (p = 0.001000). The below picture shows that there is a significant difference between every group compared.

![tukey_dow](https://github.com/bmcnamee96/health_data/blob/main/Pictures/day_of_week_tukey.png)

### Day Sections
- There is a significant difference between:
  - section 0 and all other sections of the day (p = 0.001000)
  - section 1 and sections 3 and 4 (p = 0.001000)
  - section 2 and section 9 (p = 0.014156)
  - section 4 and sections 6 (p = 0.003039) and 9 (p = 0.001000)
  - section 6 and section 3 (p = 0.008781)
  - section 9 and section 3 (p = 0.001000)

![tukey_ds](https://github.com/bmcnamee96/health_data/blob/main/Pictures/day_sections_tukey.png)

## Machine Learning
Using the actual values for the heart rates does not allow a machine learning model to accurately predict because of the granularity. Bins were created for the heart rate values to reduce the variance.  The bins from data processing were not used for the model because of the range differences for each bin. The bins for the machine learning model used 8 bins that were evenly spaced.

- Target = values_bins (the heart rate data after being binned)
- Features = day_sections (time of the day 'periods') and day_of_week

### Linear Regression
- The linear regression model was not able to accurately predict a heart rate value and had a model score of 11.27%.

### Random Forest Classifier
- Random forest classifier improved a lot over the linear regression but was still not very good at predicting heart rate. The training score was 47.46% and the testing score was 48.16%.  This means that the model will be correct about 50% of the time when trying to predict a heart rate.
- The main reason that this occured was because of the high number of values within certain bins.  The model determined that if it predicted either bin 2 or bin 3 it would be correct 50% of the time.  This can be seen when looking at a value counts of the predicted_values and values_bins.

![predictions](https://github.com/bmcnamee96/health_data/blob/main/Pictures/predictions.png)

#### Feature Importance
Random forest classifier includes a feature importance determinant that can be used to see which features have the most impact on the target. 
- In our model both features had a considerable impact on the target.

![feature_importance](https://github.com/bmcnamee96/health_data/blob/main/Pictures/features.png)

## Conclusion
In conclusion there was no way to predict heart rate when using the time of day and day of the week.

### Future 
- More data using a larger time frame would be better. After all processing, the data was only looking at a 31 day range. Using data from an entire year or more would be able to provide trends and allow the model to more accurately predict the heart rate.
- Possibly removing the time not at work could also help the model. There was a much higher count of values that were within the 0 bin because it included all time not at work. This data was left in to try and determine if the heart rate changed drastically while at or off of work.
