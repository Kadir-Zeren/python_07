a= range(1,11)
print(list(a))
print(

list(range(2,15,2))
)

a = range(2,15,2)
print(a)
print(*a)

mix_list = [1,[1,'one',2,'two',3,'three'],4]
print(mix_list[1])
print(mix_list[1][1::2])


harf = 'abcdefg'
mylist=list(harf)
print(mylist)
print(mylist[::-1])
print(len(mylist))
print(mylist[2:2:-1])
print(mylist)
print(mylist[:4:-1])
print(mylist[0:4:-1])
print(mylist[:4:-1])
mylist=['a',[1,2,3],'c','kelime',7,8,9]
mylist[-4:]=[20,30]
print(mylist)
mylist[2]=[90,89,78]
print(mylist)
mylist[0:1]=['a','b','c']
print(mylist)
a=range(5,20)
print(type(a))
print(a)
print(list(a))
print(list(range(2,21,3)))
print(list(range(2,21,-3)))
print(list(range(21,2,-3)))
print(range(10))
tuple_1 = ('h','a','p','p','y')
word='happy'
tuple_2 = tuple(word)
print(tuple_1)
print(tuple_2)
mytuple = (1,2,3,4,5,6)
print(mytuple)
print(tuple('itop'))
mytuple2=9,8,7,6,5
print(mytuple2)
a=[1,2,3]
b=(1,2,3)
print(type(a),type(b))
bos_tuple = ()
print(type(bos_tuple))
mytuple=('Solar',)
print(type(mytuple))
mytuple = (5,)
print(type(mytuple))
tuple_1 = 'h','a','p','p','y'
tuple_2 = 1, 3, 5
print(tuple_1)
print(type(tuple_1))
print(tuple_2)