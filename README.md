# Basics of Py-Numpy

--------------------
✅ NUMPY PRACTICE QUESTIONS (DS / ML LEVEL)
🟢 LEVEL 1 — Fundamentals (Warm-up, no excuses)
1. What problem does NumPy solve that Python lists cannot? (Answer in terms of memory + speed, not opinion.)
2. Given:arr = np.array([[1, 2, 3], [4, 5, 6]])What is arr.shape?What is arr.ndim?What does arr.dtype tell you?
3. Convert a Python list of floats into a NumPy array of integers without using a loop.
4. Why is this slow for large data?result = [] for i in arr: result.append(i * 2)
--------------------
🟢 LEVEL 2 — Array Creation & Shape Control
5. Create a NumPy array of shape (5, 3) filled with value 7.
6. Create an array of 10 equally spaced values between 0 and 1.
7. Create a 2D random array with:4 rows2 columnsvalues between 10 and 50
8. What is the difference between:np.arange(0, 10, 2) np.linspace(0, 10, 5)
--------------------
🟡 LEVEL 3 — Indexing, Slicing, Axis (CORE)
Given:
data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
9. Extract:the second rowthe third columnthe sub-matrix:[[20, 30], [50, 60]]
10. What is the difference between:
data[1] data[:, 1]
11. Without running code: What does this return?
np.sum(data, axis=0) np.sum(data, axis=1)
Explain why, not just values.
--------------------
🟡 LEVEL 4 — Boolean Masking (MOST IMPORTANT)
12. From data, extract all values greater than 40.
13. Replace all values less than 30 with 0 (in one line).
14. Extract values between 20 and 80 (exclusive).
15. Why is this wrong?
data[data > 20 and data < 80]
Fix it.
--------------------
🟠 LEVEL 5 — Broadcasting & Vectorization
16. Given:
prices = np.array([100, 200, 300]) discount = 10
Calculate final prices without loops.
17. Given a (4, 3) feature matrix, subtract the mean of each column.
18. Explain why this works:
arr + 5
But this fails:
arr + [1, 2]
(Answer using broadcasting rules.)
--------------------
🟠 LEVEL 6 — Reshape, Combine, Sort
19. Convert a 1D array of size 12 into a (3, 4) matrix.
20. Difference between:
flatten() ravel()
When does it matter?
21. Stack two arrays:
• one of shape (3, 2)
• one of shape (3, 2) vertically.
22. Sort a 2D array:
• column-wise
• row-wise
Explain which axis you used and why.
--------------------
🔴 LEVEL 7 — CSV-STYLE REAL DATA PRACTICE (CRITICAL)
📄 Assume this CSV file (students.csv)
id,math,science,english 1,78,85,90 2,45,60,50 3,90,88,95 4,32,40,35 5,85,92,88
Load it into NumPy (skip Pandas)
23. Load only numeric columns into a NumPy array.
24. Find:
• average score per subject
• average score per student
25. Identify students who scored below 40 in any subject.
26. Increase all scores by 5 marks, but cap maximum at 100.
27. Normalize each subject column (mean = 0, std = 1).
28. Find the top scorer per subject and return their row index.
--------------------
🔴 LEVEL 8 — Thinking Like an ML Engineer
29. Why does NumPy prefer vectorized operations over loops?
30. What happens if you mix int and float in the same array?
31. Why can wrong axis usage silently break ML models?
32. When would you prefer NumPy over Pandas in a pipeline?
--------------------
📌 RULES FOR PRACTICE (IMPORTANT)
• ❌ No loops unless explicitly required
• ❌ No Pandas
• ✅ Use vectorization
• ✅ Explain axis every time you use it
--------------------
