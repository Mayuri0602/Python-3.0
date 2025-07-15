# Dictionary: mutable and ordered, stored values in key-value pairs
data = {}
print(type(data))  #empty dictionary

s1 = {1,2,3,1,2,1}
print(s1)

data = {'name':['mayu','gunu'], 'aadhar': 1235535, 'mobile_no':67857585}
print(data['aadhar']) 

data['aadhar'] = [data['aadhar'],87789]
print(data)

a=data['name']
print(a[1])

data={'name':['shekhar','abc','raghav'],'name':"random name",'aadhar':123456,'mobile_no':136546}
print(data['name'])

data={'a':'shekhar','b':[34,5,6],'c':{45,56,7},'t':(34,56,6)}

# data['t'][-1]=90           #tuples are immutable
# print(data['t'][-1])

d1={12:"twelve",True:"right",3.14:"value of pi",'shekhar':'it is a name'}
print(d1)
d1[True]='wrong'
print(d1)

data={'a':123,'b':354,'c':78}
# data.clear()
# print(data)
print(data.items())     #dict_items([('a', 123), ('b', 354), ('c', 78)])
print(data.values())    #dict_values([123, 354, 78])
print(data.keys())      #dict_keys(['a', 'b', 'c'])
print(data.get('a'))
data.setdefault('x',56)
print(data['x'])        
data['pqr']='jaipur'    
print(data)


 

