#!/usr/bin/env python3

import sys
from pathlib import Path

import compactify

sys.path.append(str(Path(__file__).parents[1]))
import testing_infra


def main() -> int:
    test_cases = (
        (
            """
            """,
            """
            """,
        ),
        ("", ""),
        (
            """
()()
()()
()()
            """,
            """
()()
()()
()()
            """,
        ),
        (
            """
(
    (
        [[{
            ()
        }]]
    ),
)
            """,
            """
(([[{
            ()
        }]]
    ),
)
            """,
        ),
        (
            """
(
    (
        [[
            ()
        ]
        ]
    ), foo(),
)
            """,
            """
(([[
            ()
        ]
        ]
    ), foo(),
)
            """,
        ),
        (
            """
f(
    (
        [[
            ()
        ]
        ]
    ), foo(),
)
            """,
            """
f(([[
            ()
        ]
        ]
    ), foo(),
)
            """,
        ),
        (
            """
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
            """,
            """
e = sum([
        x**2
        for x in (
            x
            for (_, x) in zip([
                    i
                    for (_, i) in enumerate(range(102, 202))
                ],
                range(100)
            )
        )
    ]
)
            """,
        )
    )

    for source, expected_abstraction in test_cases:
        lines = source.splitlines(keepends=False)
        compactify.core.collapse_lparen_lines(lines)
        processed_content = "\n".join(lines)
        if not testing_infra.check_fixes_equal(processed_content, expected_abstraction):
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
