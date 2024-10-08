from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides

for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)    

#Histogram of result

x_values = list(range(1, max_result+1)) # we use list because plotly doesn't accept range 
data = [Bar(x = x_values, y = frequencies)] 

x_axis_config = {'title': 'Result', 'dtick' : 1}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title='Relsuts of rolling the dice', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout' : my_layout}, filename='d6_d6.html')
