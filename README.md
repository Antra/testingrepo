# testingrepo
Basic testing repo just for mocking about, trying to figure out how to import individual toolkit files.

In this case, the following works -- both for local import and for importing via Github.

## Local
```
from example import example as ex
ex.example()
```


## Github:
```
pip install -e "git+https://github.com/Antra/testingrepo.git#egg=example"
```

followed by:
```
from example import example as ex
ex.example()
```