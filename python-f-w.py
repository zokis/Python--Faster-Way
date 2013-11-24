from jinja2 import Template

template = Template(open('index-template.html', 'r').read())

tests = (
    (
        """>>> def a():
...     d = {}
...     return d
>>> dis(a)
  3           0 BUILD_MAP                0
              3 STORE_FAST               0 (d)

  4           6 LOAD_FAST                0 (d)
              9 RETURN_VALUE
>>> timeit(a)
0.09059309959411621
""",
        """>>> def a():
...     d = dict()
...     return d
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (dict)
              3 CALL_FUNCTION            0
              6 STORE_FAST               0 (d)

  4           9 LOAD_FAST                0 (d)
             12 RETURN_VALUE
>>> timeit(a)
0.21603679656982422"""
    ),
    (
        """>>> def a():
...     l = [0,8,6,4,2,1,3,5,7,9]
...     l.sort()
...     return l
>>> dis(a)
  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (8)
              6 LOAD_CONST               3 (6)
              9 LOAD_CONST               4 (4)
             12 LOAD_CONST               5 (2)
             15 LOAD_CONST               6 (1)
             18 LOAD_CONST               7 (3)
             21 LOAD_CONST               8 (5)
             24 LOAD_CONST               9 (7)
             27 LOAD_CONST              10 (9)
             30 BUILD_LIST              10
             33 STORE_FAST               0 (l)

  4          36 LOAD_FAST                0 (l)
             39 LOAD_ATTR                0 (sort)
             42 CALL_FUNCTION            0
             45 POP_TOP

  5          46 LOAD_FAST                0 (l)
             49 RETURN_VALUE
>>> timeit(a)
0.5776820182800293""",
        """>>> def a():
...     l = [0,8,6,4,2,1,3,5,7,9]
...     return sorted(l)
>>> dis(a)
  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (8)
              6 LOAD_CONST               3 (6)
              9 LOAD_CONST               4 (4)
             12 LOAD_CONST               5 (2)
             15 LOAD_CONST               6 (1)
             18 LOAD_CONST               7 (3)
             21 LOAD_CONST               8 (5)
             24 LOAD_CONST               9 (7)
             27 LOAD_CONST              10 (9)
             30 BUILD_LIST              10
             33 STORE_FAST               0 (l)

  4          36 LOAD_GLOBAL              0 (sorted)
             39 LOAD_FAST                0 (l)
             42 CALL_FUNCTION            1
             45 RETURN_VALUE
>>> timeit(a)
0.8237090110778809"""
    ),
    (
        """>>> def a():
...     a, b, c, d, e, f, g, h, i, j = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
...     return j, i, h, g, f, e, d, c, b, a
>>> dis(a)
  3           0 LOAD_CONST              11 ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
              3 UNPACK_SEQUENCE         10
              6 STORE_FAST               0 (a)
              9 STORE_FAST               1 (b)
             12 STORE_FAST               2 (c)
             15 STORE_FAST               3 (d)
             18 STORE_FAST               4 (e)
             21 STORE_FAST               5 (f)
             24 STORE_FAST               6 (g)
             27 STORE_FAST               7 (h)
             30 STORE_FAST               8 (i)
             33 STORE_FAST               9 (j)

  4          36 LOAD_FAST                9 (j)
             39 LOAD_FAST                8 (i)
             42 LOAD_FAST                7 (h)
             45 LOAD_FAST                6 (g)
             48 LOAD_FAST                5 (f)
             51 LOAD_FAST                4 (e)
             54 LOAD_FAST                3 (d)
             57 LOAD_FAST                2 (c)
             60 LOAD_FAST                1 (b)
             63 LOAD_FAST                0 (a)
             66 BUILD_TUPLE             10
             69 RETURN_VALUE
>>> timeit(a)
0.22710919380187988""",
        """>>> def a():
...     a = 0
...     b = 1
...     c = 2
...     d = 3
...     e = 4
...     f = 5
...     g = 6
...     h = 7
...     i = 8
...     j = 9
...     return j, i, h, g, f, e, d, c, b, a
>>> dis(a)
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               0 (a)

  4           6 LOAD_CONST               2 (1)
              9 STORE_FAST               1 (b)

  5          12 LOAD_CONST               3 (2)
             15 STORE_FAST               2 (c)

  6          18 LOAD_CONST               4 (3)
             21 STORE_FAST               3 (d)

  7          24 LOAD_CONST               5 (4)
             27 STORE_FAST               4 (e)

  8          30 LOAD_CONST               6 (5)
             33 STORE_FAST               5 (f)

  9          36 LOAD_CONST               7 (6)
             39 STORE_FAST               6 (g)

 10          42 LOAD_CONST               8 (7)
             45 STORE_FAST               7 (h)

 11          48 LOAD_CONST               9 (8)
             51 STORE_FAST               8 (i)

 12          54 LOAD_CONST              10 (9)
             57 STORE_FAST               9 (j)

 13          60 LOAD_FAST                9 (j)
             63 LOAD_FAST                8 (i)
             66 LOAD_FAST                7 (h)
             69 LOAD_FAST                6 (g)
             72 LOAD_FAST                5 (f)
             75 LOAD_FAST                4 (e)
             78 LOAD_FAST                3 (d)
             81 LOAD_FAST                2 (c)
             84 LOAD_FAST                1 (b)
             87 LOAD_FAST                0 (a)
             90 BUILD_TUPLE             10
             93 RETURN_VALUE
>>> timeit(a)
0.2503318786621094"""
    ),
    (
        """>>> def a():
...     a, b, c, d, e, f = 2, 5, 52, 25, 225, 552
...     if a < b < c < d < e < f:
...         return True
...     return False
>>> dis(a)
  3           0 LOAD_CONST               7 ((2, 5, 52, 25, 225, 552))
              3 UNPACK_SEQUENCE          6
              6 STORE_FAST               0 (a)
              9 STORE_FAST               1 (b)
             12 STORE_FAST               2 (c)
             15 STORE_FAST               3 (d)
             18 STORE_FAST               4 (e)
             21 STORE_FAST               5 (f)

  4          24 LOAD_FAST                0 (a)
             27 LOAD_FAST                1 (b)
             30 DUP_TOP
             31 ROT_THREE
             32 COMPARE_OP               0 (<)
             35 JUMP_IF_FALSE_OR_POP    80
             38 LOAD_FAST                2 (c)
             41 DUP_TOP
             42 ROT_THREE
             43 COMPARE_OP               0 (<)
             46 JUMP_IF_FALSE_OR_POP    80
             49 LOAD_FAST                3 (d)
             52 DUP_TOP
             53 ROT_THREE
             54 COMPARE_OP               0 (<)
             57 JUMP_IF_FALSE_OR_POP    80
             60 LOAD_FAST                4 (e)
             63 DUP_TOP
             64 ROT_THREE
             65 COMPARE_OP               0 (<)
             68 JUMP_IF_FALSE_OR_POP    80
             71 LOAD_FAST                5 (f)
             74 COMPARE_OP               0 (<)
             77 JUMP_FORWARD             2 (to 82)
        >>   80 ROT_TWO
             81 POP_TOP
        >>   82 POP_JUMP_IF_FALSE       89

  5          85 LOAD_GLOBAL              0 (True)
             88 RETURN_VALUE

  6     >>   89 LOAD_GLOBAL              1 (False)
             92 RETURN_VALUE
>>> timeit(a)
0.23741507530212402""",
        """>>> def a():
...     a, b, c, d, e, f = 2, 5, 52, 25, 225, 552
...     if a < b and b < c and c < d and d < e and e < f:
...         return True
...     return False
>>> dis(a)
  3           0 LOAD_CONST               7 ((2, 5, 52, 25, 225, 552))
              3 UNPACK_SEQUENCE          6
              6 STORE_FAST               0 (a)
              9 STORE_FAST               1 (b)
             12 STORE_FAST               2 (c)
             15 STORE_FAST               3 (d)
             18 STORE_FAST               4 (e)
             21 STORE_FAST               5 (f)

  4          24 LOAD_FAST                0 (a)
             27 LOAD_FAST                1 (b)
             30 COMPARE_OP               0 (<)
             33 POP_JUMP_IF_FALSE       88
             36 LOAD_FAST                1 (b)
             39 LOAD_FAST                2 (c)
             42 COMPARE_OP               0 (<)
             45 POP_JUMP_IF_FALSE       88
             48 LOAD_FAST                2 (c)
             51 LOAD_FAST                3 (d)
             54 COMPARE_OP               0 (<)
             57 POP_JUMP_IF_FALSE       88
             60 LOAD_FAST                3 (d)
             63 LOAD_FAST                4 (e)
             66 COMPARE_OP               0 (<)
             69 POP_JUMP_IF_FALSE       88
             72 LOAD_FAST                4 (e)
             75 LOAD_FAST                5 (f)
             78 COMPARE_OP               0 (<)
             81 POP_JUMP_IF_FALSE       88

  5          84 LOAD_GLOBAL              0 (True)
             87 RETURN_VALUE

  6     >>   88 LOAD_GLOBAL              1 (False)
             91 RETURN_VALUE
>>> timeit(a)
0.1962449550628662"""
    ),
    (
        """>>> def a():
...     a = True
...     if a:
...         return True
...     return False
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (True)
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 POP_JUMP_IF_FALSE       16

  5          12 LOAD_GLOBAL              0 (True)
             15 RETURN_VALUE

  6     >>   16 LOAD_GLOBAL              1 (False)
             19 RETURN_VALUE
>>> timeit(a)
0.1288449764251709""",
        """>>> def a():
...     a = True
...     if a is True:
...         return True
...     return False
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (True)
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 LOAD_GLOBAL              0 (True)
             12 COMPARE_OP               8 (is)
             15 POP_JUMP_IF_FALSE       22

  5          18 LOAD_GLOBAL              0 (True)
             21 RETURN_VALUE

  6     >>   22 LOAD_GLOBAL              1 (False)
             25 RETURN_VALUE
>>> timeit(a)
0.15628480911254883""",
        """>>> def a():
...     a = True
...     if a == True:
...         return True
...     return False
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (True)
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 LOAD_GLOBAL              0 (True)
             12 COMPARE_OP               2 (==)
             15 JUMP_IF_FALSE            5 (to 23)
             18 POP_TOP

  5          19 LOAD_GLOBAL              0 (True)
             22 RETURN_VALUE
        >>   23 POP_TOP

  6          24 LOAD_GLOBAL              1 (False)
             27 RETURN_VALUE
>>> timeit(a)
0.16727304458618164"""
    ),
    (
        """>>> def a():
...     a = 1
...     if a is not 2:
...         return True
...     return False
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 LOAD_CONST               2 (2)
             12 COMPARE_OP               9 (is not)
             15 JUMP_IF_FALSE            5 (to 23)
             18 POP_TOP

  5          19 LOAD_GLOBAL              0 (True)
             22 RETURN_VALUE
        >>   23 POP_TOP

  6          24 LOAD_GLOBAL              1 (False)
             27 RETURN_VALUE
>>> timeit(a)
0.1171870231628418""",
        """>>> def a():
...     a = 1
...     if not a is 2:
...         return True
...     return False
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 LOAD_CONST               2 (2)
             12 COMPARE_OP               9 (is not)
             15 POP_JUMP_IF_FALSE       22

  5          18 LOAD_GLOBAL              0 (True)
             21 RETURN_VALUE

  6     >>   22 LOAD_GLOBAL              1 (False)
             25 RETURN_VALUE
>>> timeit(a)
0.12001895904541016""",
        """>>> def a():
...     a = 1
...     if a != 2:
...         return True
...     return False
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 LOAD_CONST               2 (2)
             12 COMPARE_OP               3 (!=)
             15 POP_JUMP_IF_FALSE       22

  5          18 LOAD_GLOBAL              0 (True)
             21 RETURN_VALUE

  6     >>   22 LOAD_GLOBAL              1 (False)
             25 RETURN_VALUE
>>> timeit(a)
0.17791104316711426"""
    ),
    (
        """>>> def a():
...     a = []
...     if a:
...         return False
...     return True
>>> dis(a)
  3           0 BUILD_LIST               0
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 POP_JUMP_IF_FALSE       16

  5          12 LOAD_GLOBAL              0 (False)
             15 RETURN_VALUE

  6     >>   16 LOAD_GLOBAL              1 (True)
             19 RETURN_VALUE
>>> timeit(a)
0.11919498443603516""",
        """>>> def a():
...     a = []
...     if not a:
...         return True
...     return False
>>> dis(a)
  3           0 BUILD_LIST               0
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 JUMP_IF_TRUE            5 (to 17)
             12 POP_TOP

  5          13 LOAD_GLOBAL              0 (True)
             16 RETURN_VALUE
        >>   17 POP_TOP

  6          18 LOAD_GLOBAL              1 (False)
             21 RETURN_VALUE
>>> timeit(a)
0.0989830493927002""",
        """>>> def a():
...     a = []
...     if a == []:
...         return True
...     return False
>>> dis(a)
  3           0 BUILD_LIST               0
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 BUILD_LIST               0
             12 COMPARE_OP               2 (==)
             15 POP_JUMP_IF_FALSE       22

  5          18 LOAD_GLOBAL              0 (True)
             21 RETURN_VALUE

  6     >>   22 LOAD_GLOBAL              1 (False)
             25 RETURN_VALUE
>>> timeit(a)
0.152724027633667""",
        """>>> def a():
...     a = []
...     if len(a)&lt;= 0:
...         return True
...     return False
>>> dis(a)
  3           0 BUILD_LIST               0
              3 STORE_FAST               0 (a)

  4           6 LOAD_GLOBAL              0 (len)
              9 LOAD_FAST                0 (a)
             12 CALL_FUNCTION            1
             15 LOAD_CONST               1 (0)
             18 COMPARE_OP               1 (&lt;=)
             21 POP_JUMP_IF_FALSE       28

  5          24 LOAD_GLOBAL              1 (True)
             27 RETURN_VALUE

  6     >>   28 LOAD_GLOBAL              2 (False)
             31 RETURN_VALUE
>>> timeit(a)
0.18400812149047852""",
    ),
    (
        """>>> def a():
...     a = object()
...     if not a:
...         return False
...     return True
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (object)
              3 CALL_FUNCTION            0
              6 STORE_FAST               0 (a)

  4           9 LOAD_FAST                0 (a)
             12 POP_JUMP_IF_TRUE       19

  5          15 LOAD_GLOBAL              1 (False)
             18 RETURN_VALUE

  6     >>   19 LOAD_GLOBAL              2 (True)
             22 RETURN_VALUE
>>> timeit(a)
0.17762112617492676""",
        """>>> def a():
...     a = object()
...     if a is None:
...         return False
...     return True
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (object)
              3 CALL_FUNCTION            0
              6 STORE_FAST               0 (a)

  4           9 LOAD_FAST                0 (a)
             12 LOAD_CONST               0 (None)
             15 COMPARE_OP               8 (is)
             18 POP_JUMP_IF_FALSE       25

  5          21 LOAD_GLOBAL              2 (False)
             24 RETURN_VALUE

  6     >>   25 LOAD_GLOBAL              3 (True)
             28 RETURN_VALUE
>>> timeit(a)
0.2032458782196045""",
        """>>> def a():
...     a = object()
...     if a:
...         return True
...     return False
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (object)
              3 CALL_FUNCTION            0
              6 STORE_FAST               0 (a)

  4           9 LOAD_FAST                0 (a)
             12 POP_JUMP_IF_FALSE       19

  5          15 LOAD_GLOBAL              1 (True)
             18 RETURN_VALUE

  6     >>   19 LOAD_GLOBAL              2 (False)
             22 RETURN_VALUE
>>> timeit(a)
0.17735886573791504""",
        """>>> def a():
...     a = object()
...     if a is not None:
...         return True
...     return False
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (object)
              3 CALL_FUNCTION            0
              6 STORE_FAST               0 (a)

  4           9 LOAD_FAST                0 (a)
             12 LOAD_CONST               0 (None)
             15 COMPARE_OP               9 (is not)
             18 POP_JUMP_IF_FALSE       25

  5          21 LOAD_GLOBAL              2 (True)
             24 RETURN_VALUE

  6     >>   25 LOAD_GLOBAL              3 (False)
             28 RETURN_VALUE
>>> timeit(a)
0.19365406036376953""",
    ),
    (
        """>>> def a():
...     a = [1, 2, 3, 4, 5]
...     s = 0
...     for p, v in enumerate(a):
...         s += p
...         s += v
...     return s
>>> a()
25
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 LOAD_CONST               2 (2)
              6 LOAD_CONST               3 (3)
              9 LOAD_CONST               4 (4)
             12 LOAD_CONST               5 (5)
             15 BUILD_LIST               5
             18 STORE_FAST               0 (a)

  4          21 LOAD_CONST               6 (0)
             24 STORE_FAST               1 (s)

  5          27 SETUP_LOOP              46 (to 76)
             30 LOAD_GLOBAL              0 (enumerate)
             33 LOAD_FAST                0 (a)
             36 CALL_FUNCTION            1
             39 GET_ITER
        >>   40 FOR_ITER                32 (to 75)
             43 UNPACK_SEQUENCE          2
             46 STORE_FAST               2 (p)
             49 STORE_FAST               3 (v)

  6          52 LOAD_FAST                1 (s)
             55 LOAD_FAST                2 (p)
             58 INPLACE_ADD
             59 STORE_FAST               1 (s)

  7          62 LOAD_FAST                1 (s)
             65 LOAD_FAST                3 (v)
             68 INPLACE_ADD
             69 STORE_FAST               1 (s)
             72 JUMP_ABSOLUTE           40
        >>   75 POP_BLOCK

  8     >>   76 LOAD_FAST                1 (s)
             79 RETURN_VALUE
>>> timeit(a)
0.7968449592590332""",
        """>>> def a():
...     a = [1, 2, 3, 4, 5]
...     s = 0
...     for i in range(len(a)):
...         s += i
...         s += a[i]
...     return s
>>> a()
25
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 LOAD_CONST               2 (2)
              6 LOAD_CONST               3 (3)
              9 LOAD_CONST               4 (4)
             12 LOAD_CONST               5 (5)
             15 BUILD_LIST               5
             18 STORE_FAST               0 (a)

  4          21 LOAD_CONST               6 (0)
             24 STORE_FAST               1 (s)

  5          27 SETUP_LOOP              50 (to 80)
             30 LOAD_GLOBAL              0 (range)
             33 LOAD_GLOBAL              1 (len)
             36 LOAD_FAST                0 (a)
             39 CALL_FUNCTION            1
             42 CALL_FUNCTION            1
             45 GET_ITER
        >>   46 FOR_ITER                30 (to 79)
             49 STORE_FAST               2 (i)

  6          52 LOAD_FAST                1 (s)
             55 LOAD_FAST                2 (i)
             58 INPLACE_ADD
             59 STORE_FAST               1 (s)

  7          62 LOAD_FAST                1 (s)
             65 LOAD_FAST                0 (a)
             68 LOAD_FAST                2 (i)
             71 BINARY_SUBSCR
             72 INPLACE_ADD
             73 STORE_FAST               1 (s)
             76 JUMP_ABSOLUTE           46
        >>   79 POP_BLOCK

  8     >>   80 LOAD_FAST                1 (s)
             83 RETURN_VALUE
>>> timeit(a)
0.8638288974761963""",
    ),
    (
        """>>> def a():
...     r = ''
...     for i in range(10):
...         r += str(i)
...     return r
>>> a()
'0123456789'
>>> dis(a)
  3           0 LOAD_CONST               1 ('')
              3 STORE_FAST               0 (r)

  4           6 SETUP_LOOP              36 (to 45)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (10)
             15 CALL_FUNCTION            1
             18 GET_ITER
        >>   19 FOR_ITER                22 (to 44)
             22 STORE_FAST               1 (i)

  5          25 LOAD_FAST                0 (r)
             28 LOAD_GLOBAL              1 (str)
             31 LOAD_FAST                1 (i)
             34 CALL_FUNCTION            1
             37 INPLACE_ADD
             38 STORE_FAST               0 (r)
             41 JUMP_ABSOLUTE           19
        >>   44 POP_BLOCK

  6     >>   45 LOAD_FAST                0 (r)
             48 RETURN_VALUE
>>> timeit(a)
1.964811086654663""",
        """>>> def a():
...     r = []
...     for i in range(10):
...         r.append(str(i))
...     return ''.join(r)
>>> a()
'0123456789'
>>> dis(a)
  3           0 BUILD_LIST               0
              3 STORE_FAST               0 (r)

  4           6 SETUP_LOOP              39 (to 48)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               1 (10)
             15 CALL_FUNCTION            1
             18 GET_ITER
        >>   19 FOR_ITER                25 (to 47)
             22 STORE_FAST               1 (i)

  5          25 LOAD_FAST                0 (r)
             28 LOAD_ATTR                1 (append)
             31 LOAD_GLOBAL              2 (str)
             34 LOAD_FAST                1 (i)
             37 CALL_FUNCTION            1
             40 CALL_FUNCTION            1
             43 POP_TOP
             44 JUMP_ABSOLUTE           19
        >>   47 POP_BLOCK

  6     >>   48 LOAD_CONST               2 ('')
             51 LOAD_ATTR                3 (join)
             54 LOAD_FAST                0 (r)
             57 CALL_FUNCTION            1
             60 RETURN_VALUE
>>> timeit(a)
2.6579368114471436""",
    ),
    (
        """>>> def a():
...     a = 5
...     b = 2
...     c = 3
...     return "%d" % (a*(b+c))
>>> a()
'25'
>>> dis(a)
  3           0 LOAD_CONST               1 (5)
              3 STORE_FAST               0 (a)

  4           6 LOAD_CONST               2 (2)
              9 STORE_FAST               1 (b)

  5          12 LOAD_CONST               3 (3)
             15 STORE_FAST               2 (c)

  6          18 LOAD_CONST               4 ('%d')
             21 LOAD_FAST                0 (a)
             24 LOAD_FAST                1 (b)
             27 LOAD_FAST                2 (c)
             30 BINARY_ADD
             31 BINARY_MULTIPLY
             32 BINARY_MODULO
             33 RETURN_VALUE
>>> timeit(a)
0.6534428596496582""",
        """>>> def a():
...     a = 5
...     b = 2
...     c = 3
...     return str(a*(b+c))
>>> a()
'25'
>>> dis(a)
  3           0 LOAD_CONST               1 (5)
              3 STORE_FAST               0 (a)

  4           6 LOAD_CONST               2 (2)
              9 STORE_FAST               1 (b)

  5          12 LOAD_CONST               3 (3)
             15 STORE_FAST               2 (c)

  6          18 LOAD_GLOBAL              0 (str)
             21 LOAD_FAST                0 (a)
             24 LOAD_FAST                1 (b)
             27 LOAD_FAST                2 (c)
             30 BINARY_ADD
             31 BINARY_MULTIPLY
             32 CALL_FUNCTION            1
             35 RETURN_VALUE
>>> timeit(a)
0.27884984016418457""",
        """>>> def a():
...     a = 5
...     b = 2
...     c = 3
...     return "%s" % (a*(b+c))
>>> a()
'25'
>>> dis(a)
  3           0 LOAD_CONST               1 (5)
              3 STORE_FAST               0 (a)

  4           6 LOAD_CONST               2 (2)
              9 STORE_FAST               1 (b)

  5          12 LOAD_CONST               3 (3)
             15 STORE_FAST               2 (c)

  6          18 LOAD_CONST               4 ('%s')
             21 LOAD_FAST                0 (a)
             24 LOAD_FAST                1 (b)
             27 LOAD_FAST                2 (c)
             30 BINARY_ADD
             31 BINARY_MULTIPLY
             32 BINARY_MODULO
             33 RETURN_VALUE
>>> timeit(a)
0.23713302612304688"""
    ),
    (
        """>>> def a():
...     a = [1, 2, 3, 4, 5]
...     return a.__len__()
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 LOAD_CONST               2 (2)
              6 LOAD_CONST               3 (3)
              9 LOAD_CONST               4 (4)
             12 LOAD_CONST               5 (5)
             15 BUILD_LIST               5
             18 STORE_FAST               0 (a)

  4          21 LOAD_FAST                0 (a)
             24 LOAD_ATTR                0 (__len__)
             27 CALL_FUNCTION            0
             30 RETURN_VALUE
>>> timeit(a)
0.24736285209655762""",
        """>>> def a():
...     a = [1, 2, 3, 4, 5]
...     return len(a)
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 LOAD_CONST               2 (2)
              6 LOAD_CONST               3 (3)
              9 LOAD_CONST               4 (4)
             12 LOAD_CONST               5 (5)
             15 BUILD_LIST               5
             18 STORE_FAST               0 (a)

  4          21 LOAD_GLOBAL              0 (len)
             24 LOAD_FAST                0 (a)
             27 CALL_FUNCTION            1
             30 RETURN_VALUE
>>> timeit(a)
0.22818613052368164"""
    ),
    (
        """>>> def a():
...     a = 1
...     b = 2
...     c = 2
...     d = 5
...     return (a.__add__(b.__add__(c))).__mul__(d)
>>> a()
25
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (a)

  4           6 LOAD_CONST               2 (2)
              9 STORE_FAST               1 (b)

  5          12 LOAD_CONST               2 (2)
             15 STORE_FAST               2 (c)

  6          18 LOAD_CONST               3 (5)
             21 STORE_FAST               3 (d)

  7          24 LOAD_FAST                0 (a)
             27 LOAD_ATTR                0 (__add__)
             30 LOAD_FAST                1 (b)
             33 LOAD_ATTR                0 (__add__)
             36 LOAD_FAST                2 (c)
             39 CALL_FUNCTION            1
             42 CALL_FUNCTION            1
             45 LOAD_ATTR                1 (__mul__)
             48 LOAD_FAST                3 (d)
             51 CALL_FUNCTION            1
             54 RETURN_VALUE
>>> timeit(a)
0.4007859230041504""",
        """>>> def a():
...     a = 1
...     b = 2
...     c = 2
...     d = 5
...     return (a+b+c)*d
>>> a()
25
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (a)

  4           6 LOAD_CONST               2 (2)
              9 STORE_FAST               1 (b)

  5          12 LOAD_CONST               2 (2)
             15 STORE_FAST               2 (c)

  6          18 LOAD_CONST               3 (5)
             21 STORE_FAST               3 (d)

  7          24 LOAD_FAST                0 (a)
             27 LOAD_FAST                1 (b)
             30 BINARY_ADD
             31 LOAD_FAST                2 (c)
             34 BINARY_ADD
             35 LOAD_FAST                3 (d)
             38 BINARY_MULTIPLY
             39 RETURN_VALUE
>>> timeit(a)
0.17691397666931152""",
    ),
    (
        """>>> class Z():
...     def __init__(self,v):
...         self.v = v
...     def __mul__(self, o):
...         return Z(self.v*o.v)
...     def __add__(self, o):
...         return Z(self.v+o.v)
>>> def a():
...     a = Z(5)
...     b = Z(2)
...     c = Z(3)
...     return (b+c)*a
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (Z)
              3 LOAD_CONST               1 (5)
              6 CALL_FUNCTION            1
              9 STORE_FAST               0 (a)

  4          12 LOAD_GLOBAL              0 (Z)
             15 LOAD_CONST               2 (2)
             18 CALL_FUNCTION            1
             21 STORE_FAST               1 (b)

  5          24 LOAD_GLOBAL              0 (Z)
             27 LOAD_CONST               3 (3)
             30 CALL_FUNCTION            1
             33 STORE_FAST               2 (c)

  6          36 LOAD_FAST                1 (b)
             39 LOAD_FAST                2 (c)
             42 BINARY_ADD
             43 LOAD_FAST                0 (a)
             46 BINARY_MULTIPLY
             47 RETURN_VALUE
>>> timeit(a)
3.0483150482177734""",
        """>>> class Z():
...     def __init__(self,v):
...         self.v = v
...     def __mul__(self, o):
...         return Z(self.v*o.v)
...     def __add__(self, o):
...         return Z(self.v+o.v)
>>> def a():
...     a = Z(5)
...     b = Z(2)
...     c = Z(3)
...     return (b.__add__(c)).__mul__(a)
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (Z)
              3 LOAD_CONST               1 (5)
              6 CALL_FUNCTION            1
              9 STORE_FAST               0 (a)

  4          12 LOAD_GLOBAL              0 (Z)
             15 LOAD_CONST               2 (2)
             18 CALL_FUNCTION            1
             21 STORE_FAST               1 (b)

  5          24 LOAD_GLOBAL              0 (Z)
             27 LOAD_CONST               3 (3)
             30 CALL_FUNCTION            1
             33 STORE_FAST               2 (c)

  6          36 LOAD_FAST                1 (b)
             39 LOAD_ATTR                1 (__add__)
             42 LOAD_FAST                2 (c)
             45 CALL_FUNCTION            1
             48 LOAD_ATTR                2 (__mul__)
             51 LOAD_FAST                0 (a)
             54 CALL_FUNCTION            1
             57 RETURN_VALUE
>>> timeit(a)
2.027787923812866"""
    ),
    (
        """>>> def a():
...     s = 0
...     for i in range(50000):
...         s += i
...     return s
>>> a()
1249975000
>>> dis(a)
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               0 (s)

  4           6 SETUP_LOOP              30 (to 39)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (50000)
             15 CALL_FUNCTION            1
             18 GET_ITER
        >>   19 FOR_ITER                16 (to 38)
             22 STORE_FAST               1 (i)

  5          25 LOAD_FAST                0 (s)
             28 LOAD_FAST                1 (i)
             31 INPLACE_ADD
             32 STORE_FAST               0 (s)
             35 JUMP_ABSOLUTE           19
        >>   38 POP_BLOCK

  6     >>   39 LOAD_FAST                0 (s)
             42 RETURN_VALUE
>>> timeit(a, number=500)
0.9544589519500732""",
        """>>> def a():
...     return sum(i for i in range(50000))
>>> a()
1249975000
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (sum)
              3 LOAD_CONST               1 (&lt;code object &lt;genexpr&gt; at 0x2c7eb30, file "&lt;input&gt;", line 3&gt;)
              6 MAKE_FUNCTION            0
              9 LOAD_GLOBAL              1 (range)
             12 LOAD_CONST               2 (50000)
             15 CALL_FUNCTION            1
             18 GET_ITER
             19 CALL_FUNCTION            1
             22 CALL_FUNCTION            1
             25 RETURN_VALUE
>>> timeit(a, number=500)
1.1507539749145508""",
    ),
    (
        """>>> def a():
...     l = []
...     for i in range(1000):
...         l.append(i)
...     return l
>>> dis(a)
  3           0 BUILD_LIST               0
              3 STORE_FAST               0 (l)

  4           6 SETUP_LOOP              33 (to 42)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               1 (1000)
             15 CALL_FUNCTION            1
             18 GET_ITER
        >>   19 FOR_ITER                19 (to 41)
             22 STORE_FAST               1 (i)

  5          25 LOAD_FAST                0 (l)
             28 LOAD_ATTR                1 (append)
             31 LOAD_FAST                1 (i)
             34 CALL_FUNCTION            1
             37 POP_TOP
             38 JUMP_ABSOLUTE           19
        >>   41 POP_BLOCK

  6     >>   42 LOAD_FAST                0 (l)
             45 RETURN_VALUE
>>> timeit(a)
74.72631120681763""",
        """>>> def a():
...     return [i for i in range(1000)]
>>> dis(a)
  3           0 BUILD_LIST               0
              3 LOAD_GLOBAL              0 (range)
              6 LOAD_CONST               1 (1000)
              9 CALL_FUNCTION            1
             12 GET_ITER
        >>   13 FOR_ITER                12 (to 28)
             16 STORE_FAST               0 (i)
             19 LOAD_FAST                0 (i)
             22 LIST_APPEND              2
             25 JUMP_ABSOLUTE           13
        >>   28 RETURN_VALUE
>>> timeit(a)
31.74762511253357"""
    ),
    (
        """>>> def a():
...     d = {}
...     for i in range(100):
...         d.update({str(i):i*2})
...     return d
>>> dis(a)
  3           0 BUILD_MAP                0
              3 STORE_FAST               0 (d)

  4           6 SETUP_LOOP              50 (to 59)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               1 (100)
             15 CALL_FUNCTION            1
             18 GET_ITER
        >>   19 FOR_ITER                36 (to 58)
             22 STORE_FAST               1 (i)

  5          25 LOAD_FAST                0 (d)
             28 LOAD_ATTR                1 (update)
             31 BUILD_MAP                1
             34 LOAD_FAST                1 (i)
             37 LOAD_CONST               2 (2)
             40 BINARY_MULTIPLY
             41 LOAD_GLOBAL              2 (str)
             44 LOAD_FAST                1 (i)
             47 CALL_FUNCTION            1
             50 STORE_MAP
             51 CALL_FUNCTION            1
             54 POP_TOP
             55 JUMP_ABSOLUTE           19
        >>   58 POP_BLOCK

  6     >>   59 LOAD_FAST                0 (d)
             62 RETURN_VALUE
>>> timeit(a)
43.51503276824951""",
        """>>> def a():
...     d = {}
...     for i in range(100):
...         d[str(i)] = i*2
...     return d
>>> dis(a)
  3           0 BUILD_MAP                0
              3 STORE_FAST               0 (d)

  4           6 SETUP_LOOP              40 (to 49)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               1 (100)
             15 CALL_FUNCTION            1
             18 GET_ITER
        >>   19 FOR_ITER                26 (to 48)
             22 STORE_FAST               1 (i)

  5          25 LOAD_FAST                1 (i)
             28 LOAD_CONST               2 (2)
             31 BINARY_MULTIPLY
             32 LOAD_FAST                0 (d)
             35 LOAD_GLOBAL              1 (str)
             38 LOAD_FAST                1 (i)
             41 CALL_FUNCTION            1
             44 STORE_SUBSCR
             45 JUMP_ABSOLUTE           19
        >>   48 POP_BLOCK

  6     >>   49 LOAD_FAST                0 (d)
             52 RETURN_VALUE
>>> timeit(a)
22.53758192062378""",
        """>>> def a():
...     return {str(i):i*2 for i in range(100)}
>>> dis(a)
  3           0 LOAD_CONST               1 (&lt;code object &lt;dictcomp&gt; at 0x2193ab0, file "&lt;input&gt;", line 3&gt;)
              3 MAKE_FUNCTION            0
              6 LOAD_GLOBAL              0 (range)
              9 LOAD_CONST               2 (100)
             12 CALL_FUNCTION            1
             15 GET_ITER
             16 CALL_FUNCTION            1
             19 RETURN_VALUE
>>> timeit(a)
21.24774694442749"""
    ),
    (
        """>>> def a():
...     l = range(50, -20, -2)
...     d = {}
...     for p, v in enumerate(l):
...         d.update({p:v})
...     return d
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (range)
              3 LOAD_CONST               1 (50)
              6 LOAD_CONST               2 (-20)
              9 LOAD_CONST               3 (-2)
             12 CALL_FUNCTION            3
             15 STORE_FAST               0 (l)

  4          18 BUILD_MAP                0
             21 STORE_FAST               1 (d)

  5          24 SETUP_LOOP              46 (to 73)
             27 LOAD_GLOBAL              1 (enumerate)
             30 LOAD_FAST                0 (l)
             33 CALL_FUNCTION            1
             36 GET_ITER
        >>   37 FOR_ITER                32 (to 72)
             40 UNPACK_SEQUENCE          2
             43 STORE_FAST               2 (p)
             46 STORE_FAST               3 (v)

  6          49 LOAD_FAST                1 (d)
             52 LOAD_ATTR                2 (update)
             55 BUILD_MAP                1
             58 LOAD_FAST                3 (v)
             61 LOAD_FAST                2 (p)
             64 STORE_MAP
             65 CALL_FUNCTION            1
             68 POP_TOP
             69 JUMP_ABSOLUTE           37
        >>   72 POP_BLOCK

  7     >>   73 LOAD_FAST                1 (d)
             76 RETURN_VALUE
>>> timeit(a)
10.904900074005127""",
        """>>> def a():
...     l = range(50, -20, -2)
...     d = {}
...     for p, v in enumerate(l):
...         d[p] = v
...     return d
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (range)
              3 LOAD_CONST               1 (50)
              6 LOAD_CONST               2 (-20)
              9 LOAD_CONST               3 (-2)
             12 CALL_FUNCTION            3
             15 STORE_FAST               0 (l)

  4          18 BUILD_MAP                0
             21 STORE_FAST               1 (d)

  5          24 SETUP_LOOP              36 (to 63)
             27 LOAD_GLOBAL              1 (enumerate)
             30 LOAD_FAST                0 (l)
             33 CALL_FUNCTION            1
             36 GET_ITER
        >>   37 FOR_ITER                22 (to 62)
             40 UNPACK_SEQUENCE          2
             43 STORE_FAST               2 (p)
             46 STORE_FAST               3 (v)

  6          49 LOAD_FAST                3 (v)
             52 LOAD_FAST                1 (d)
             55 LOAD_FAST                2 (p)
             58 STORE_SUBSCR
             59 JUMP_ABSOLUTE           37
        >>   62 POP_BLOCK

  7     >>   63 LOAD_FAST                1 (d)
             66 RETURN_VALUE
>>> timeit(a)
3.2161331176757812""",
        """>>> def a():
...     l = range(50, -20, -2)
...     return {p:v for p, v in enumerate(l)}
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (range)
              3 LOAD_CONST               1 (50)
              6 LOAD_CONST               2 (-20)
              9 LOAD_CONST               3 (-2)
             12 CALL_FUNCTION            3
             15 STORE_FAST               0 (l)

  4          18 LOAD_CONST               4 (&lt;code object &lt;dictcomp&gt; at 0x2ad9db0, file "&lt;input&gt;", line 4&gt;)
             21 MAKE_FUNCTION            0
             24 LOAD_GLOBAL              1 (enumerate)
             27 LOAD_FAST                0 (l)
             30 CALL_FUNCTION            1
             33 GET_ITER
             34 CALL_FUNCTION            1
             37 RETURN_VALUE
>>> timeit(a)
3.210350933074951"""
    ),
    (
        """>>> def a():
...     a = 0
...     return bool(a)
>>> dis(a)
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               0 (a)

  4           6 LOAD_GLOBAL              0 (bool)
              9 LOAD_FAST                0 (a)
             12 CALL_FUNCTION            1
             15 RETURN_VALUE
>>> timeit(a)
0.21692705154418945""",
        """>>> def a():
...     a = True
...     return bool(a)
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (True)
              3 STORE_FAST               0 (a)

  4           6 LOAD_GLOBAL              1 (bool)
              9 LOAD_FAST                0 (a)
             12 CALL_FUNCTION            1
             15 RETURN_VALUE
>>> timeit(a)
0.22511601448059082""",
        """>>> def a():
...     a = 1
...     return bool(a)
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (a)

  4           6 LOAD_GLOBAL              0 (bool)
              9 LOAD_FAST                0 (a)
             12 CALL_FUNCTION            1
             15 RETURN_VALUE
>>> timeit(a)
0.2140359878540039""",
        """>>> def a():
...     a = []
...     return bool(a)
>>> dis(a)
  3           0 BUILD_LIST               0
              3 STORE_FAST               0 (a)

  4           6 LOAD_GLOBAL              0 (bool)
              9 LOAD_FAST                0 (a)
             12 CALL_FUNCTION            1
             15 RETURN_VALUE
>>> timeit(a)
0.23107004165649414""",
        """>>> def a():
...     a = [1]
...     return bool(a)
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 BUILD_LIST               1
              6 STORE_FAST               0 (a)

  4           9 LOAD_GLOBAL              0 (bool)
             12 LOAD_FAST                0 (a)
             15 CALL_FUNCTION            1
             18 RETURN_VALUE
>>> timeit(a)
0.26291584968566895""",
        """>>> def a():
...     a = [1, 2, 3, 4]
...     return bool(a)
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 LOAD_CONST               2 (2)
              6 LOAD_CONST               3 (3)
              9 LOAD_CONST               4 (4)
             12 BUILD_LIST               4
             15 STORE_FAST               0 (a)

  4          18 LOAD_GLOBAL              0 (bool)
             21 LOAD_FAST                0 (a)
             24 CALL_FUNCTION            1
             27 RETURN_VALUE
>>> timeit(a)
0.2995791435241699""",
    ),
    (
        """>>> def a():
...     a = 1
...     return Trueif a != 2 else False
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 LOAD_CONST               2 (2)
             12 COMPARE_OP               3 (!=)
             15 POP_JUMP_IF_FALSE       22
             18 LOAD_GLOBAL              0 (True)
             21 RETURN_VALUE
        >>   22 LOAD_GLOBAL              1 (False)
             25 RETURN_VALUE
>>> timeit(a)
0.11238908767700195""",
        """>>> def a():
...     a = 1
...     return a != 2
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 LOAD_CONST               2 (2)
             12 COMPARE_OP               3 (!=)
             15 RETURN_VALUE
>>> timeit(a)
0.0989840030670666""",
        """>>> def a():
...     a = 1
...     return a != 2 and Trueor False
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 LOAD_CONST               2 (2)
             12 COMPARE_OP               3 (!=)
             15 POP_JUMP_IF_FALSE       24
             18 LOAD_GLOBAL              0 (True)
             21 JUMP_IF_TRUE_OR_POP     27
        >>   24 LOAD_GLOBAL              1 (False)
        >>   27 RETURN_VALUE
>>> timeit(a)
0.12901902198791504"""
    ),
    (
        """>>> def a():
...     a = [1,2,3,4,5]
...     return sum([p+v for p, v in enumerate(a)])
>>> a()
25
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 LOAD_CONST               2 (2)
              6 LOAD_CONST               3 (3)
              9 LOAD_CONST               4 (4)
             12 LOAD_CONST               5 (5)
             15 BUILD_LIST               5
             18 STORE_FAST               0 (a)

  4          21 LOAD_GLOBAL              0 (sum)
             24 BUILD_LIST               0
             27 LOAD_GLOBAL              1 (enumerate)
             30 LOAD_FAST                0 (a)
             33 CALL_FUNCTION            1
             36 GET_ITER
        >>   37 FOR_ITER                22 (to 62)
             40 UNPACK_SEQUENCE          2
             43 STORE_FAST               1 (p)
             46 STORE_FAST               2 (v)
             49 LOAD_FAST                1 (p)
             52 LOAD_FAST                2 (v)
             55 BINARY_ADD
             56 LIST_APPEND              2
             59 JUMP_ABSOLUTE           37
        >>   62 CALL_FUNCTION            1
             65 RETURN_VALUE
>>> timeit(a)
0.8525490760803223""",
        """>>> def a():
...     return sum([p+v for p, v in enumerate([1, 2, 3, 4, 5])])
>>> a()
25
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (sum)
              3 BUILD_LIST               0
              6 LOAD_GLOBAL              1 (enumerate)
              9 LOAD_CONST               1 (1)
             12 LOAD_CONST               2 (2)
             15 LOAD_CONST               3 (3)
             18 LOAD_CONST               4 (4)
             21 LOAD_CONST               5 (5)
             24 BUILD_LIST               5
             27 CALL_FUNCTION            1
             30 GET_ITER
        >>   31 FOR_ITER                22 (to 56)
             34 UNPACK_SEQUENCE          2
             37 STORE_FAST               0 (p)
             40 STORE_FAST               1 (v)
             43 LOAD_FAST                0 (p)
             46 LOAD_FAST                1 (v)
             49 BINARY_ADD
             50 LIST_APPEND              2
             53 JUMP_ABSOLUTE           31
        >>   56 CALL_FUNCTION            1
             59 RETURN_VALUE
>>> timeit(a)
0.8301830291748047""",
        """>>> def a():
...     return sum([p+v for p, v in enumerate(xrange(1, 6))])
>>> a()
25
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (sum)
              3 BUILD_LIST               0
              6 LOAD_GLOBAL              1 (enumerate)
              9 LOAD_GLOBAL              2 (xrange)
             12 LOAD_CONST               1 (1)
             15 LOAD_CONST               2 (6)
             18 CALL_FUNCTION            2
             21 CALL_FUNCTION            1
             24 GET_ITER
        >>   25 FOR_ITER                22 (to 50)
             28 UNPACK_SEQUENCE          2
             31 STORE_FAST               0 (p)
             34 STORE_FAST               1 (v)
             37 LOAD_FAST                0 (p)
             40 LOAD_FAST                1 (v)
             43 BINARY_ADD
             44 LIST_APPEND              2
             47 JUMP_ABSOLUTE           25
        >>   50 CALL_FUNCTION            1
             53 RETURN_VALUE
>>> timeit(a)
0.9235079288482666""",
    ),
    (
        """>>> def a():
...     a = 1
...     if a == 1 or a == 2 or a == 3:
...         return True
...     return False
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 LOAD_CONST               1 (1)
             12 COMPARE_OP               2 (==)
             15 POP_JUMP_IF_TRUE       42
             18 LOAD_FAST                0 (a)
             21 LOAD_CONST               2 (2)
             24 COMPARE_OP               2 (==)
             27 POP_JUMP_IF_TRUE       42
             30 LOAD_FAST                0 (a)
             33 LOAD_CONST               3 (3)
             36 COMPARE_OP               2 (==)
             39 POP_JUMP_IF_FALSE       46

  5     >>   42 LOAD_GLOBAL              0 (True)
             45 RETURN_VALUE

  6     >>   46 LOAD_GLOBAL              1 (False)
             49 RETURN_VALUE
>>> timeit(a)
0.1189959774017334""",
        """>>> def a():
...     a = 1
...     if a in (1, 2, 3):
...         return True
...     return False
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (a)

  4           6 LOAD_FAST                0 (a)
              9 LOAD_CONST               4 ((1, 2, 3))
             12 COMPARE_OP               6 (in)
             15 POP_JUMP_IF_FALSE       22

  5          18 LOAD_GLOBAL              0 (True)
             21 RETURN_VALUE

  6     >>   22 LOAD_GLOBAL              1 (False)
             25 RETURN_VALUE
>>> timeit(a)
0.11190297317504883"""
    ),
    (
        """>>> def a():
...     r = ''
...     for i in range(10):
...         r = '%s%s' % (r, str(i))
...     return r
>>> dis(a)
  3           0 LOAD_CONST               1 ('')
              3 STORE_FAST               0 (r)

  4           6 SETUP_LOOP              42 (to 51)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (10)
             15 CALL_FUNCTION            1
             18 GET_ITER
        >>   19 FOR_ITER                28 (to 50)
             22 STORE_FAST               1 (i)

  5          25 LOAD_CONST               3 ('%s%s')
             28 LOAD_FAST                0 (r)
             31 LOAD_GLOBAL              1 (str)
             34 LOAD_FAST                1 (i)
             37 CALL_FUNCTION            1
             40 BUILD_TUPLE              2
             43 BINARY_MODULO
             44 STORE_FAST               0 (r)
             47 JUMP_ABSOLUTE           19
        >>   50 POP_BLOCK

  6     >>   51 LOAD_FAST                0 (r)
             54 RETURN_VALUE
>>> timeit(a)
3.1673998832702637""",
        """>>> def a():
...     return ''.join(map(str, xrange(10)))
>>> dis(a)
  3           0 LOAD_CONST               1 ('')
              3 LOAD_ATTR                0 (join)
              6 LOAD_GLOBAL              1 (map)
              9 LOAD_GLOBAL              2 (str)
             12 LOAD_GLOBAL              3 (xrange)
             15 LOAD_CONST               2 (10)
             18 CALL_FUNCTION            1
             21 CALL_FUNCTION            2
             24 CALL_FUNCTION            1
             27 RETURN_VALUE
>>> timeit(a)
1.4769208431243896""",
        """>>> def a():
...     return ''.join(map(str, range(10)))
>>> dis(a)
  3           0 LOAD_CONST               1 ('')
              3 LOAD_ATTR                0 (join)
              6 LOAD_GLOBAL              1 (map)
              9 LOAD_GLOBAL              2 (str)
             12 LOAD_GLOBAL              3 (range)
             15 LOAD_CONST               2 (10)
             18 CALL_FUNCTION            1
             21 CALL_FUNCTION            2
             24 CALL_FUNCTION            1
             27 RETURN_VALUE
>>> timeit(a)
1.454106092453003"""
    ),
    (
        """>>> def a():
...     a = [[1,2,3],[2,3,4],[4,5,6]]
...     b = {x[1]: x[2] for x in a}
...     return b
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 LOAD_CONST               2 (2)
              6 LOAD_CONST               3 (3)
              9 BUILD_LIST               3
             12 LOAD_CONST               2 (2)
             15 LOAD_CONST               3 (3)
             18 LOAD_CONST               4 (4)
             21 BUILD_LIST               3
             24 LOAD_CONST               4 (4)
             27 LOAD_CONST               5 (5)
             30 LOAD_CONST               6 (6)
             33 BUILD_LIST               3
             36 BUILD_LIST               3
             39 STORE_FAST               0 (a)

  4          42 LOAD_CONST               7 (&lt;code object &lt;dictcomp&gt; at 0x2739cb0, file "&lt;input&gt;", line 4&gt;)
             45 MAKE_FUNCTION            0
             48 LOAD_FAST                0 (a)
             51 GET_ITER
             52 CALL_FUNCTION            1
             55 STORE_FAST               1 (b)

  5          58 LOAD_FAST                1 (b)
             61 RETURN_VALUE
>>> timeit(a)
0.880389928817749""",
        """>>> def a():
...     a = [[1,2,3],[2,3,4],[4,5,6]]
...     b = dict((x,y)for w,x,y in a)
...     return b
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 LOAD_CONST               2 (2)
              6 LOAD_CONST               3 (3)
              9 BUILD_LIST               3
             12 LOAD_CONST               2 (2)
             15 LOAD_CONST               3 (3)
             18 LOAD_CONST               4 (4)
             21 BUILD_LIST               3
             24 LOAD_CONST               4 (4)
             27 LOAD_CONST               5 (5)
             30 LOAD_CONST               6 (6)
             33 BUILD_LIST               3
             36 BUILD_LIST               3
             39 STORE_FAST               0 (a)

  4          42 LOAD_GLOBAL              0 (dict)
             45 LOAD_CONST               7 (&lt;code object &lt;genexpr&gt; at 0x218f130, file "&lt;input&gt;", line 4&gt;)
             48 MAKE_FUNCTION            0
             51 LOAD_FAST                0 (a)
             54 GET_ITER
             55 CALL_FUNCTION            1
             58 CALL_FUNCTION            1
             61 STORE_FAST               1 (b)

  5          64 LOAD_FAST                1 (b)
             67 RETURN_VALUE
>>> timeit(a)
1.6701810359954834""",
        """>>> def a():
...     a = [[1,2,3],[2,3,4],[4,5,6]]
...     b = {k:v for x,k,v in a}
...     return b
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 LOAD_CONST               2 (2)
              6 LOAD_CONST               3 (3)
              9 BUILD_LIST               3
             12 LOAD_CONST               2 (2)
             15 LOAD_CONST               3 (3)
             18 LOAD_CONST               4 (4)
             21 BUILD_LIST               3
             24 LOAD_CONST               4 (4)
             27 LOAD_CONST               5 (5)
             30 LOAD_CONST               6 (6)
             33 BUILD_LIST               3
             36 BUILD_LIST               3
             39 STORE_FAST               0 (a)

  4          42 LOAD_CONST               7 (&lt;code object &lt;dictcomp&gt; at 0x1f894b0, file "&lt;input&gt;", line 4&gt;)
             45 MAKE_FUNCTION            0
             48 LOAD_FAST                0 (a)
             51 GET_ITER
             52 CALL_FUNCTION            1
             55 STORE_FAST               1 (b)

  5          58 LOAD_FAST                1 (b)
             61 RETURN_VALUE
>>> timeit(a)
0.8081288146972656"""
    ),
    (
        """>>> def a():
...     n = 1
...     return not n
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (n)

  4           6 LOAD_FAST                0 (n)
              9 UNARY_NOT
             10 RETURN_VALUE
>>> timeit(a)
0.11161303520202637""",
        """>>> def a():
...     n = 0
...     return not n
>>> dis(a)
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               0 (n)

  4           6 LOAD_FAST                0 (n)
              9 UNARY_NOT
             10 RETURN_VALUE
>>> timeit(a)
0.11124205589294434""",
        """>>> def a():
...     n = 1
...     if n:
...         return False
...     else:
...         return True
>>> dis(a)
  3           0 LOAD_CONST               1 (1)
              3 STORE_FAST               0 (n)

  4           6 LOAD_FAST                0 (n)
              9 POP_JUMP_IF_FALSE       16

  5          12 LOAD_GLOBAL              0 (False)
             15 RETURN_VALUE

  7     >>   16 LOAD_GLOBAL              1 (True)
             19 RETURN_VALUE
             20 LOAD_CONST               0 (None)
             23 RETURN_VALUE
>>> timeit(a)
0.10635685920715332""",
        """>>> def a():
...     n = 0
...     if n:
...         return False
...     else:
...         return True
>>> dis(a)
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               0 (n)

  4           6 LOAD_FAST                0 (n)
              9 POP_JUMP_IF_FALSE       16

  5          12 LOAD_GLOBAL              0 (False)
             15 RETURN_VALUE

  7     >>   16 LOAD_GLOBAL              1 (True)
             19 RETURN_VALUE
             20 LOAD_CONST               0 (None)
             23 RETURN_VALUE
>>> timeit(a)
0.10210394859313965"""
    ),
    (
        """>>> def k(x=1,y=1,z=-1):
...     return x*(y-2*z)
>>> def a():
...     d = {'x':5, 'y':3}
...     return k(**d)
>>> a()
25
>>> dis(a)
  3           0 BUILD_MAP                2
              3 LOAD_CONST               1 (5)
              6 LOAD_CONST               2 ('x')
              9 STORE_MAP
             10 LOAD_CONST               3 (3)
             13 LOAD_CONST               4 ('y')
             16 STORE_MAP
             17 STORE_FAST               0 (d)

  4          20 LOAD_GLOBAL              0 (k)
             23 LOAD_FAST                0 (d)
             26 CALL_FUNCTION_KW         0
             29 RETURN_VALUE
>>> timeit(a)
0.47187590599060059""",
        """>>> def k(x=1,y=1,z=-1):
...     return x*(y-2*z)
>>> def a():
...     return k(x=5,y=3)
>>> a()
25
>>> dis(a)
  3           0 LOAD_GLOBAL              0 (k)
              3 LOAD_CONST               1 ('x')
              6 LOAD_CONST               2 (5)
              9 LOAD_CONST               3 ('y')
             12 LOAD_CONST               4 (3)
             15 CALL_FUNCTION          512
             18 RETURN_VALUE
>>> timeit(a)
0.2616560459136963"""
    ),
    (
        """>>> def fib(n):
...     a, b = 0, 1
...     for i in range(n):
...         a, b = b, a + b
...     return a
>>> fib(25)
75025
>>> dis(fib)
  3           0 LOAD_CONST               3 ((0, 1))
              3 UNPACK_SEQUENCE          2
              6 STORE_FAST               1 (a)
              9 STORE_FAST               2 (b)

  4          12 SETUP_LOOP              37 (to 52)
             15 LOAD_GLOBAL              0 (range)
             18 LOAD_FAST                0 (n)
             21 CALL_FUNCTION            1
             24 GET_ITER
        >>   25 FOR_ITER                23 (to 51)
             28 STORE_FAST               3 (i)

  5          31 LOAD_FAST                2 (b)
             34 LOAD_FAST                1 (a)
             37 LOAD_FAST                2 (b)
             40 BINARY_ADD
             41 ROT_TWO
             42 STORE_FAST               1 (a)
             45 STORE_FAST               2 (b)
             48 JUMP_ABSOLUTE           25
        >>   51 POP_BLOCK

  6     >>   52 LOAD_FAST                1 (a)
             55 RETURN_VALUE
>>> def a():
...     return fib(25)
>>> timeit(a)
2.0159001350402832""",
        """>>> def fib(n):
...     a, b = 0, 1
...     for i in range(n):
...         x = a + b
...         a = b
...         b = x
...     return a
>>> fib(25)
75025
>>> dis(fib)
  3           0 LOAD_CONST               3 ((0, 1))
              3 UNPACK_SEQUENCE          2
              6 STORE_FAST               1 (a)
              9 STORE_FAST               2 (b)

  4          12 SETUP_LOOP              42 (to 57)
             15 LOAD_GLOBAL              0 (range)
             18 LOAD_FAST                0 (n)
             21 CALL_FUNCTION            1
             24 GET_ITER
        >>   25 FOR_ITER                28 (to 56)
             28 STORE_FAST               3 (i)

  5          31 LOAD_FAST                1 (a)
             34 LOAD_FAST                2 (b)
             37 BINARY_ADD
             38 STORE_FAST               4 (x)

  6          41 LOAD_FAST                2 (b)
             44 STORE_FAST               1 (a)

  7          47 LOAD_FAST                4 (x)
             50 STORE_FAST               2 (b)
             53 JUMP_ABSOLUTE           25
        >>   56 POP_BLOCK

  8     >>   57 LOAD_FAST                1 (a)
             60 RETURN_VALUE
>>> def a():
...     return fib(25)
>>> timeit(a)
2.2374579906463623""",
    ),
    (
        """>>> def a():
...     x=0
...     y=0
...     z=0
...     w=0
...     k=0
...     return x,y,z,w,k
>>> dis(a)
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               0 (x)

  4           6 LOAD_CONST               1 (0)
              9 STORE_FAST               1 (y)

  5          12 LOAD_CONST               1 (0)
             15 STORE_FAST               2 (z)

  6          18 LOAD_CONST               1 (0)
             21 STORE_FAST               3 (w)

  7          24 LOAD_CONST               1 (0)
             27 STORE_FAST               4 (k)

  8          30 LOAD_FAST                0 (x)
             33 LOAD_FAST                1 (y)
             36 LOAD_FAST                2 (z)
             39 LOAD_FAST                3 (w)
             42 LOAD_FAST                4 (k)
             45 BUILD_TUPLE              5
             48 RETURN_VALUE
>>> timeit(a)
0.22387209129333496""",
        """>>> def a():
...     x=y=z=w=k=0
...     return x,y,z,w,k
>>> dis(a)
  3           0 LOAD_CONST               1 (0)
              3 DUP_TOP
              4 STORE_FAST               0 (x)
              7 DUP_TOP
              8 STORE_FAST               1 (y)
             11 DUP_TOP
             12 STORE_FAST               2 (z)
             15 DUP_TOP
             16 STORE_FAST               3 (w)
             19 STORE_FAST               4 (k)

  4          22 LOAD_FAST                0 (x)
             25 LOAD_FAST                1 (y)
             28 LOAD_FAST                2 (z)
             31 LOAD_FAST                3 (w)
             34 LOAD_FAST                4 (k)
             37 BUILD_TUPLE              5
             40 RETURN_VALUE
>>> timeit(a)
0.21921992301940918""",
        """>>> def a():
...     x,y,z,w,k=0,0,0,0,0
...     return x,y,z,w,k
>>> dis(a)
  3           0 LOAD_CONST               2 ((0, 0, 0, 0, 0))
              3 UNPACK_SEQUENCE          5
              6 STORE_FAST               0 (x)
              9 STORE_FAST               1 (y)
             12 STORE_FAST               2 (z)
             15 STORE_FAST               3 (w)
             18 STORE_FAST               4 (k)

  4          21 LOAD_FAST                0 (x)
             24 LOAD_FAST                1 (y)
             27 LOAD_FAST                2 (z)
             30 LOAD_FAST                3 (w)
             33 LOAD_FAST                4 (k)
             36 BUILD_TUPLE              5
             39 RETURN_VALUE
>>> timeit(a)
0.21370291709899902"""
    ),
    (
        """>>> def a():
...     n = 123.123
...     return int(n)
...
>>> a()
123
>>> dis(a)
  3           0 LOAD_CONST               1 (123.123)
              3 STORE_FAST               0 (n)

  4           6 LOAD_GLOBAL              0 (int)
              9 LOAD_FAST                0 (n)
             12 CALL_FUNCTION            1
             15 RETURN_VALUE
>>> timeit(a)
0.18375706672668457
""",
        """>>> def a():
...     n = 123.123
...     return math.floor(n)
...
>>> a()
123.0
>>> dis(a)
  3           0 LOAD_CONST               1 (123.123)
              3 STORE_FAST               0 (n)

  4           6 LOAD_GLOBAL              0 (math)
              9 LOAD_ATTR                1 (floor)
             12 LOAD_FAST                0 (n)
             15 CALL_FUNCTION            1
             18 RETURN_VALUE
>>> timeit(a)
0.17320585250854492
""",
        """>>> def a():
...     n = 123.123
...     return math.trunc(n)
...
>>> a()
123
>>> dis(a)
  3           0 LOAD_CONST               1 (123.123)
              3 STORE_FAST               0 (n)

  4           6 LOAD_GLOBAL              0 (math)
              9 LOAD_ATTR                1 (trunc)
             12 LOAD_FAST                0 (n)
             15 CALL_FUNCTION            1
             18 RETURN_VALUE
>>> timeit(a)
0.2588181495666504
""",
        """>>> def a():
...     n = 123.123
...     return n // 1
...
>>> a()
123.0
>>> dis(a)
  3           0 LOAD_CONST               1 (123.123)
              3 STORE_FAST               0 (n)

  4           6 LOAD_FAST                0 (n)
              9 LOAD_CONST               2 (1)
             12 BINARY_FLOOR_DIVIDE
             13 RETURN_VALUE
>>> timeit(a)
0.19820308685302734
""",
    )
)

print template.render(tests=[
    {
        'n': k + 1,
        'span': 12 / len(v),
        'cases': v,
    }
    for k, v in enumerate(tests)
    ]
)
