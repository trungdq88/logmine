logmine - a log pattern analyzer
==

```
usage: logmine [-h] [-m MAX_DIST] [-v [VARIABLES [VARIABLES ...]]]
               [-d DELIMETERS] [-min MIN_MEMBERS] [-k1 K1] [-k2 K2]
               [-s {desc,asc}] [-da] [-p PATTERN_PLACEHOLDER] [-dhp] [-dm]
               [-dhv] [-sc]
               [file [file ...]]

LogMine: a log pattern analyzer

positional arguments:
  file                  Filenames or glob pattern to analyze.

optional arguments:
  -h, --help            show this help message and exit
  -m MAX_DIST, --max-dist MAX_DIST
                        This parameter control how the granularity of the
                        clustering algorithm. Lower the value will provide
                        more granular clusters (more clusters generated).
  -v [VARIABLES [VARIABLES ...]], --variables [VARIABLES [VARIABLES ...]]
                        List of variables to replace before process the log
                        file. A variable is a pair of name and a regex
                        pattern. Format: "name:/regex/". During processing
                        time, LogMine will consider all texts that match
                        varible regexes to be the same value. This is useful
                        to reduce the number of unnecessary cluster generated,
                        with trade off of processing time.
  -d DELIMETERS, --delimeters DELIMETERS
                        A regex pattern used to split a line into multiple
                        fields.
  -min MIN_MEMBERS, --min-members MIN_MEMBERS
                        Minimum number of members in a cluster to show in the
                        result.
  -k1 K1, --fixed-value-weight K1
                        Internal weighting variable. This value will be used
                        as the weight value when two fields have the same
                        value. This is used in the score function to calculate
                        the distance between two lines.
  -k2 K2, --variable-weight K2
                        Similar to k1 but for comparing variables. Two
                        variable is considering the same if they have same
                        name.
  -s {desc,asc}, --sorted {desc,asc}
                        Sort the clusters by number of members.
  -da, --disable-number-align
                        Disable number align in output.
  -p PATTERN_PLACEHOLDER, --pattern-placeholder PATTERN_PLACEHOLDER
                        Use a string as placeholder for patterns in output.
  -dhp, --disable-highlight-patterns
                        Disable highlighting for patterns in output.
  -dm, --disable-mask-variables
                        Disable masks for variables in output. When disabled
                        variables will be shown as the actual value.
  -dhv, --disable-highlight-variables
                        Disable highlighting for variables in output.
  -sc, --single-core    Force LogMine to only run on 1 core. This will
                        increase the processing time. Note: the result output
                        can be different compare to when run with multicores,
                        this is expected.
```
