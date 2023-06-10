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
(
    (
        [[{
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
            [[{
                        ()
            }]]
    ),
)
            """,
            """
(
    (
        [[{
            ()
        }]]
    ),
)
            """,
        ),
    )

    for source, expected_abstraction in test_cases:
        lines = source.splitlines(keepends=False)
        compactify.core.remove_excessive_indent(lines)
        processed_content = "\n".join(lines)
        if not testing_infra.check_fixes_equal(processed_content, expected_abstraction):
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
