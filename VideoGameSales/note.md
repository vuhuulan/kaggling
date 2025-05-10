# Data Exploration

We do some vanilla exploration first, how about `Genre` and its total amount?
Great, and 12 we have. Next, how about the total games in each genre, for
example "Action" genre. And, oh?!:

```
Rank            3316
Name            3316
Platform        3316
Year            3253
Genre           3316
Publisher       3309
NA_Sales        3316
EU_Sales        3316
JP_Sales        3316
Other_Sales     3316
Global_Sales    3316
```

Are you seeing this? There are more in "Name" than in "Year" and "Publisher".
What does this mean? How can we further investigate this?

Assume that every game is uniquely named, then there are 3316 games. If all the
games are properly noted, then we should have 3316 of every other thing, in
other words, there are some games lacked information on "Year" and "Publisher".

We can clean this with the `dropna()` function. Easey!!
