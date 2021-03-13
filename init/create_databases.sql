# create databases
CREATE DATABASE IF NOT EXISTS `atendimento-agendamento-db`;
CREATE DATABASE IF NOT EXISTS `atendimento-agendamento-test-db`;

# create root user and grant rights
CREATE USER 'root'@'root' IDENTIFIED BY 'root';
GRANT ALL ON *.* TO 'root'@'%';