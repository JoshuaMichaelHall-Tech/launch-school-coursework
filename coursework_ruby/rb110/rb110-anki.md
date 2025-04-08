## What are the different types of collections in Ruby?
Collections in Ruby include arrays and hashes. Arrays store ordered lists of elements accessed by index, while hashes store key-value pairs.

## How do you handle "out of bounds" with arrays?
When accessing an index that is out of bounds, Ruby returns `nil`. To determine if this `nil` represents "out of bounds" rather than an actual `nil` value in the array, use the `fetch` method, which will raise an `IndexError` for out-of-bounds indices.

## How do you handle "key not found" with hashes?
When accessing a key that doesn't exist in a hash, Ruby returns `nil`. To determine if this `nil` represents "key not found" rather than an actual `nil` value in the hash, use the `fetch` method, which will raise a `KeyError` for keys that don't exist.

## What are nested collections?
Nested collections are collections that contain other collections as elements. For example, an array can contain other arrays or hashes, and a hash can have arrays or other hashes as values.

## How do you reference elements in nested collections?
Use chained bracket notation. For example, `arr[0][1]` accesses the second element of the first sub-array in `arr`. For hashes, you can use the key: `hash[:key][:nested_key]`.

## How do you loop through collections?
You can use methods like `each`, `each_with_index`, or manual loops with counters. For example:
```ruby
array.each { |element| puts element }
```
or
```ruby
counter = 0
loop do
  break if counter == array.size
  puts array[counter]
  counter += 1
end
```

## What is the difference between `each`, `map`, and `select`?
- `each` iterates through a collection and returns the original collection.
- `map` transforms each element based on the block's return value and returns a new collection of the same size.
- `select` filters elements based on the truthiness of the block's return value and returns a new collection containing only the elements for which the block returned a truthy value.

## What is selection from collections?
Selection is the process of picking certain elements from a collection based on some criteria. In Ruby, you can use methods like `select` or implement it manually with a loop and conditional statement.

## What is transformation of collections?
Transformation is the process of creating a new collection where each element has been modified in some way. In Ruby, you can use `map` or implement it manually.

## How do you sort collections in Ruby?
Use the `sort` or `sort_by` method. The `sort` method uses the `<=>` (spaceship) operator to compare elements. You can also pass a block to these methods for custom sorting.

## How do you pass blocks to iterative methods?
Blocks can be passed to methods implicitly using `do...end` or `{...}`, or explicitly using the `&block` parameter in the method definition. Within the method, you can use `yield` to call the block.

## What is the difference between shallow copy and deep copy?
A shallow copy creates a new object but shares references to nested objects with the original. A deep copy creates a completely independent copy, including copies of all nested objects. Methods like `dup` and `clone` create shallow copies in Ruby.

## What is method chaining?
Method chaining is calling multiple methods in sequence, where each method operates on the return value of the previous method. For example: `str[2, 3][0]` first gets a substring and then gets the first character of that substring.

## What are common methods used with Ruby collections?
Common methods include:
- `any?`: Returns true if the block returns a truthy value for any element
- `all?`: Returns true if the block returns a truthy value for all elements
- `each_with_index`: Iterates with both the element and its index
- `each_with_object`: Iterates with an object that can be updated in the block
- `first`: Returns the first element or the first n elements
- `include?`: Checks if an element exists in the collection
- `partition`: Divides elements into two arrays based on the block's return value
