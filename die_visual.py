from die import Die
import pygal



die_1=Die()

die_2=Die(10)
results=[0 for x in range(16)] # list=[0,0,0,0,0,0]

for roll_num in range(1000):
    result=die_1.roll()+die_2.roll()
    results[result-1]+=1

hist=pygal.Bar()
hist.title="Results of rolling one D6 1000 times."
hist.x_labels=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D6+D10',results)
hist.render_to_file('die_visual.svg')

