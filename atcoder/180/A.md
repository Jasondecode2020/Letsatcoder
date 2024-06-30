- 1. used list groups method of list 'ABA...' or 'BAB...' in a group of arrays.
- 2. if the length of each listed group, if the length is more than 3, use ceil of x / 2 to get how many ways in each group
- 3. use combinatorics method of multiply each number of the group.

```
The idea is that, if it is ABAB, it will become AB, or matter 'ABA' or 'BAB', there are 2 ways.
If it is BABAB, it will first become 'BAB', than become 'B', there are 3 ways.
```