import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics

df = pd.read_csv("height-weight.csv")
weight = df["Weight(Pounds)"].tolist()
fig = ff.create_distplot([weight], ["Weight"], show_hist=False)


mean = statistics.mean(weight)
sd = statistics.stdev(weight)

first_st_deviation_start, first_st_deviation_end = mean-sd, mean+sd
second_st_deviation_start, second_st_deviation_end = mean-(2*sd), mean+(2*sd)
third_st_deviation_start, third_st_deviation_end = mean-(3*sd), mean+(3*sd)

fig.add_trace(go.Scatter(x=[mean, mean], y = [0, 0.04], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_st_deviation_start, first_st_deviation_start], y = [0, 0.04], mode="lines", name="FirstDevationStart"))
fig.add_trace(go.Scatter(x=[first_st_deviation_end, first_st_deviation_end], y = [0, 0.04], mode="lines", name="FirstDevationEnd"))
fig.add_trace(go.Scatter(x=[second_st_deviation_start, second_st_deviation_start], y = [0, 0.04], mode="lines", name="SecondDevationStart"))
fig.add_trace(go.Scatter(x=[second_st_deviation_end, second_st_deviation_end], y = [0, 0.04], mode="lines", name="SecondDevationEnd"))
fig.show()

data_in_1st_st_deviation = [result for result in weight if result > first_st_deviation_start and result < first_st_deviation_end]
data_in_2nd_st_deviation = [result for result in weight if result > second_st_deviation_start and result < second_st_deviation_end]
data_in_3rd_st_deviation = [result for result in weight if result > third_st_deviation_start and result < third_st_deviation_end]
print("Mean of this data is {}".format(mean))
print("Standard Deviation is {}".format(sd))
print("{}% of data lies within 1 standard deviation".format(len(data_in_1st_st_deviation)*100.0/len(weight)))
print("{}% of data lies within 2 standard deviation".format(len(data_in_2nd_st_deviation)*100.0/len(weight)))
print("{}% of data lies within 3 standard deviation".format(len(data_in_3rd_st_deviation)*100.0/len(weight)))