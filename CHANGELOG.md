# CHANGELOG



## v0.1.0 (2025-01-27)

### Feature

* feat: initialize mypy exhaustive check project

- Add initial project structure and files.
- Include Pipfile for dependency management.
- Create base plugin and dispatcher for mypy integration.
- Define CheckType enum for plugin checks.
- Update README with project title. ([`6836a4d`](https://github.com/ELC/mypy-exhaustive-check/commit/6836a4d170533bcacc34de5dc92a7c7c8e3fb908))

### Fix

* fix(dict_check): improve error messages and add plugin

- Ensure error messages for missing enum members are sorted.
- Add a plugin function to expose the ExhaustiveDictPlugin.
- Update test cases to validate behavior for exhaustive checks.
- Install the package in the CI workflow before running tests. ([`658a519`](https://github.com/ELC/mypy-exhaustive-check/commit/658a519473368e390cb0c180d67a5f7b32d10f84))

### Unknown

* Initial commit ([`0b0d702`](https://github.com/ELC/mypy-exhaustive-check/commit/0b0d70294c44ef77ae4463ca9bb9b2db50f277b9))
