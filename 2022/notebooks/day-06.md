## Part 1

``` r
signal <- readr::read_file('../inputs/signal.txt')

pattern <- "[a-z]*([a-z])[a-z]*\\1"  # finds a duplicate character in a string

for (i in 4:nchar(signal)) {
  potential_packet <- substr(signal, i-3, i)
  if (regexpr(pattern, potential_packet) == -1) {
    break
  }
}
print(i)
```

    ## [1] 1542

## Part 2

``` r
for (i in 14:nchar(signal)) {
  potential_packet <- substr(signal, i-13, i)
  if (regexpr(pattern, potential_packet) == -1) {
    break
  }
}
print(i)
```

    ## [1] 3153
