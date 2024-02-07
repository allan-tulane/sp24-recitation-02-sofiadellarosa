# CMPS 2200  Recitation 02

**Name (Team Member 1):**Sofia Della Rosa
**Name (Team Member 2):**Jaimie Morris

IMPORTANT: 
**Tabulate does not work on this replit, but it is installed and works on my partners. That is the replit we worked on together, I copied work onto this repo. **

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$. # done sofia

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones. # done sofia 

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases. # done sofia 

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**TODO: your answer goes here** --> need to add answer
- if f(n) == 1, W(n) is O(n)
- if f(n) == log n, W(n) is log(n) * log(n)
- if f(n) == n, W(n) is O(nlogn)

When n is 200
- if f(n) == 1, W(n) is 255
- if f(n) == log n, W(n) is 351.3137522458472
- if f(n) == n, W(n) is 1504
  
assuming a = 1 and b = 2 
| n  | 1 | log(n) | n  |
|----|---|--------|----|
| 5  | 3 | 3.30   | 8  |
|10  | 4 | 5.61   | 18 |
|20  | 5 | 8.60   | 38 |
|50  | 6 | 13.51  | 97 |
|100 | 7 | 18.11  | 197|
|500 | 9 | 30.88  | 994|
|1000|10 | 37.79  |1994|


- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

**TODO: your answer goes here**
|     n |       W_1 |           W_2 |
|-------|-----------|---------------|
|    10 |       126 |          1692 |
|    20 |       524 |         14768 |
|    50 |      2518 |        236908 |
|   100 |     10172 |       1947632 |
|  1000 |    697496 |    1987993280 |
|  5000 |  34237688 |  249711292352 |
| 10000 | 136960752 | 1998845169408 |

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**TODO: your answer goes here**
|     n |   W_1 |           W_2 |
|-------|-------|---------------|
|    10 |    18 |          1134 |
|    20 |    38 |          9134 |
|    50 |    97 |        142597 |
|   100 |   197 |       1142597 |
|  1000 |  1994 |    1142849990 |
|  5000 |  9995 |  142856974901 |
| 10000 | 19995 | 1142856974901 |
