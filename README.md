# Using Plain Text Files (`.txt`)

A diagnostic computer has collected rows of numerical data. Each line of the input file represents one set of readings.

Your job is to create an algorithm that reads the file one line at a time, processes the numbers on that line, and produces a diagnostic checksum. This follows the lesson's read-process-write cycle: read data from a file, process it in Python, and then write the results to a file.

### The Algorithm

For each line of the input file:

1. Remove the newline or unnecessary whitespace.
2. Separate the numbers using the spaces between them.
3. Convert the values from strings into integers.
4. Find the largest number on the line.
5. Find the smallest number on the line.
6. Subtract the smallest number from the largest number. This is the **difference** for that line.
7. Add the difference to a running **checksum**.
8. Write the difference for that line to `checksum_results.txt`.

After every line has been processed, write the final checksum as the last line of `checksum_results.txt`.

### Sample Input

Save the following as `checksum_sample.txt`:

```text
12 7 19 4
8 8 3 14
21 13 17 9
6 2 10 5
```

For the first line:

```text
12 7 19 4
```

The largest value is `19` and the smallest is `4`.

```text
19 - 4 = 15
```

The four line differences are:

```text

12  7 19  4 | Checksum = 15
 8  8  3 14 | Checksum = 11
21 13 17  9 | Checksum = 12
 6  2 10  5 | Checksum = 8
```

The final checksum is:

```text
15 + 11 + 12 + 8 = 46
```

Therefore, `checksum_results.txt` should contain:

```text
15
11
12
8
Checksum: 46
```

### Full Challenge Input

Once your algorithm works correctly with the sample, use the input from `checksum_input.txt` as your full input. You might notice that your real input is a little longer and uses bigger numbers. If your algorithm does not work for the sample or uses only hardcoded numbers for the loops, it is unlikely you will be able to complete the full input.

### Required File Structure

```text
diagnostic_checksum/
│
├── main.py
├── checksum_practice_input.txt
├── checksum_input.txt
└── checksum_results.txt
```

`checksum_results.txt` should be created or overwritten by the program when it runs.

## Using Plain Text Files (`.txt`) — 20 Marks

| Assessment Item | Criteria | Marks |
|---|---|---:|
| ☐ Reading the Input File | Opens the provided input file in read mode and processes its contents one line at a time. | 2 |
| ☐ Processing Each Line | Removes unnecessary whitespace, separates the values on each line, and converts each value from a string into an integer. | 4 |
| ☐ Calculating Line Differences | Correctly identifies the largest and smallest value on every line and calculates the difference between them. | 4 |
| ☐ Calculating the Checksum | Maintains a running total of all line differences and produces the correct final checksum. | 3 |
| ☐ Writing Line Results | Creates or overwrites `checksum_results.txt` and writes each calculated line difference on its own line. | 3 |
| ☐ Writing the Final Result | Writes the final checksum to the end of `checksum_results.txt` in the required format. | 2 |
| ☐ Sample Verification | When run using `checksum_sample.txt`, produces the four expected differences and a checksum of `46`. | 1 |
| ☐ File Structure | Uses the required `main.py`, input `.txt` file, and `checksum_results.txt` file structure. | 1 |
|  | **Total** | **20** |