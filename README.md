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


## Bitbucket
When the module is stored as .repo/tools/example+/example/example.py, where the setup.py is in the "+" folder:
```
pip install -e "git+https://user@bitbucket-repo/scm/tools/temp.git#egg=example&subdirectory=tools/example"
```

followed by:
```
from example import example as ex
ex.example()
```