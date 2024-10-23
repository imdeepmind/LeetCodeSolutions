-- Write your PostgreSQL query statement below

SELECT B.student_id, B.student_name, B.subject_name, COALESCE(E.attended_exams, 0) AS attended_exams FROM (
    SELECT * FROM Students S, Subjects Sb
) B
LEFT JOIN (
    SELECT E.student_id, E.subject_name, COUNT(*) as attended_exams
    FROM Examinations E
    GROUP BY E.student_id, E.subject_name
) E
ON E.student_id = B.student_id AND E.subject_name = B.subject_name 
ORDER BY B.student_id, B.subject_name
