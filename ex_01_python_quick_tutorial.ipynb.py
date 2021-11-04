print("Moring")
print("_"*50)

x=5
func=5*x+6
print(func)
print("_"*50)

x=4
monadic_equation=3*x
print("monadic_equation={:.2f}".format(monadic_equation))
print("_"*50)

city_name="songyuan"
coordinate_longitude=124.823608
coordiante_latitude=45.118243
print("The longitude of the songyuan coordinate is {lon:.2f}, and the latitude is {lat:.2f}.".format(lon=coordinate_longitude,lat=coordiante_latitude))
print("_"*50)

x,y,b=2,9,7 
func_2=3*x+4*y-b
print("func_2={}".format(func_2))
print("_"*50)

lst_n=list(range(4,20,4))
print(lst_n)
print("The list length={}".format(len(lst_n)))
print("Maximum value={}".format(max(lst_n)))
print("Minimum value={}".format(min(lst_n)))
print("_"*50)

lst_s=list(map(chr,range(65,75)))
print(lst_s)
print("[-2:-1]->{}".format(lst_s[-2:-1]))
print("[-3:]->{}".format(lst_s[-3:]))
print(lst_s)
print("[0:3:2]->{}".format(lst_s[0:3:2]))
print("[9:3:-2]->{}".format(lst_s[9:3:-2]))
print("[:]->{}",format(lst_s[:]))
print("_"*50)

help(chr)
print("_"*50)

lst_s=list(map(chr,range(65,75)))
print(lst_s)
lst_s[4]=36
print("lst_s[4]=36->{}".format(lst_s))
lst_none=lst_s+[None]*3
print("lst_s+[None]*3->{}".format(lst_none))
lst_none[-2:]=list(range(100,105,2))
print("lst_none[-2:]=list(range(100,105,2))->{}".format(lst_none))
lst_none[1:1]=[0,0,0,12]
print("lst_none[1:1]=[0,0,0,12]->{}".format(lst_none))
del lst_none[-2:]
print("del lst_none[-2:]->{}".format(lst_none))
print("_"*50)

lst_s=list(map(chr,range(100,105)))
print(lst_s)
lst_s.append(10)
#append() #方法用于在列表末尾添加新的对象。
print("lst_s.append(10)->{}".format(lst_s))
lst_s.append(list(range(50,80,5)))
print("lst_s.append(list(range(50,80,5)))->{}".format(lst_s))
lst_spechars=['*','.','*']
lst_s.extend(lst_spechars)
print("lst_s.extend(lst_spechars)->{}".format(lst_s))
print("lst_s.count('*')={}".format(lst_s.count('*')))
print("lst_s.index('e')={}".format(lst_s.index('e')))
#Python index 方法检测字符串中是否包含子字符串 str;是否在list中有e
lst_s.insert(3,[1000,1200,1500])
#insert() 函数用于将指定对象插入列表的指定位置
print("lst_s.insert(2,[1000,1200,1500])->{}".format(lst_s))
print("lst_s.pop(5)_popup->{}".format(lst_s.pop(5)))
print("lst_s.pop(7)_retention->{}".format(lst_s))
lst_s.remove('.')
print("lst_s.remove('.')_retention->{}".format(lst_s))
print("_"*50)

list_n=[2,22,6,63,12,17]
list_n.sort()
print("list_n.sort()->{}".format(list_n))
print("_"*50)

tuple_1=2,5,7,
print("tuple_1=2,5,7,->{}".format(tuple_1))
print("8*(10+3)->{}".format(8*(10+3)))
print("tuple((4,8,9))->{}".format(tuple((4,8,9)))) 
print("tuple([3,6,9])->{}".format(tuple([3,6,9]))) 
print("_"*50)

import random
items=[(0,[i for i in range(7)]),(1,[random.sample(list(range(150,200,1)),3)]),(2,'morning')] 
print("items->{}".format(items))
dic=dict(items)
print("dic=dict(items)->{}".format(dic))
print("dic[2]->{}".format(dic[2]))
print("_"*50)
print("len(dic)->{}".format(len(dic)))
#Python 字典(Dictionary) len() 函数计算字典元素个数
dic[3]=(random.random(),random.uniform(10,30))
print("dic[3]=(random.random(),random.uniform(10,30))->{}".format(dic))
del dic[2]
print("del dic[1]->{}".format(dic))
print("3 in dic->{}".format(3 in dic))
print("8 in dic->{}".format(5 in dic))
print("dic.keys()->{}".format(dic.keys()))
print("dic.values()->{}".format(dic.values()))
print("dic.items()->{}".format(dic.items()))
print("list(dic.keys())->{}".format(list(dic.keys())))
print("_"*50)
for k,v in enumerate(dic.items()):
    print(k,v)
print("_"*50)

lst_A=list(range(1,20,3))
lst_B=list(range(200,350,25))
print("lst_A={},lst_B={}".format(lst_A,lst_B))
dic_2={0:lst_A,1:lst_B}
print("dic_2={}".format(dic_2))
dic_assignment=dic_2
print("dic_assignment={}".format(dic_assignment))
dic_2.clear()
print("dic_2.clear()->{}".format(dic_2))
print("dic_assignment={}".format(dic_assignment))
dic_2[5]=list(range(2,16,2))
print("dic_2[5]=list(range(2,16,2))->{}".format(dic_2))
dic_copy=dic_2.copy()
print("dic_copy=dic_2.copy()->{}".format(dic_copy))
dic_2[8]=[5,7]
print("dic_2[8]=[5,7]->{}".format(dic_2))
print("dic_copy={}".format(dic_copy))
dic_copy[5].remove(4)
print("dic_copy[5].remove(4)->{}".format(dic_copy))
dic_copy.setdefault(6,[88,99])
print("dic_copy.setdefault(6,[88,99])->{}".format(dic_copy))
dic_2.pop(5) 
print("dic_2.pop(5)->{}".format(dic_2))
dic_update={8:[5,7,6,3,2],9:[3,2,33,55,66]}
print("dic_update={}".format(dic_update))
dic_2.update(dic_update)
print("dic_2.update(dic_update->{}".format(dic_2))
print("dic_2.get(9)->{}".format(dic_2.get(9)))
dic_2.popitem()
print("dic_2.popitem()->{}".format(dic_2))
print("_"*50)
dic_3={}.fromkeys([0,2,4,6,8,'Ah'])
print("dic_3={}"+".fromkeys([0,2,4,6,48,'Ah'])->{}".format(dic_3))
print("_"*50)

lst_s_3=list("i don't know how to do")
print("lst_s_3=list(\"i don't know how to do\")->{}".format(lst_s_3)) #"\" escape character
print("\"i don't know\"+\"how to do\"->{}".format("i don't know"+" how to do"))
print("\"+\".join(str(123456))->{}".format("+".join(str(123456))))
print("len(\"i don't know how to do\")->{}".format(len("i don't know how to do")))
coordinates="124.823608,45.118243"
print("coordinates.split(\",\")->{}".format(coordinates.split(",")))
print("eval(coordinates)->{}".format(eval(coordinates)))
print("\"i don't know how to do\".lower()->{}".format("i don't know how to do".lower()))
print("\"i don't know how to do\".upper()->{}".format("i don't know how to do".upper()))
print("\"i don't know how to do\"[6:]->{}".format("i don't know how to do"[6:]))
print("\"i don't know how to do\".strip()->{}".format("i don't know how to do".strip()))
print("\"i don't know how to do\".replace(\"a\",\"b\")->{}".format("i don't know how to do".replace("a","b")))
hello_lst=list("i don't know how to do")
hello_lst.sort()
print("hello_lst.sort()>{}".format(hello_lst))
print("\"i don't know how to do\".find(\"o\")->{}".format("i don't know how to do".find("o")))
print("_"*50)

format_str="%s and %s"
values=("xiaoming","xiaohong")
new_str=format_str % values
print("new_str=format_str % values->{}".format(new_str))
format_str_2="Pi with three decimals:%.4f,and enter a value with percent sign:%.1f %%"
from math import pi
new_str_2=format_str_2 % (pi,3.14)
print("new_str_2=format_str_2 % (pi,3.14)->{}".format(new_str_2))
print("_"*50)

format_str_3="%10f,%.2f,%.5s,%.*s,%d,%x,%f"
new_str_3=format_str_3%(pi,pi,"CA",5,"CA",52,52,pi)
print("{}".format(new_str_3))
print("_"*50)

from string import Template
s_template_1=Template("$x,1,$x!")
s_1=s_template_1.substitute(x="xiaohong")
print("s_1=s_template_1.substitute(x=\"xiaohong\")->{}".format(s_1))
s_template_2=Template("${x}thon is amazing!")
s_2=s_template_2.substitute(x="ca")
print("s_2=s_template_2.substitute(x=\"ca\")->{}".format(s_2))
s_template_3=Template("$x and $y are friends!")
substitute_dict=dict([('x','xiaohong'),('y','xiaoming')])
print("substitute_dict={}".format(substitute_dict))
s_3=s_template_3.substitute(substitute_dict)
print("s_3=s_template_3.substitute(substitute_dict)->{}".format(s_3))
print("_"*50)

import re
pattern_1='xiaohong'
text="xiaohong is a girl!"
print("re.findall(pattern_1,text)->{}".format(re.findall(pattern_1,text)))
pattern_2='xiaoming'
print("re.findall(pattern_2,text)->{}".format(re.findall(pattern_2,text)))
print("_"*50)

print("re.findall('.ming','xiao ming!')->{}".format(re.findall('.ython','xiao ming!')))
print("re.findall('.ming','xiao mming!')->{}".format(re.findall('.ython','xiao mming!')))
print("re.findall('.ming','xiao lming!')->{}".format(re.findall('.ython','xiao lming!')))
print("re.findall('.ming','xiao ing!')->{}".format(re.findall('.ython','xiao ing!')))
print("_"*50)

print("re.findall(r'w?cadesign\.cn,w+\.cadesign\.cn','cadesign.cn,www.cadesign.cn')->{}".format(re.findall(r'w?cadesign\.cn,w+\.cadesign\.cn','cadesign.cn,www.cadesign.cn')))
print("re.findall(r'w{2}"+"\.cadesign\.cn','www.cadesign.cn')->{}".format(re.findall(r'w{2}\.cadesign\.cn','www.cadesign.cn')))
print("re.findall(r'w{1,3}"+"\.cadesign\.cn','www.cadesign.cn')->{}".format(re.findall(r'w{1,3}\.cadesign\.cn','www.cadesign.cn')))
print("_"*50)

print("re.findall('[xi]*ng!','xiao ming!')->{}".format(re.findall('[Py]*thon!','xiao ming!')))
print("re.findall('[xi]*ng!','xiao ing!')->{}".format(re.findall('[Py]*thon!','xiao ing!')))
print("re.findall('[xi]*ng!','xiao ning!')->{}".format(re.findall('[Py]*thon!','xiao ning!')))
print("re.findall('[xi]*ng!','xiao mng!')->{}".format(re.findall('[Py]*thon!','xiao mng!')))
print("_"*50)

print("re.findall('hu|ji','hu')->{}".format(re.findall('hu|ji','hu')))
print("re.findall('hu|ji','ji')->{}".format(re.findall('hu|ji','ji')))
print("re.findall('hu|ji','hu and ji')->{}".format(re.findall('hu|ji','ji and hu')))
print("_"*50)

print("re.findall('\d','number=52')->{}".format(re.findall('\d','number=52')))
print("re.findall('\D','numb=10')->{}".format(re.findall('\D','numb=10')))
print("re.findall('[^0-9]','number=10')->{}".format(re.findall('[^0-9]','number=10')))
print("_"*50)

print("re.findall('[a-z]','ming')->{}".format(re.findall('[a-z]','ming-3.0')))
print("re.search('[a-z]+','ming')->{}".format(re.search('[a-z]+','ming')))
if re.search('[a-z]+','ming'):
    print("re.search('[a-z]+','ming')->what't up!")
print("re.split(',','xiao,,,,,,ming!')->{}".format(re.split(',','xiao,,,,,,ming!')))
print("re.sub('xiao','ming','xiao ming!')->{}".format(re.sub('xiao','ming','xiao ming!')))
pattern_compile=re.compile('ming')
print("pattern_compile.findall('xiao,,,,,,ming!')->{}".format(pattern_compile.findall('xiao,,,,,,ming!')))
if re.match('g','ming'):
    print("re.match('g','ming')->what's up!")
print("_"*50)

print("\'ming\'.find(\'ming\')->{}".format('ming'.find('ming')))
print("\'ming\'.find(\'ing\')->{}".format('ming'.find('ing')))
print("\'ming\'.find(\'i\')->{}".format('ming'.find('i')))
print("\'m\' in \'ming\'->{}".format('m' in 'ming'))
print("_"*50)

print("\'xi,,xiao,,xiao ming!\'.split(',')->{}".format( 'xi,,xiao,,xiao ming!'.split(',')))
print("\'xiaoming!\'.replace(\'ming\',\'hong\')->{}".format( 'xiaoming!'.replace('ming','hong')))
print("_"*50)
#匹配对象和组
match_1=re.match(r'www\.(.*)\..{3}','www.xvvxinyao.org')
print("match_1.gourp(1)->{}".format(match_1.group(1)))
print("match_1.start(1)->{}".format(match_1.start(1)))
print("match_1.end(1)->{}".format(match_1.end(1)))
print("match_1.span(1)->{}".format(match_1.span(1)))
match_2=re.match(r'www\.(.*)\.(.{3})','www.xvxinyao.org')
print("match_2.group(1)->{}".format(match_2.group(1)))
print("match_2.group(2)->{}".format(match_2.group(2)))
print("_"*50)
#for循环
lst_1=list(range(5,40,6))
print("lst_1={}".format(lst_1))
print("for i in lst_1:")
for i in lst_1:
    print(i)
print("for i in range(len(lst_1)):")
for i in range(len(lst_1)):
    print("idx={},val={}".format(i,lst_1[i]))   
dic_4=dict(a=3,b=3,c=6,d=2)
print("dic_4={}".format(dic_4))
print("for k in dic_4:")
for k in dic_4:
    print(k)
print("for k,v in dic_4.items():")
for k,v in dic_4.items():
    print("key={},val={}".format(k,v))
print("_"*50)
 #while循环
x=7
while x<=130:
    print("x={}".format(x))
    x+=15
print("_"*50)
x=7
while x<=150:
    print("x={}".format(x))
    x+=30 
    if x>=50:break    
import sys
print("sys.maxsize={}".format(sys.maxsize))
for i in range(sys.maxsize):
    print("i={}".format(i))  #?
    i+=30
    if i>=50:break
print("_"*50)
#并行迭代
lst_a=[0,2,3,6]
lst_b=['point_a','point_b','point_c','point_d']
zip_lst=zip(lst_a,lst_b) 
print("zip_lst=zip(lst_a,lst_b)->{}".format(zip_lst))
print("dict(zip_lst)->{}".format(dict(zip_lst)))
zip_lst=zip(lst_a,lst_b) 
for a,b in zip_lst:
    print(a,b)
zip_lst=zip(lst_a,lst_b)
a,b=zip(*zip_lst)
print("a={},b={}".format(a,b))
print("_"*50)
#编号迭代
lst_c=['point_a','point_b','point_c','point_d']
dic_4={}
for idx,value in enumerate(lst_c):
    dic_4[idx]=value
print("dic_4={}".format(dic_4))
print("dict((i,v) for i,v in enumerate(lst_c))->{}".format(dict((i,v) for i,v in enumerate(lst_c)))) 
for i,(a,b) in enumerate(zip(lst_a,lst_b)):
    print('%d:%s,%s'%(i,a,b))
print("_"*50)
#list comprehension(列表推导式)
print("[x*x for x in range(4,60,7) if x%2==0]->{}".format([x*x for x in range(4,60,7) if x%2==0]))
print("[(x,y) for x in range(4)for y in range(2)]->{}".format([(x,y) for x in range(4)for y in range(2)]))
print("[(x,y) for x,y in zip(range(4),range(2))]->{}".format([(x,y) for x,y in zip(range(4),range(2))]))
nested_list=[[a for a in range(5,12,4)],2,3,[b for b in range(60,100,7)],[[c for c in range(1000,2000,120)],3,9]]
print("[[a for a in range(5,12,4)],2,3,[b for b in range(60,100,7)],[[c for c in range(1000,2000,120)],3,9]]->{}".format(nested_list))
flatten_lst=lambda lst: [m for n_lst in lst for m in flatten_lst(n_lst)] if type(lst) is list else [lst] 
print("flatten_lst(nested_list)->{}".format(flatten_lst(nested_list)))
print("_"*50)


#条件语句模式
x=7
if x<0:
    print('负数')
elif x==0:
    print('等于0')
elif 0<x<10:
    print('大于0小于10')
else:
    print('大于0')
print("_"*50)
    #相等运算符==与同一性运算符is
x=y=[7,7,9]
z=[3,6,9]
print("x==y->{}".format(x==y))
print("x is y->{}".format(x is y))
print("x==z->{}".format(x==z))
print("x is z->{}".format(x is z))
print("x is not y->{}".format(x is not y))
print("x is not z->{}".format(x is not z))
print("id_x:{};id_y:{};id_z:{}".format(id(x),id(y),id(z)))
del x[2]
print("x={},y={},z={} after del x[2]".format(x,y,z))
print("_"*50)
#成员资格运算符，in与not in
x=[7,6,9]
print("3 in x->{}".format(3 in x))
print("4 in x->{}".format(0 in x))
print("7 not in x->{}".format(3 not in x))
print("0 not in x->{}".format(0 not in x))
print("_"*50)
#布尔运算符
a,b,c=0,12,17
if c>a and c<b:
    print('a<c<b')
else: print('a<c<b no')
print("_"*50)
#定义函数
def simple_func(x,y):
    z=pow(x,3)+y#pow函数运行为x的y次方
    return z
print("simple_func(3,5)->{}".format(simple_func(3,5)))
print("simple_func(4,3)->{}".format(simple_func(4,3)))
print("simple_func(y=7,x=3)->{}".format(simple_func(y=7,x=3)))
print("_"*50)
#定义斐波那契数列(Successione di Fibonacci)函数
def fibonacci(s,count):
    fib_lst=[0,1]
    fib_part=[]
    if s==0 or s==1:
        fib_part[:]=fib_lst
        for i in range(count-2):
            fib_part.append(fib_part[-1]+fib_part[-2])
    else:
        while True:
            fib_lst[:]=[fib_lst[1],fib_lst[0]+fib_lst[1]]
            #print(fib_lst)
            if fib_lst[1]-s>=0:break
        fib_part[:]=fib_lst
        if abs(fib_lst[0]-s)>=abs(fib_lst[1]-s):
            for i in range(count-1):
                fib_part.append(fib_part[-1]+fib_part[-2])
            fib_part.pop(0)
        else:
            for i in range(count-2):
                fib_part.append(fib_part[-1]+fib_part[-2])
    return fib_part
print("fibonacci(4,9)->{}".format(fibonacci(4,9)))
print("fibonacci(7,8)->{}".format(fibonacci(7,8)))
print("_"*50)
#递归
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(8))
print("_"*50)
#类
class cat:
    run='wuooo' 
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('yummy')
            self.hungry=False
        else:
            print('No.Thanks!')
class Apodidae(cat):
    def __init__(self):
        super(Apodidae,self).__init__()
        self.sound='miao!'
    def sing(self):
        print(self.sound)
swift=Apodidae()
print("swift.run->{}".format(swift.run))
print("swift.eat()->")
swift.eat()
print("swift.eat()->")
swift.eat()
print("swift.sing()->")
swift.sing()
blackswift=Apodidae()
scarceswift=Apodidae()
print("blackswift.sing()->")
blackswift.sing()
print("scarceswift.sing()->")
scarceswift.sing()
print("blackswift.run->{}".format(blackswift.run))
blackswift.run='humming'
print("blackswift.run after redefining the blackswif's attribute->{}".format(blackswift.run))
print("scarceswift.run->{}".format(scarceswift.run))
help(Apodidae)
help(cat)
print("_"*50)

class Fibs():
    def __init__(self):
        self.a=0
        self.b=1
    def next(self): 
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self
f=Fibs()
fa=[]
fb=[]
for i in range(4):
    fa.append(f.next())
print("fa={}".format(fa))
for i in range(7):
    fb.append(f.next())
print("fb={}".format(fb))
lst_d=list(range(5,20,3))
print("lst_d={}".format(lst_d))
lst_iter=iter(lst_d)
print("next(lst_iter)->{}".format(next(lst_iter)))
print("next(lst_iter)->{}".format(next(lst_iter)))
for i in lst_iter:
    print(i)
lst_e=[list(range(5,20,3)),[3,7,67,list(range(5)),56]]
print("lst_e={}".format(lst_e))
flatten_lst=[]
for v_1 in lst_e:
    try:
        for v_2 in v_1:
            try:
                for v_3 in v_2:
                    flatten_lst.append(v_3)
            except TypeError:
                flatten_lst.append(v_2)
    except TypeError:
        flatten_lst.append(v_1)
print("flatten_lst={}".format(flatten_lst))
def flatten(lst):
    try:       
        for n_lst in lst:         
            for m in flatten(n_lst):           
                yield m  
    except TypeError: 
        yield lst 
print("list(flatten(lst_e))->{}".format(list(flatten(lst_e))))
def infinite():
    n=5
    while True:
        yield 'num#'+str(n)
        n+=1
n=infinite()
print("next(n)->{}".format(next(n)))
print("next(n)->{}".format(next(n)))
print("next(n)->{}".format(next(n)))
print("[next(n) for i in range(3)]->{}".format([next(n) for i in range(3)]))
n=3
print("[[(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n)]->{}".format([[(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n)]))
print("([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))->{}".format(([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))))
gen=([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))
print("next(gen)->{}".format(next(gen)))
print("next(gen)->{}".format(next(gen)))
print("_"*50)
def f_convert_a(x):
    try:
        return float(x)
    except:
        return x
print("f_convert_a('3.13')->{}".format(f_convert_a('3.13')))    
print("f_convert_a('i donot know')->{}".format(f_convert_a('i donot know')))  
print("f_convert_a(3,4,7)->{}".format(f_convert_a((3,4,7))))  
print("_"*50)
def f_convert_c(x):
    try:
        return float(x)
    except ValueError:
        return x
    except TypeError:
        print(x,'TypeError')
print("f_convert_c('3.13')->{}".format(f_convert_c('3.13')))    
print("f_convert_c('i donot know')->{}".format(f_convert_c('i donot know')))  
print("f_convert_c(3,4,7)->{}".format(f_convert_c((3,4,7))))     
print("_"*50)
def f_convert_d(x):
    try:
        return float(x)
    except (ValueError,TypeError):
        print(x,'ValueError or TypeError')
print("f_convert_d('3.13')->{}".format(f_convert_d('3.13')))    
print("f_convert_d('i donot know')->{}".format(f_convert_d('i donot know')))  
print("f_convert_d(3,4,7)->{}".format(f_convert_d((3,4,7))))    
print("_"*50)
def f_convert_e(x):
    try:
        return float(x)
    except (ValueError,TypeError) as e:
        return print(x,e)
print("f_convert_e('3.13')->{}".format(f_convert_e('3.13')))    
print("f_convert_e('i donot know')->{}".format(f_convert_e('i donot know')))  
print("f_convert_e(3,4,7)->{}".format(f_convert_e((3,4,7))))     
print("_"*50)
def f_open_b(fp):
    try:
        f=open(fp,'r')
    except IOError as e:
        print('Unable to open',fp,':%s\n' %e)
    else:
        data=f.read()
        f.close()
        return data
    finally:
        print('done!')
f_open_b("./data/tryException.txt")        
