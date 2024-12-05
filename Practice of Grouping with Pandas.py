import codecademylib3
import pandas as pd

#Analyzing Ad Sources
#1
ad_clicks = pd.read_csv('ad_clicks.csv')
#print(ad_clicks.head())

#2
ad_clicks.groupby("utm_source").user_id.count().reset_index

#3
ad_clicks ["is_click"] = ~ad_clicks\
   .ad_click_timestamp.isnull() #the expresion "~" significa inversión, es decir acá se busca los invertido a NULL
print(ad_clicks.head())

#4
clicks_by_source = ad_clicks\
   .groupby(['utm_source',
             'is_click'])\
   .user_id.count()\
   .reset_index()

#5
clicks_pivot = clicks_by_source\
   .pivot(index='utm_source',
          columns='is_click',
          values='user_id')\
   .reset_index()

#6
clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False]) * 100

print (clicks_pivot)


#Analyzing an A/B Test
#7
AorB = ad_clicks\
   .groupby("experimental_group")\
   .user_id.count()\
   .reset_index()

#8 Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.



#9 The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.
# Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.




#10 For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.




#11Compare the results for A and B. What happened over the course of the week?
#Do you recommend that your company use Ad A or Ad B? 
