# Database Schema Overview

## Tables
- program_type
- programs
- program_session
- members
- staff
- staff_session
- attendance

## Relationships
- program_type 1 → Many programs
- programs 1 → Many program_sessions
- program_session 1 → Many attendance
- members 1 → Many attendance
- staff 1 → Many staff_session
- program_session 1 → Many staff_session