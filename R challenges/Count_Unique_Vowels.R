# List of vowels
vowels = c('a','e','i','o','u')
# String to search for vowels
search_string = tolower("Hello World!")
# Initial count of unique vowels
count = 0

# Loop through the vowels.  If the current vowel is in the search string, bump the counter.
for (x in vowels) {
  if (grepl(x, search_string)) {
    count = count + 1
  }
}

cat("The number of unique vowels is", count)

