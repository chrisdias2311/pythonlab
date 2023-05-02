Shell script to convert temperature from centigrade to fahrenheit:
```
#!/bin/bash
echo "Enter temperature in degrees Centigrade: "
read temp_c
temp_f=$((($temp_c * 9/5) + 32))
echo "$temp_c degrees Centigrade is equal to $temp_f degrees Fahrenheit"


egrep script to list all the filenames starting from p in the specified directory:
```
#!/bin/bash
echo "Enter directory path: "
read dir_path
ls $dir_path | egrep "^p.*"
```

Shell script to display greatest among three numbers:
#!/bin/bash
echo "Enter three numbers: "
read a b c
if [ $a -gt $b ] && [ $a -gt $c ]
then
    echo "$a is the greatest number"
elif [ $b -gt $a ] && [ $b -gt $c ]
then
    echo "$b is the greatest number"
else
    echo "$c is the greatest number"
fi
```

Shell script to check whether entered year is a leap year or not:
 
```bash
#!/bin/bash
 
echo "Enter a year: "
read year
 
if [ $((year % 4)) -eq 0 ] && [ $((year % 100)) -ne 0 ] || [ $((year % 400)) -eq 0 ]; then
  echo "$year is a leap year"
else
  echo "$year is not a leap year"
fi
```

6. AWK script to replace the third occurrence of a pattern:
```
awk '/pattern/ && (++count == 3) { sub(/pattern/, "replacement"); }1'
```
This script will replace the third occurrence of "pattern" with "replacement" in a file. The script uses the `sub` function to replace the pattern and the `++count` operator to keep track of the number of occurrences. The `1` at the end is a shorthand for `{ print }` and tells AWK to print the modified file.
7. Sed script to replace the word 'director' by 'manager' in the third line of a file:
```
sed '3s/director/manager/' filename
```

Shell script to determine whether a person is a major or a minor:
#!/bin/bash
echo "Enter your age:"
read age
if [ $age -ge 18 ]
then
  echo "You are a major"
else
  echo "You are a minor"
fi
```
```
perl
#!/usr/bin/perl
sub is_prime {
    my $n = shift;
    for (2..int(sqrt($n))) {
        return 0 if $n % $_ == 0;
    }
    return 1;
}
 
for (my $i = 1; $i <= 50; $i++) {
    if (is_prime($i)) {
        print "$i ";
    }
}
```
Explanation:
- The `is_prime` subroutine takes a number `n` and returns `1` if it is a prime number, and `0` otherwise. It checks whether `n` is divisible by any number between `2` and the square root of `n`.
- The main loop iterates from `1` to `50` and checks whether each number is prime using the `is_prime` subroutine. If a number is prime, it is printed to the console.

Here's an example shell script to check whether a number is divisible by 2 and 5: 
```bash
#!/bin/bash
 Echo “Enter a number”
read num
 
if (( num % 2 == 0 )) && (( num % 5 == 0 )); then
  echo "$num is divisible by 2 and 5."
else
  echo "$num is not divisible by 2 and 5."
fi
```
In this script, the user is prompted to enter a number, which is stored in the `num` variable. The script then checks whether `num` is divisible by 2 and 5 using the modulus operator (`%`). If it is, the script prints a message saying so; otherwise, it prints a different message.

Shell script to search whether the entered element is present in the list or not:
```
#!/bin/bash
# Define the list
list=(apple banana orange pear)
 
# Prompt the user to enter an element
read -p "Enter an element to search: " element
 
# Loop through the list and search for the element
for item in "${list[@]}"
do
    if [[ $item == $element ]]; then
        echo "Element found in the list."
        exit
    fi
done
 
# If the element is not found
echo "Element not found in the list."
```
 
In this script, we have defined a list of fruits and prompted the user to enter an element to search. Then, we have looped through the list and compared each element with the entered element. If the element is found in the list, the script prints "Element found in the list." and terminates. If the element is not found in the list, the script prints "Element not found in the list."


#!/bin/bash
 
if [ $# -eq 0 ]; then
    echo "Please provide a file name."
    exit 1
fi
 
filename=$1
if [ ! -f "$filename" ]; then
    echo "File not found: $filename"
    exit 1
fi
 
char_count=$(wc -c < "$filename")
word_count=$(wc -w < "$filename")
line_count=$(wc -l < "$filename")
 
echo "Character count: $char_count"
echo "Word count: $word_count"
echo "Line count: $line_count"







```bash
#!/bin/bash
 
read -p "Enter a value: " value
 
# Check if the entered value is a number
if [[ "$value" =~ ^[0-9]+$ ]]; then
    echo "The entered value is a number."
else
    echo "The entered value is an alphabet."
fi
```
This script accepts a value from the user and checks if it is a number or an alphabet using a regular expression. If the entered value contains only digits, it is considered a number, and if it contains any non-digit characters, it is considered an alphabet.

#!/bin/bash
 
echo "Enter a number: "
read num
 
echo "Multiplication table of $num: "
 
for i in {1..10}
do
  echo "$num x $i = $((num*i))"
done
```
 
Example:
 
```
$ ./multiplication_table.sh
Enter a number:
5
Multiplication table of 5:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```
To generate the fibonacci series in a shell script, you can use the following code:
 
```





#!/bin/bash
 
echo "Enter the number of terms in the Fibonacci series: "
read n
 
a=0
b=1
 
echo "The Fibonacci series is: "
 
for ((i=0; i<n; i++))
do
  echo -n "$a "
  fn=$((a + b))
  a=$b
  b=$fn
done
 
echo ""
```

sum=0
echo "Enter 10 numbers:"
for ((i=1; i<=10; i++))
do
  read num
  sum=$((sum+num))

Shell script to compute nth power of a number:
 
```
#!/bin/bash
 
echo "Enter a number:"
read num
 
echo "Enter the power:"
read pow
 
result=1
for ((i=1; i<=pow; i++))
do
    result=$((result * num))
done
 
echo "$num raised to the power of $pow is $result"
```

done
echo "The sum of entered numbers is: $sum"
``` 
In this script, we have used a for loop to read 10 numbers from the user and calculate their sum using a variable called `sum`. Finally, we have printed the sum using `echo`.


Here's a shell script to compute the factorial of a number:
 
```bash
#!/bin/bash
 
echo "Enter a number: "
read num
 
fact=1
 
for((i=1;i<=$num;i++))
do
  fact=$((fact*i))
done
 
echo "Factorial of $num is $fact"












