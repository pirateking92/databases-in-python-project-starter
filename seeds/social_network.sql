DROP TABLE IF EXISTS posts; --HAVE FOREIGN KEY TABLE FIRST
DROP TABLE IF EXISTS user_accounts;
DROP SEQUENCE IF EXISTS user_accounts_id_seq;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Create the table without the foreign key first.
CREATE TABLE user_accounts (
  id SERIAL PRIMARY KEY,
  email_address text,
  username text
);

-- Then the table with the foreign key second.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  views int,
-- The foreign key name is always {other_table_singular}_id
  user_account_id int,
  constraint fk_user_accounts foreign key(user_account_id) -- this one shouldnt be plural
    references user_accounts(id)
    on delete cascade
);

INSERT INTO user_accounts (email_address, username) VALUES('doyle9214@gmail.com', 'doyle9214');
INSERT INTO user_accounts (email_address, username) VALUES('test@gmail.com', 'test1234');

INSERT INTO posts (title, content, views, user_account_id) VALUES('Makers', 'Studying a lot', 123, 1);
INSERT INTO posts (title, content, views, user_account_id) VALUES('Test', 'Test to test', 54321, 1);