# Report for assignment 3

## 1. Project
Name: keon/algorithms

URL: https://github.com/keon/algorithms

A python collection of different algorithms.

## Onboarding experience
Did it build and run as documented?
> It was installed as documented for everyone and all tests worked.

## 2. Complexity
1. What are your results for ten complex functions?
> Complexity given first, function & file location second
> 1. CCN: 14, count_islands, @40-65@./algorithms/bfs/count_islands.py
> 2. CCN: 13, pacific_atlantic, @32-54@./algorithms/dfs/pacific_atlantic.py
> 3. CCN: 10, maximum_flow_bfs, @28-87@./algorithms/graph/maximum_flow_bfs.py
> 4. CCN: 10, scc, @53-78@./algorithms/graph/satisfiability.py
> 5. CCN 13, get_skyline, @39-60@./algorithms/heap/skyline.py
> 6. CCN 14, intersection, @21-64@./algorithms/linkedlist/intersection.py
> 7. CCN 10, solve_chinese_remainder, @7-39@./algorithms/maths/chinese_remainder_theorem.py
> 8. CCN 11, pattern_match.backtrack, @23-40@./algorithms/backtrack/pattern_match.py
> 9. CCN 12, maze_search, @29-66@./algorithms/bfs/maze_search.py
> 10. CCN 12, ladder_length, @24-64@./algorithms/bfs/word_ladder.py
   
   * Did all methods (tools vs. manual count) get the same result?
> Yes, we checked number 1, 3, 6, 7, 8 and they all checked out.
   * Are the results clear?
> Compared to the lizard output the manual result was clear
2. Are the functions just complex, or also long?
> In general the functions with high cyclomatic complexity are long. The reason being that in order to have high CCN the function must contain a certain amount of if statements, loops etc. However, that is not necessarily the case. One line of code could have high CCN but that would be considered bad coding practices.
3. What is the purpose of the functions?
> `count_islands`: `count_islands` takes a grid of 1s (which represent land) and 0s (which represent water) and counts the number of horizontally and/or vertically connected 1s (which represent islands) in the grid. The high CC is mainly due to the program checking all of the different directions when determining if something is an island or not; this leads to if statements with multiple logical AND statements within them.

> `maximum_flow_bfs`:  The function gives the maximum flow given a NxN matrix. It uses BFS to conduct the search. The high CCN is necessary for the function to perform as expected.

> `intersection`: The purpose of these function is to find common nodes in a pointer based data structure if elements in the data structure have a pointer in common than than that element is returned 

> `pattern_match`: Returns true if a given string pattern makes up the given larger string, otherwise returns false

> `solve_chinese_remainder`: Finds the smallest number x that satisfies the equations x mod y1 = z1, x mod y2 = z2, …, etc using the chinese remainder theorem if applicable.

4. Are exceptions taken into account in the given measurements?
> Exceptions are taken into account when they manually raised. 

5. Is the documentation clear w.r.t. all the possible outcomes?
> `count_islands`: The documentation for the `count_islands` function lists 4 examples that illustrate the different outcomes well. 

> `maximum_flow_bfs`: The comments give a clear understanding of what the branch does and the requirements for the code to enter the path. 

>  `intersection`: Not really since the comments that document the function states that it returns the node that the data structure with common pointers if any. It's not clear what would happen if the datstruce contains more than one node with a common pointer. Do we return both or just the first one we find? There is also no testing for a case like this.

> `pattern_match`: Not in the case of empty strings or when something that isn’t a string is given as input

> `solve_chinese_remainder`: The documentation does not specify when manual exceptions will be raised, it is only clear through checking the actual code. 

## 3. DIY & Coverage improvement
> We used arrays initiated in the function that contained X amount of boolean values. When we reached a branch the flag was set to True. The unique ID was the index in the array. 

> Manual branch coverage for `count_islands` is implemented on the `count_islands` branch [here](https://github.com/will-berg/assignment3/tree/count_islands).
> The branch coverage of the unit tests for the `count_islands` function is 100%, this result was consistent with the result that we got when using the `coverage.py` tool.

> Since the branch coverage for `count_islands` already was 100%, we will be adding tests for the the `multiply` function in `sparse_mul.py`. The `multiply` function was not tested prior to this implementation, so the branch coverage beforehand was 0% and no requirements were tested. The following requirements should reasonably be tested: 
> 1. If any inputs are None, the result should be None
> 2. An exception should be raised if the dimensions are not compatible for multiplication
> 3. Valid inputs (not None) with compatible dimensions should give the correct result
>
> After implementing tests that check these requirements, 100% branch coverage was achieved. The tests are implemented on the branch `sparse_mul` and can be found [here](https://github.com/will-berg/assignment3/tree/sparse_mul). 

> Manual branch coverage for `pattern_match` is implemented on the [pattern_match_improved_coverage](https://github.com/keon/algorithms/compare/master...will-berg:assignment3:pattern_match_improved_coverage) branch, and the DIY in [pattern_match_diy](https://github.com/keon/algorithms/compare/master...will-berg:assignment3:pattern_match_diy) branch.
> The branch coverage of the unit tests for the `pattern_match` raised from 90% to 100% with the two added test cases using the `coverage.py` tool, but from ~85% to 100% using manual tools. This could be that I counted more places as branches than the `coverage.py` tool and therefore set out more flags than neccesary.

>Manual branch coverage for `maze_search` is implemented on the [/feature/coverage-maze-search](https://github.com/will-berg/assignment3/commits/feature/coverage-maze-search) and the improve coverage is implemented on [/feature/improve-coverage-maze-search](https://github.com/will-berg/assignment3/commits/feature/improve-coverage-maze-search). The branch coverage for went up from 0.9 to 1.0.

>Manual branch coverage for `summarize_range` is implemented on the [/feature/coverage-maze-search](https://github.com/will-berg/assignment3/commits/feature/coverage-maze-search) branch, and the DIY in [/feature/improve-coverage-maze-search](https://github.com/will-berg/assignment3/commits/feature/improve-coverage-maze-search) branch. The coverage went up from 0.75 to 1.0

>Manual branch coverage for `intersection` is implemented on the [intersection-diy](https://github.com/will-berg/assignment3/tree/intersection-diy) and improve coverage is implemented on [intersection-coverage](https://github.com/will-berg/assignment3/tree/intersection-coverage). The branch coverage went up from 0.7 to 1.0 before implementing else-statements for each if-statement. After it implementing else-statements the manual branch coverage was ~0.93.

>Manual branch coverage tool for `solve_chinese_remainder` is implemented on branch [issue#9](https://github.com/will-berg/assignment3/tree/issue%239) and the two tests that increases the coverage to 100% on the branch [issue#10](https://github.com/will-berg/assignment3/tree/issue%2310).


1. What is the quality of your own coverage measurement? Does it take into account ternary operators (condition ? yes : no) and exceptions, if available in your language?

> It does not take ternary operators into account (none were encountered in the code). Exceptions are taken into account when they are manually raised. 

2. What are the limitations of your tool? How would the instrumentation change if you modify the program?

> If the algorithms are modified the DIY flag-system will no longer function as intended. This is a limitation of the tool. It can also not really deal with list comprehensions, as there is no way to set the flag upon entering the loop without "unrolling" it. 

3. If you have an automated tool, are your results consistent with the ones produced by existing tool(s)?

> The automated tool we used was *coverage* which can be installed with pip install. If you don’t take into account the `if __name__ == “__main__”:` statement the results are consistent (given that results from multiple tests are taken into consideration).

## 4. Refactoring

### count_islands
> The easiest way to reduce the complexity of many of these complex functions is by simply splitting them up into multiple functions that do simple things. For example, in the `count_islands` function, everything is done inside that one function (it calls no helper function). An easy way to reduce the complexity of `count_islands` could thus be to create some function(s) that help in determining whether something is an island or not. This would definitely lower the cyclomatic complexity of the function, but it also means that we are creating a helper function and only calling it once, which might be considered bad practice by some.

### maximum_flow_bfs.py
> It would be possible to split up maximum_flow_bfs.py into smaller help functions in order to reduce CCN. For example, you could place the *# finding the minimum flow* into a help function.

### pattern_match.py
> You could move out the first two if statements that checks for easy solutions (where the pattern it is looking for is none and the string is either none or not). The rest is a for loop which is reductive

### solve_chinese_remainder.py
> The high complexity in this function mainly comes from a lot of error checking done before the main algorithm is ran. The main algorithm itself is fairly short and difficult to decompose into smaller functions. Hence the easiest way to reduce the complexity is to seperate the error checking into its own function that runs first. This will reduce the cyclomatic complexity from 10 down to 5.

### maze_search.py
> The entire feature is implemented in one function with two loops and multiple if statements which leads to a high complexity. The loop for inside the while loops could be implemented as a separate function instead. This would lower the complexity and adhere more to the single responsibility coding paradigm. The same could be done for the setup. The main drawback with this is that all these functions need to share the same data structure(a queue) that will be passed around between the functions. Since Python arguments are passed by reference rather than value the price for this is very low.

## Self-assessment: Way of working
Current state according to the Essence standard: 
>We think we are in the `In place` category. Since we just switched groups, we did have different preferences in how we should communicate. But we did quickly agree on what we wanted to use, and we have also switched out things when we didn't think something was working for us which we had previously agreed upon. 

>[Link to Essence document](https://docs.google.com/document/d/1ocaGm4cGDml2fPU-MAHiebSv8pOMbU-RqiVDseqZJ3w/edit?usp=sharing).

Where is potential for improvement?
> Creating a modular coverage tool that can calculate coverage when the progam changes.

## Overall experience
What are your main take-aways from this project? What did you learn?

>Creating tests that have good coverage and using built in tools to check coverage.

>Spliting functions in help functions in order to lower CCN.

>Forking and working with open source projects.

Is there something special you want to mention here?

## Statement of Contributions
> Oscar Bergström: `maximum_flow_bfs` until DIY & `intersection` DIY and coverage tests (2 tests and DIY). Not going for P+.

> William Berg: `count_islands` DIY and coverage improvement for `sparse_mul.multiply` (2 tests). Not going for P+.  

> Michael Ask: `solve_chinese_remainder` DIY, coverage improvement and complexity reduction refractoring in the file algorithms/maths/chinese_remainder_thereom.py. Added two tests for complete branch coverage and refractored the function from a cyclomatic complexity of 10 down to 5. Going for P+.

> Hanna Bjarre: DIY and coverage improvement for `pattern_match` (2 tests). Not going for P+.

> Gustav Kasche: DIY and coverage improvement for  `maze_search` and coverage improvement for `summarize_ranges` (2 tests in total). Not going for P+.
