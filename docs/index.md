# k3str

[![Action-CI](https://github.com/pykit3/k3str/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3str/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3str/badge/?version=stable)](https://k3str.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3str)](https://pypi.org/project/k3str)

String operation utilities for encoding conversion.

k3str is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3str
```

## Quick Start

```python
import k3str

# Convert string to bytes
b = k3str.to_bytes('我')
print(repr(b))  # b'\xe6\x88\x91'

# Convert to UTF-8 bytes
utf8_bytes = k3str.to_utf8('hello')

# Get default encoding
print(k3str.default_encoding)
```

## API Reference

::: k3str

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
