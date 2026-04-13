-- Constraints
ALTER TABLE programs
ADD CONSTRAINT FK_Programs_ProgramType
    FOREIGN KEY (program_type_id) REFERENCES program_type(program_type_id);

ALTER TABLE program_session
ADD CONSTRAINT FK_ProgramSession_Programs
    FOREIGN KEY (program_id) REFERENCES programs(program_id);

ALTER TABLE attendance
ADD CONSTRAINT FK_Attendance_Members
    FOREIGN KEY (member_id) REFERENCES members(member_id);

ALTER TABLE attendance
ADD CONSTRAINT FK_Attendance_ProgramSession
    FOREIGN KEY (program_session_id) REFERENCES program_session(program_session_id);

ALTER TABLE attendance
ADD CONSTRAINT FK_Attendance_Staff
    FOREIGN KEY (recorded_by_staff_id) REFERENCES staff(staff_id);

-- Indexes
CREATE INDEX IX_Programs_ProgramTypeID ON programs(program_type_id);
CREATE INDEX IX_ProgramSession_ProgramID ON program_session(program_id);
CREATE INDEX IX_Attendance_MemberID ON attendance(member_id);
CREATE INDEX IX_Attendance_ProgramSessionID ON attendance(program_session_id);
CREATE INDEX IX_StaffSession_StaffID ON staff_session(staff_id);
CREATE INDEX IX_StaffSession_ProgramSessionID ON staff_session(program_session_id);