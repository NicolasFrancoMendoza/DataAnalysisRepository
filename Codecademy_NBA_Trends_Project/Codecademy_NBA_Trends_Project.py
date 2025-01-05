import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

#Using the pts column from the nba_2010 DataFrame, create two series named knicks_pts (fran_id = "Knicks") and nets_pts(fran_id = "Nets") that represent the points each team has scored in their games.
knicks_pts = nba_2010[nba_2010.fran_id == 'Knicks']['pts']
nets_pts = nba_2010[nba_2010.fran_id == 'Nets']['pts']

#Calculate the difference between the two teams’ average points scored and save the result as diff_means_2010. Based on this value, do you think fran_id and pts are associated? Why or why not?
diff_means_2010 = knicks_pts.mean() - nets_pts.mean()
print(diff_means_2010)

#Create a set of overlapping histograms that can be used to compare the points scored for the Knicks compared to the Nets. Use the series you created in the previous step (1) and the code below to create the plot. Do the distributions appear to be the same?
plt.hist(knicks_pts, alpha = 0.8, normed = True, label = 'Knicks')
plt.hist(nets_pts, alpha = 0.8, normed = True, label = 'Nets')
#note that density is used for newer version of matplotlib
plt.legend()
plt.title("2010 Season")
plt.show()

#First, calculate the mean difference between the two teams points scored. Save and print the value as diff_means_2014. Did the difference in points get larger or smaller in 2014? Then, plot the overlapping histograms. Does the mean difference you calculated make sense?
knicks_pts_14 = nba_2014[nba_2014.fran_id == 'Knicks']['pts']
nets_pts_14 = nba_2014[nba_2014.fran_id == 'Nets']['pts']

diff_means_2014 = knicks_pts_14.mean() - nets_pts_14.mean()
print(diff_means_2014)

plt.hist(knicks_pts_14, alpha = .8, normed = True, label = 'Knicks')
plt.hist(nets_pts_14, alpha = .8, normed = True, label = 'Nets')
plt.legend()
plt.title("2014 Season")
plt.show()

#Using nba_2010, generate side-by-side boxplots with points scored (pts) on the y-axis and team (fran_id) on the x-axis. Is there any overlap between the boxes? Does this chart suggest that fran_id and pts are associated? Which pairs of teams, if any, earn different average scores per game?
sns.boxplot(data = nba_2010, x = 'fran_id', y = 'pts')
plt.show()

#Save your result as location_result_freq and print your result. Based on this table, do you think the variables are associated?`
location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)

#Convert this table of frequencies to a table of proportions and save the result as location_result_proportions.
location_result_proportions = location_result_freq/len(nba_2010)

#Using the contingency table created in the previous exercise (Ex. 7), calculate the expected contingency table (if there were no association) and the Chi-Square statistic. Does the actual contingency table look similar to the expected table — or different? Based on this output, do you think there is an association between these variables?
chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)

#Using nba_2010, calculate the covariance between forecast (538's projected win probability) and point_diff (the margin of victory/defeat) in the dataset. Save and print your result. Looking at the matrix, what is the covariance between these two variables?
point_diff_forecast_cov = np.cov(nba_2010.point_diff, nba_2010.forecast)

#Using nba_2010, calculate the correlation between forecast and point_diff. Call this point_diff_forecast_corr. Save and print your result. Does this value suggest an association between the two variables?
point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)

#Generate a scatter plot of forecast (on the x-axis) and point_diff (on the y-axis). Does the correlation value make sense?
plt.clf() #to clear the previous plot
plt.scatter('forecast', 'point_diff', data=nba_2010)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.show()
