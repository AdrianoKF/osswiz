# OSSWiz - the Wizard of OSS

[![](https://img.shields.io/pypi/v/osswiz)](https://pypi.org/project/osswiz) ![GitHub](https://img.shields.io/github/license/AdrianoKF/osswiz)

## Usage

You can run osswiz checks (through [repo-review](https://repo-review.readthedocs.io/en/latest/)) from the command line to interactively check your project:

```console
# If you have the package installed
$ osswiz

# If you don't have the package installed
$ pipx run osswiz
# or, using uv:
$ uvx osswiz
```

If want to run checks automatically whenever you make a commit, you can use the osswiz [`pre-commit`](https://pre-commit.com) hook:

```yaml
- repo: https://github.com/AdrianoKF/osswiz
  rev: main # or desired version from releases/tags
  hooks:
    - id: osswiz
```

## License

This project is licensed under the terms of the Apache-2.0 license.
