# eddy

Yet another Python progress spinner. Original credit/idea goes to a [StackOverflow post](https://stackoverflow.com/a/4995896).

[![demo](https://asciinema.org/a/H9YswufWCmp6U3iQvTFhNwJjU.png)](https://asciinema.org/a/H9YswufWCmp6U3iQvTFhNwJjU?autoplay=1)

## Example

```python
import eddy
import time

eddy.start()
time.sleep(3)
eddy.stop()

```

## Testing

Use `pytest` to run through all the presets:

```bash
cd eddy
pyest -s
```


