# Masonite Audit

<p align="center">
    <img src="https://banners.beyondco.de/Masonite%20Audit.png?theme=light&packageManager=pip+install&packageName=masonite-audit&pattern=charlieBrown&style=style_2&description=Keep+track+of+all+your+model+changes+with+ease.&md=1&showWatermark=1&fontSize=100px&images=adjustments&widths=50&heights=50">
</p>

<p align="center">
  <img alt="GitHub Workflow Status" src="https://github.com/py-package/masonite-audit/actions/workflows/pythonapp.yml/badge.svg">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/masonite-audit">
  <img alt="issues" src="https://img.shields.io/github/issues/py-package/masonite-audit">
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python Version">
  <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/py-package/masonite-audit">
  <img alt="License" src="https://img.shields.io/github/license/py-package/masonite-audit">
  <a href="https://github.com/py-package/masonite-audit/stargazers"><img alt="star" src="https://img.shields.io/github/stars/py-package/masonite-audit" /></a>
  <img alt="downloads" src="https://img.shields.io/pypi/dm/masonite-audit?style=flat" />
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Introduction

Keep track of all your model changes with ease.

## Getting Started

Install the package using pip:

```bash
pip install masonite-audit
```

Add AuditProvider to your project in `config/providers.py`:

```python
# config/providers.py
# ...
from masonite_audit import AuditProvider

# ...
PROVIDERS = [
    # ...
    # Third Party Providers
    AuditProvider,
    # ...
]
```

Publish the package configuration files.

```bash
python craft package:publish masonite-audit
```

This will add migrations and other `masonite-audit` related configuration to your project. Run your migrations to create the related database tables.

```bash
python craft migrate
```

Finally, inherit `Audit` mixin into all the models for which you need audit logging.

```python
from masonite_audit.mixins import Audit
class YourModel(Audit):
    pass
```

If you want to get the audit history for a model, you can use the `history` method:

```python
user = User.find(1)
user.history()
```

In order to rollback to previous versions of a model, you can use the `rollback` method:

```python
user = User.find(1)
user.rollback() # to rollback to previous version
# or
user.rollback(step=4) # to rollback to version 4
```



## License

Masonite Audit is open-sourced software licensed under the [MIT license](LICENSE).

