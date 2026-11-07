#!/usr/bin/env python3
"""Bounded local demonstration of documentation-test evidence limits.

No external services, filesystem mutation, credentials, or third-party packages.
Synthetic examples illustrate documented Python doctest mechanics, not their
frequency in real documentation or their effect on developer task performance.
"""
import doctest
import hashlib
import json
from pathlib import Path
import platform


def run_example(text, context=None, flags=0):
    test = doctest.DocTestParser().get_doctest(
        text, context or {}, "synthetic-documentation", "synthetic.txt", 0
    )
    runner = doctest.DocTestRunner(optionflags=flags)
    messages = []
    result = runner.run(test, out=messages.append)
    return {"attempted": result.attempted, "failed": result.failed}


def main():
    fragment = ">>> tenant\n'example-test-tenant'\n"
    complete = ">>> tenant = 'example-test-tenant'\n>>> tenant\n'example-test-tenant'\n"
    broad = '>>> print("job failed")\njob ...\n'
    exact = '>>> print("job failed")\njob succeeded\n'
    cases = {
        "fragment_with_injected_context": run_example(
            fragment, {"tenant": "example-test-tenant"}
        ),
        "same_fragment_without_injected_context": run_example(fragment),
        "complete_example_without_injected_context": run_example(complete),
        "failed_job_matches_broad_output": run_example(broad, flags=doctest.ELLIPSIS),
        "failed_job_fails_success_assertion": run_example(exact),
    }
    expected_failures = {
        "fragment_with_injected_context": 0,
        "same_fragment_without_injected_context": 1,
        "complete_example_without_injected_context": 0,
        "failed_job_matches_broad_output": 0,
        "failed_job_fails_success_assertion": 1,
    }
    if any(cases[key]["failed"] != value for key, value in expected_failures.items()):
        raise SystemExit("Unexpected probe behavior; inspect Python/doctest version")
    print(json.dumps({
        "scope": "synthetic Python doctest mechanics; no human or agent usability result",
        "python": platform.python_version(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "cases": cases,
    }, indent=2))


if __name__ == "__main__":
    main()
