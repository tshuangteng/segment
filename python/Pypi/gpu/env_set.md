
### forces applications to use the default language for output
```
locale -a
export LC_ALL='C.UTF-8'
locale
```

### controls the number of threads that many libraries. for example numpy
```
export OMP_NUM_THREADS=1
```