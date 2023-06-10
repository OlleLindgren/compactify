"""Integration test cases, used in test_format_code and test_format_file"""

import testing_infra

INTEGRATION_TEST_CASES = (
    ("", ""),
    (
        """
for x in range(100):
    if x > 10:
        y = 13
    else:
        x += 1
        x *= 12
        print(x > 30)
        y = 100 - sum(x, 2, 3)
print(x)
        """,
        """
for x in range(100):
    if x > 10:
        y = 13
    else:
        x += 1
        x *= 12
        print(x > 30)
        y = 100 - sum(x, 2, 3)
print(x)
        """,
    ),
    (
        """
sum({})
        """,
        """
sum({})
        """,
    ),
    (
        """
sum(
    {
        1, 2, 3
    }
)
        """,
        """
sum({
    1, 2, 3
})
        """,
    ),
    (
        """
X = sorted(range(100))[::3]
Z = {
    **{ww: ww + 1 for ww in range(12)},
    22: 33,
    99: 88,
    **{w**3: w**2 for a in X if a % 3 == 0 and a % 4 == 2 for w in X if w > len(X) // 2},
    **{w ** (-1): w ** (-2) for a in X if a % 5 == 0 and a % 9 == 2},
    1: 333,
}
if all(y in {1, 2, 5} for y in set(Z)):
    print(Z, X)
        """,
        """
X = sorted(range(100))[::3]
Z = {
    **{ww: ww + 1 for ww in range(12)},
    22: 33,
    99: 88,
    **{w**3: w**2 for a in X if a % 3 == 0 and a % 4 == 2 for w in X if w > len(X) // 2},
    **{w ** (-1): w ** (-2) for a in X if a % 5 == 0 and a % 9 == 2},
    1: 333,
}
if all(y in {1, 2, 5} for y in set(Z)):
    print(Z, X)
        """,
    ),
    (
            """
import numpy as np

i, j, k = 10, 11, 12

a = np.random.random((i, j))
b = np.random.random((j, k))

u = np.array(
    [
        [
            np.sum(
                a__ * b__
                for a__, b__ in zip(a_, b_)
            )
            for a_ in a
        ]
        for b_ in b.T
    ]
).T

print(u)
            """,
        """
import numpy as np

i, j, k = 10, 11, 12

a = np.random.random((i, j))
b = np.random.random((j, k))

u = np.array([[
    np.sum(
        a__ * b__
        for a__, b__ in zip(a_, b_)
    )
    for a_ in a
    ]
    for b_ in b.T
    ]
).T

print(u)
            """,
    ),
    (
        """
import numpy as np

i, j, k = 10, 11, 12

a = np.random.random((i, j))
b = np.random.random((j, k))

u = np.array(
    [
        [
            np.dot(b[:, i], a[j, :])
            for i in range(b.shape[1])
        ]
        for j in range(a.shape[0])
    ]
)

print(u)
        """,
        """
import numpy as np

i, j, k = 10, 11, 12

a = np.random.random((i, j))
b = np.random.random((j, k))

u = np.array([[
    np.dot(b[:, i], a[j, :])
    for i in range(b.shape[1])
    ]
    for j in range(a.shape[0])
])

print(u)
        """,
    ),
    (
        """
import pandas as pd
DF = pd.DataFrame([{
    "foo": 10 + i,
    "bar": 10 - i
    }
    for i in range(10)
])
X = sum((
    row[1 + 1] + row.foo - row.bar
    for row in DF.itertuples()
)) + sum(DF.index)
print(X)
        """,
        """
import pandas as pd
DF = pd.DataFrame([{
    "foo": 10 + i,
    "bar": 10 - i
    }
    for i in range(10)
])
X = sum((
    row[1 + 1] + row.foo - row.bar
    for row in DF.itertuples()
)) + sum(DF.index)
print(X)
        """,
    ),
    (
        """
def foo():
    e = sum(
        [
            x**2
            for x in (
                x
                for (_, x) in zip(
                    [
                        i
                        for (_, i) in enumerate(range(102, 202))
                    ],
                    range(100)
                )
            )
        ]
    )
    return e

print(foo())
        """,
        """
def foo():
    e = sum([
        x**2
        for x in (
            x
            for (_, x) in zip([
                i
                for (_, i) in enumerate(range(102, 202))
                ],
                range(100)
    ))])
    return e

print(foo())
        """,
    ),
    (
        """
print(
    sum(
        [
            a for a in range(6, 10) if a % 2 == 0
        ]
    )
)
        """,
        """
print(
    sum([
        a for a in range(6, 10) if a % 2 == 0
]))
        """,
    ),
)
