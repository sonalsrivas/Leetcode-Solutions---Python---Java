# Write your MySQL query statement below
SELECT name as employee
FROM Employee as E
WHERE salary > (SELECT salary FROM Employee as M WHERE E.managerId = M.id );