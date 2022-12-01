## Part 1

Find the maximum calories in the input file, which is organized by each
row having a calorie value for a given snack carried by an elf, and each
elf’s snack list is split by an empty line.

``` r
calories <- readr::read_lines('../inputs/calories.txt')

calories_list <- c(0)
elf_ID <- 1

for (cal in calories) {
    if (cal == "") {
      elf_ID <- elf_ID + 1
      calories_list[elf_ID] <- 0
    } else {
      calories_list[elf_ID] <- calories_list[elf_ID] + strtoi(cal)
  }
}

print(max(calories_list))
```

    ## [1] 72602

## Part 2

Find the sum of the top three elves’ snacks.

``` r
calories <- readr::read_lines('../inputs/calories.txt')

calories_list <- c(0)
elf_ID <- 1

for (cal in calories) {
    if (cal == "") {
      elf_ID <- elf_ID + 1
      calories_list[elf_ID] <- 0
    } else {
      calories_list[elf_ID] <- calories_list[elf_ID] + strtoi(cal)
  }
}

sorted <- sort(calories_list, decreasing=TRUE)

print(sorted[1] + sorted[2] + sorted[3])
```

    ## [1] 207410
