# your.harvard

## Problem to Solve

If you’re not already familiar, Harvard has a course shopping tool called my.harvard, with which students explore (and ultimately register for!) classes. To keep track of courses, students, and their registrations, my.harvard presumably uses some kind of underlying database. And yet, if you’ve ever used it, you’ll know that my.harvard isn’t especially… quick.

Here’s your chance to make my.harvard just a little bit faster! In this problem, take some Harvard course data and create indexes to speed up typical queries on the database. Keep in mind that indexing every column isn’t always the best solution: you’ll need to consider trade-offs in terms of space and time, ultimately representing Harvard’s courses and students in the most efficient way possible.

Within `harvard.db`, you’ll find five tables that implement the relationships described in the ER diagram above. Click the drop-downs below to learn more about the schema of each individual table.

### students table

The `students` table contains the following columns:

- `id`, which is the student’s ID.
- `name`, which is the student’s name.

### courses table

The `courses` table contains the following columns:

- `id`, which is the courses’s ID.
- `department`, which is the department in which the course is taught (e.g., “Computer Science”, “Economics”, “Philosophy”).
- `number`, which is the course number (e.g., 50, 12, 330).
- `semester`, which is the semester in which the class was taught (e.g., “Spring 2024”, “Fall 2023”).
- `title`, which is the title of the course (e.g., “Introduction to Computer Science”).

### enrollments table

The `enrollments` table contains the following columns:

- `id`, which is the ID to identify the enrollment.
- `student_id`, which is the ID of the student enrolled.
- `course_id`, which is the ID of the course in which the student is enrolled.

### requirements table

The `requirements` table contains the following columns:

- `id`, which is the ID of the requirement.
- `name`, which is the name of the requirement.

### satisfies table

The `satisfies` table contains the following columns:

- `id`, which is the ID of the course-requirement pair.
- `course_id`, which is the ID of a given course.
- `requirement_id`, which is the ID of the requirement which the given course satisfies.

## Specification

In `indexes.sql`, write a set of SQL statements that create indexes which will speed up typical queries on the `harvard.db` database. The number of indexes you create, as well as the columns they include, is entirely up to you. Be sure to balance speed with disk space, only creating indexes you need.

When engineers optimize a database, they often care about the typical queries run on the database. Such queries highlight patterns with which a database is accessed, thus revealing the best columns and tables on which to create indexes. Click the spoiler tags below to see the set of typical queries run on `harvard.db`.

### Typical SELECT queries on `harvard.db`

### Typical INSERT, UPDATE, and DELETE queries on `harvard.db`

## Advice

- Type `.timer on` or `.timer off` to turn SQLite’s built-in query timer on or off, respectively.
- Recall that creating an index on a column can ensure that SELECT queries which search that column run faster. At the same time, an index requires additional space.
- Recall that an index organizes data in such a way as to facilitate the search process. Yet, when new rows are added, updated, or deleted, the index needs to be re-arranged—resulting in some INSERT, UPDATE, and DELETE queries actually taking longer when an index exists!
- Recall that in SQLite you can execute

  ```sql
  EXPLAIN QUERY PLAN
  ...
  ```
  where `...` is a full SQL query. SQLite will reveal the process it intends to use to execute the given query. You’ll know that your query is using an index when EXPLAIN QUERY PLAN lists steps that includes “USING INDEX” or “USING COVERING INDEX.” Keep in mind that a query can involve multiple steps and, depending on which indexes you’ve created, some of those steps may use an index while others may not!
