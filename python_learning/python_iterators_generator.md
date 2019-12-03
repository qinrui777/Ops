### iterator、iterable

- iterator 迭代器
- iterable 可迭代的对象: iterable is an object capable of returning its members one at a time

```python
from collections.abc import Iterable, Iterator

a = [1,2,3]
b = iter(a)
c = list(b) # iterator是消耗型的,用一次少一次.对iterator进行变量,iterator就空了!

if b:
    print(1)
if b == None:
    print("b become None.")

d = list(b)
e = iter(a) #通过iter()方法,得到iterator,iter()实际上调用了__iter__()

print(type(a)) #<class 'list'>
print(type(b)) # <class 'list_iterator'>
print(type(c)) # <class 'list'>
print(type(d)) # <class 'list'>
print(type(e)) # <class 'list_iterator'>

print(isinstance(a,Iterator))  # Flase   
print(isinstance(a,Iterable))  # True => list 是iterable可迭代的对象

print(isinstance(b,Iterator))  # True
print(isinstance(b,Iterable))  # True
# 可见,itertor一定是iterable,但iterable不一定是itertor

print(next(e))  #next()实际调用了__next__()方法, iterator才可以调用 next() 方法
```

### generator
普通函数用 return 返回一个值，和 Java 等其他语言是一样的，然而在 Python 中还有一种函数，用关键字 yield 来返回值，这种函数叫生成器函数

**generator**: A function which returns a generator iterator. It looks like a normal function except that it contains yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function.

python有两种类型的生成器：生成器表达式和生成器函数。


- **generator expression:** An expression that returns an iterator.
```python
>>> a = (elem for elem in [1, 2, 3])
>>> a
<generator object <genexpr> at 0x1031c13d0>
```

- **generator iterator:** An object created by a generator funcion.

```python
def fibonacci(max):
    n,a,b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a+b
        n = n + 1

print(fab(5))       # <generator object fab at 0x1008cc0d0>
print(type(fab(5))) # <class 'generator'>
fibos = fibonacci(5)
print(next(fibos),next(fibos),next(fibos))  # 打印：斐波拉契数列 1 1 2， 等同于 python2.x print(f.next())
```

其实说白了,generator就是iterator的一种,以更优雅的方式实现的iterator.官方的说法是:
`Python’s generators provide a convenient way to implement the iterator protocol.`
前文讲到iterator通过__next__()方法实现了每次调用,返回一个单一值的功能.而yield就是实现generator的__next__()

---

Ref:
- http://kissg.me/2016/04/09/python-generator-yield/
- https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/index.html
- https://nvie.com/posts/iterators-vs-generators/