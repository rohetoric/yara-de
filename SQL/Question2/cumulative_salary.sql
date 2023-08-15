CREATE TABLE Employee (
    id int NOT NULL,
    month int NOT NULL,
    salary int,
    PRIMARY KEY (id, month));

INSERT INTO Employee(id,month,salary)
VALUES
(1,1,20),(2,1,20),(1,2,30),(2,2,30),(3,2,40),(1,3,40),(3,3,60),(1,4,60),(3,4,70),(1,7,90),(1,8,90);

SELECT emp1.Id id, emp1.month month, sum(emp2.salary) salary 
FROM Employee emp1 join Employee emp2 ON emp1.id = emp2.id AND (emp1.month=emp2.month OR emp1.month=emp2.month+1 OR emp1.month=emp2.month+2) AND emp1.month<(SELECT max(month) FROM Employee WHERE id=emp1.id) 
GROUP by 1,2 
ORDER BY 1,2 DESC;

