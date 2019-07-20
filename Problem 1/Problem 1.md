## Multiples of 3 and 5

### Problem

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

### Solution
The easy approach would be taking the summation of the $\sum_{i=1}^{999} t_i$ where $t=i|3 \vee i|5$

#### Sudo Code

    for integer i < 1000:
        if(i % 3 == 0 OR i % 5 == 0)
            sum += i

### The Internet Solution
In general, $a+(n-1)d=x$, gives $n=\Z((x-a)/d+1)$.

But for this problem we can improve even further, as $a=d$ we get $n=\Z(x/d-d/d+1)=\Z(x/d)$.

The nth (last) term, $l=a+(n-1)d=d+(\Z(x/d)-1)*d=d*\Z(x/d)$.

Combining this to find the sum, $S=(n/2)(a+l)=(\Z(x/d)/2)*(d+d*\Z(x/d))$.

Simplifying, $S=d*\Z(x/d)*(1+\Z(x/d))/2$.

As the problem asks for the sum of multiples of 3 and 5 we find the sum of each series, but as 3,6,9,... and 5,10,15,... have multiples of 15 in common, we need to subtract the series for 15,30,45,...

However, caution is needed. The problem states below then 1000, so we must use 999 in the formula (otherwise it would include 1000 in the sum, as a multiple of 5)

$T=3*\Z(999/3)*(1+\Z(999/3))/2 + 5*\Z(999/5)*(1+\Z(999/5))/2 - 15*\Z(999/15)*(1+\Z(999/15))/2$

Clever substitutions and manipulations you can simplify to:

$T=1.5*\Z((x-1)/3)*\Z((x+2)/3) + 2.5*\Z((x-1)/5)*\Z((x+4)/5) - 7.5*\Z((x-1)/15)*\Z((x+14)/15)$