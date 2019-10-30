ls -l src/*_test.py | awk '{ print $9 }' | awk '!/^\s*$/' | xargs -I{} python {}
