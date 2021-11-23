# tree-fizz-buzz

Conduct “FizzBuzz” on a k-ary tree while traversing through it to create a new tree.
Set the values of each of the new nodes depending on the corresponding node value in the source tree.

## Challenge

Write a function called fizz buzz tree
Arguments: k-ary tree
Return: new k-ary tree

## Approach & Efficiency
Time : O(N)
space : O(1)

## API

Methods:

Determine whether or not the value of each node is divisible by 3, 5 or both. by Create a new tree with the same structure as the original, but the values modified as follows:

If the value is divisible by 3, replace the value with “Fizz”
If the value is divisible by 5, replace the value with “Buzz”
If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
If the value is not divisible by 3 or 5, simply turn the number into a String.

[The code](/code_challenges/tree-fizz-buzz/tree_fizz_buzz/tree_fizz_buzz.py)

[The test](/code_challenges/tree-fizz-buzz/tests/test_tree_fizz_buzz.py)

## whiteBoard:

![](/code_challenges/tree-fizz-buzz/Lab18.png)