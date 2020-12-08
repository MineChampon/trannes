CREATE DATABASE IF NOT EXISTS trannes CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER IF NOT EXISTS 'minecha'@'%' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON trannes.* TO 'minecha'@'%';

create table users(
user_id varchar(32) primary key not null,
password varchar(255) not null)
charset=utf8mb4;

create table user_details(
user_id varchar(32) primary key, 
user_name varchar(32) not null, 
mail_address varchar(255) not null, 
gender varchar(8) not null,
birthday date not null,
created_at timestamp not null default current_timestamp,
updated_at timestamp not null default current_timestamp on update current_timestamp)
charset=utf8mb4;

create table books(
isbn_id varchar(13) primary key,
book_title varchar(255) not null,
book_author varchar(255) not null,
book_detail varchar(1000) not null,
created_at timestamp not null default current_timestamp,
updated_at timestamp not null default current_timestamp on update current_timestamp)
charset=utf8mb4;

create table book_genres(
isbn_id varchar(13) not null,
book_genre varchar(255) not null,
created_at timestamp not null default current_timestamp)
charset=utf8mb4;

create table user_books(
user_id varchar(32) not null,
isbn_id varchar(13) not null,
created_at timestamp not null default current_timestamp)
charset=utf8mb4;

create table user_lists(
list_id int(8) primary key auto_increment,
list_name varchar(32) not null,
user_id varchar(32) not null,
created_at timestamp not null default current_timestamp,
updated_at timestamp not null default current_timestamp on update current_timestamp)
charset=utf8mb4;

create table users_list_books(
list_id int(8) not null,
isbn_id varchar(13) not null,
created_at timestamp not null default current_timestamp)
charset=utf8mb4;

create table search_history(
user_id varchar(32) not null,
search_word varchar(255) not null,
created_at timestamp not null default current_timestamp)
charset=utf8mb4;


FLUSH PRIVILEGES;