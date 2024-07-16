-- settings.sql
CREATE DATABASE hackathon_db;
CREATE USER hackathon_user WITH PASSWORD 'hackathon_password';
GRANT ALL PRIVILEGES ON DATABASE hackathon_db TO hackathon_user;
ALTER DATABASE hackathon_db OWNER TO hackathon_user;