sheep=[5,7,300, 90, 24, 50, 75]

# câu 2.1
print("Hello, my name is Quan and these are my ship sizes")
print(sheep)


# câu 2.2
print("now my biggest sheep has size ",max(sheep), " let's shear it")
i=sheep.index(max(sheep))

# câu 2.3
sheep[int(i)]=8
print("after shearig, here is my flock")
print(sheep)

# câu 2.4
onemonth=[j+50 for j in (sheep)]
print("one month has passed, now here is my flock")
print(onemonth)


# câu 2.5
m=int(input('numbers of month: '))
onemonth=[j+50 for j in (sheep)]
print("one month has passed, now here is my flock")
print(onemonth)
for k in range(1,m+1):
    
    print('MONTH  ', k,':')
    print('one month has pass, now here is my flock')
    for l in range(len(sheep)):
        sheep[l]=sheep[l]+50 
    print(sheep)
    print("now my biggest sheep has size ",max(sheep), " let's shear it")
    i=sheep.index(max(sheep))
    sheep[int(i)]=8
    print("after shearing, here is my flock")
    print(sheep)


# câu 2.6
m=int(input('numbers of month: '))
i=sheep.index(max(sheep))
sheep[int(i)]=8
print("after shearig, here is my flock")
print(sheep)

for k in range(1,m+1):
    print('MONTH  ', k,':')
    print('one month has pass, now here is my flock')
    for l in range(len(sheep)):
        sheep[l]=sheep[l]+50 
    print(sheep)
    if k!= m:
        print("now my biggest sheep has size ",max(sheep), " let's shear it")
        i=sheep.index(max(sheep))
        sheep[int(i)]=8
        print("after shearing, here is my flock")
        print(sheep)
    else:
        size=sum(sheep)
        print("my flock has size in total: ",size)
        money=size*2
        print("i would get",size," * 2$ = ",money,'$')





