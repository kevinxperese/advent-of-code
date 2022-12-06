## Part 1

``` r
range_pairs <- readr::read_csv('../inputs/assignment_pairs.txt', 
                               col_names=c('range1', 'range2'),
                               show_col_types = FALSE)

df <- range_pairs %>% 
  separate(range1, c('min1', 'max1'), '-', convert=TRUE) %>% 
  separate(range2, c('min2', 'max2'), '-', convert=TRUE)

fully_overlap <- 0
for (i in 1:nrow(range_pairs)) {
  if (((df[i, 'min1'] >= df[i, 'min2']) & (df[i, 'max1'] <= df[i, 'max2'])) |
      ((df[i, 'min2'] >= df[i, 'min1']) & (df[i, 'max2'] <= df[i, 'max1']))) {
    fully_overlap = fully_overlap + 1
  }
}

print(fully_overlap)
```

    ## [1] 487

## Part 2

``` r
range_pairs <- readr::read_csv('../inputs/assignment_pairs.txt', 
                               col_names=c('range1', 'range2'),
                               show_col_types = FALSE)

df <- range_pairs %>% 
  separate(range1, c('min1', 'max1'), '-', convert=TRUE) %>% 
  separate(range2, c('min2', 'max2'), '-', convert=TRUE)

intersection <- 0
for (i in 1:nrow(range_pairs)) {
  if (((df[i, 'min2'] <= df[i, 'max1']) & (df[i, 'max1'] <= df[i, 'max2'])) |
      ((df[i, 'min1'] <= df[i, 'max2']) & (df[i, 'max2'] <= df[i, 'max1']))) {
    intersection = intersection + 1
  }
}

print(intersection)
```

    ## [1] 849
