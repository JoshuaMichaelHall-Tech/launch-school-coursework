```
Given an array of positive or negative integers

 I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:

It can happen that a sum is 0 if some numbers are negative!
Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst
others.


P
input: array of integers
output: array of arrays containing 2 values, the first is each of the prime factors, 
the second is the sum of the original numbers for which the first is a factor

E


D
collection of prime numbers up to highest input -1

A
helper - get prime numbers
  takes an integer and returns array of prime numbers
  
helper - get primes
  takes array
  set result array
    for each element in original array
      pass to helper (get prime numbers) to get primes and add array with (number and (array of primes))
  return result

helper - get qualified sums
  takes original input array and current qualified prime
  for each 
  
main
  takes input array
  convert to primes collection
  for collection in collection,
    convert array at index 1 to (qualified sums)

```

def sum_of_divided(lst)
  
end
