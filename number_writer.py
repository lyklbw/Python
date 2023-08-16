import json

number=[1,2,3,4,5,6,7,8,9,10]

filename='number.json'

with open(filename,'w') as f_obj:
    json.dump(number,f_obj)#数json.dump() 接受两个实参：要存储的数据以及可用于存储数据的文件对象