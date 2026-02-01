# includes (namespace package)

Small, explicit, and pragmatic helpers for dynamic imports in Python.

This project provides a **namespace package** (`includes.*`) implementing
utility functions to dynamically include/import modules using a concise,
script-friendly syntax.

It is intended for **personal tools, experiments, and controlled environments**,
not as a general-purpose replacement for Python’s import system.

---

## Package type

This is a **namespace package** (PEP 420):

installed independently but sharing the same `includes` namespace.

## Structure

```text
includes/
├── includes/
│   └── core.py
├── pyproject.toml
├── README.md
└── test.py

```


## Installation

### Development / editable install (recommended)

```bash
pip install -e .
```

### Standard install

```bash
pip install .
```

The package becomes available system-wide or inside the active virtual
environment.

---


### Example

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#pylint:disable=W0301

from includes import include,includes;

include("numpy as np");
include("pygame as pg");
include("* from sys");

includes(
    "time",
    "math",
    ["numpy as np", "pygame"]
);
```

Debug output is controlled by the `DBG` variable inside `core.py`.

---

##  Provided functions

Example:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#pylint:disable=W0301

from includes import *;

debug(ON);
include("numpy as np");
include("pygame as pg");
debug(INFO);
includes("time", "* from sys");
debug(off);
if(debug):
    includes("datetime as dt");
```

```bash
# python test.py 

numpy included
pygame included
time included
sys included
```

### `includes(*args)`

Convenience wrapper that accepts:

* multiple strings
* lists of strings
* mixed arguments

---

## Design notes & limitations

* Uses `exec()` internally
* Breaks static analysis, autocompletion, and type checking
* Intended for **trusted input only**
* Best suited for scripts, tools, REPLs, and experiments

This is a **deliberate trade-off**, not an accident.

If you need static safety, prefer standard Python imports.

---


##  License

  Copyright 2018- William Martinez Bas <metfar@gmail.com>

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor,
  MA 02110-1301, USA.

 ---------------------------------------------------------------------
 Package:			includes
 Version:			0.8.4
 Description;		allows to import using include/includes
 ---------------------------------------------------------------------

---

## Philosophy

> Explicit is better than implicit.
> Dynamic, but controlled.
> Simple tools for people who know what they are doing.


### Enjoy

Have a nice one!

                                                       - oOo -
