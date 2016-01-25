### What is this?
Here you can find a few implementations of PageRank in Python 2.7. No libraries are used. This was a learning experiment. There are few versions that all use power method.

* main.py - first implementation that is very slow and shouldn't be used
* improve.py - fastest implementation that does 1000 nodes in a 1,5 seconds
* matrix.py - a bit different method that is a bit slower than previus, but has most potential for improvement

### How to use?
There is a basic test cases set up in tests folder. If you want to create different size test cases then just run `generate.py`.

Once you edit your settings just run any of the scripts and it should print out PageRank vector.

### How to improve this?
You should try an add Numpy and Pandas libraries if you are looking for maximum speed. Also, you should use PyPy interpreter instead of basic Python one. This was prohibited in my learning experiment, but you should definetly expand there.
