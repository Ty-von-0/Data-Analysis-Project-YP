--This file contains SQL commands to alter the database schema based on the changes made to the data generation scripts and the new requirements for the database structure.

--program_type
ALTER TABLE program_type
DROP COLUMN description;

--programs
ALTER TABLE programs
DROP COLUMN description;

ALTER TABLE programs
DROP COLUMN age_group;

-- members 
ALTER TABLE members
DROP COLUMN birth_date;

ALTER TABLE members
DROP COLUMN neighborhood;

ALTER TABLE members
DROP COLUMN notes;

ALTER TABLE members
DROP COLUMN enrollment_date;

ALTER TABLE members
ADD age INT;

ALTER TABLE members
ADD join_date DATE;

--staff
ALTER TABLE staff DROP COLUMN staff_type;

ALTER TABLE staff DROP COLUMN phone;

ALTER TABLE staff DROP COLUMN email;

ALTER TABLE staff DROP COLUMN is_active;

--drop constraint for is_active
ALTER TABLE staff
DROP CONSTRAINT DF__staff__is_active__3F466844;

-- now ALTER TABLE staff DROP COLUMN is_active; can be ran succesfully
ALTER TABLE staff ADD status VARCHAR(50);

--program_session
ALTER TABLE program_session
DROP COLUMN location;

ALTER TABLE program_session
DROP COLUMN notes;

--staff_session
ALTER TABLE staff_session
DROP COLUMN hours_worked;

ALTER TABLE staff_session
DROP COLUMN notes;

--attendance
ALTER TABLE attendance
DROP COLUMN check_out_time;

ALTER TABLE attendance
DROP COLUMN recorded_by_staff_id;

ALTER TABLE attendance
DROP CONSTRAINT FK_Attendance_Staff;