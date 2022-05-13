# What I Have Done
- Exported an xml file from Apple Health
- Found all heart rate data using BeautifulSoup
- created a df that starts with the first day of school and ends on the last day
- filtered out all of the weekend days
- created multiple bins
    - hr_bin based on values
        - normal between 60 and 100
        - high > 100
        - low < 60
    - time_bin based on the time of the day (used period of school)
    - day_week bin based on the day of the week with 0 = Monday and 4 = Friday

--------------------------------------------------------------------------------

# What Needs To Be Done
## Charts for the data
1) bar chart for which period had the highest max hr for each day
    - line chart over the bar chart, showing the average for that day 
