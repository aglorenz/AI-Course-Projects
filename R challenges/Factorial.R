factorial <- function(n) {
  if (n == 1 || n == 0) {
    return(1)
  } else {
      return(n * factorial(n-1))
  }
}

cat(factorial(5))



