# Miscellaneous stuff

Fix annoying `FutureWarning ...` in PyCharm's Jupyter Console

```python
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
```