-- table: program_type
-- purpose: This is a lookup table used for the program categories.

CREATE TABLE program_type (
    program_type_id INT IDENTITY(1,1) PRIMARY KEY,
    program_type_name VARCHAR(100) NOT NULL,
    description VARCHAR(255)
);

-- table: programs
-- purpose: Stores all programs offered by the organization.

CREATE TABLE programs (
    program_id INT IDENTITY(1,1) PRIMARY KEY,
    [program_name] VARCHAR(150) NOT NULL,
    program_type_id INT NOT NULL,
    description VARCHAR(255),
    age_group VARCHAR(50),
    is_active BIT NOT NULL DEFAULT 1,

    CONSTRAINT FK_Programs_ProgramType
        FOREIGN KEY (program_type_id) REFERENCES program_type(program_type_id)
);

-- table: members
-- purpose: Represents youth participants.

CREATE TABLE members (
    member_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birth_date DATE,
    gender VARCHAR(20),
    neighborhood VARCHAR(100),
    enrollment_date DATE NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'Active',
    notes VARCHAR(255)
);

-- table: staff
-- purpose: Stores information about staff and volunteers who support program delivery.

CREATE TABLE staff (
    staff_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    staff_type VARCHAR(50) NOT NULL,   -- Volunteer, PaidStaff, Intern
    role VARCHAR(100),                -- Coach, Tutor, Mentor, etc.
    start_date DATE NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(150),
    is_active BIT NOT NULL DEFAULT 1
);

-- table: program_session
-- purpose: Represents individual scheduled sessions of a program.

CREATE TABLE program_session (
    program_session_id INT IDENTITY(1,1) PRIMARY KEY,
    program_id INT NOT NULL,
    session_date DATE NOT NULL,
    start_time TIME,
    end_time TIME,
    location VARCHAR(150),
    notes VARCHAR(255),

    CONSTRAINT FK_ProgramSession_Programs
        FOREIGN KEY (program_id) REFERENCES programs(program_id)
);

-- table: staff_session
-- purpose: Junction table linking Staff to ProgramSession.

CREATE TABLE staff_session (
    staff_session_id INT IDENTITY(1,1) PRIMARY KEY,
    staff_id INT NOT NULL,
    program_session_id INT NOT NULL,
    hours_worked DECIMAL(4,2),
    role_in_session VARCHAR(100),
    notes VARCHAR(255),

    CONSTRAINT FK_StaffSession_Staff
        FOREIGN KEY (staff_id) REFERENCES Staff(staff_id),

    CONSTRAINT FK_StaffSession_ProgramSession
        FOREIGN KEY (program_session_id) REFERENCES program_session(program_session_id)
);

-- table: attendance
-- purpose: Records attendance for each Member at each program_session.

CREATE TABLE attendance (
    attendance_id INT IDENTITY(1,1) PRIMARY KEY,
    member_id INT NOT NULL,
    program_session_id INT NOT NULL,
    attendance_status VARCHAR(50) NOT NULL,  -- Present, Absent, Late, Excused
    check_in_time TIME,
    check_out_time TIME,
    recorded_by_staff_id INT,
    notes VARCHAR(255),

    CONSTRAINT FK_Attendance_Members
        FOREIGN KEY (member_id) REFERENCES Members(member_id),

    CONSTRAINT FK_Attendance_ProgramSession
        FOREIGN KEY (program_session_id) REFERENCES program_session(program_session_id),

    CONSTRAINT FK_Attendance_Staff
        FOREIGN KEY (recorded_by_staff_id) REFERENCES Staff(staff_id)
);

