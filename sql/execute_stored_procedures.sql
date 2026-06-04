--staff 
--rename start_date -> hire_date
EXEC sp_rename 'staff.start_date', 'hire_date', 'COLUMN';

--program_session
--Execute store procedure to rename column program_session_id to session_id
EXEC sp_rename 'program_session.program_session_id', 'session_id', 'COLUMN';

--staff_session
--Execute store procedure to rename column program_session_id to session_id
EXEC sp_rename 'staff_session.program_session_id', 'session_id', 'COLUMN';
--Execute store procedure to rename column role_in_session to role_during_session
EXEC sp_rename 'staff_session.role_in_session', 'role_during_session', 'COLUMN';

--attendance
--Execute store procedure to rename column program_session_id to session_id
EXEC sp_rename 'attendance.program_session_id', 'session_id', 'COLUMN';
--Execute store procedure to rename column attendance_status to present
EXEC sp_rename 'attendance.attendance_status', 'present', 'COLUMN';