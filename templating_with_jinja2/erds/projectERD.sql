
        
CREATE TABLE post_likes
(
  id         INT       NOT NULL AUTO_INCREMENT,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NULL     DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  post_id    INT       NOT NULL,
  user_id    INT       NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE posts
(
  id         INT          NOT NULL AUTO_INCREMENT,
  created_at timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp    NULL     DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  content    VARCHAR(255) NULL    ,
  creator_id INT          NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE users
(
  id         INT          NOT NULL AUTO_INCREMENT,
  created_at timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp    NULL     DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  user_name  VARCHAR(255) NULL    ,
  email      VARCHAR(255) NULL    ,
  PRIMARY KEY (id)
);

ALTER TABLE posts
  ADD CONSTRAINT FK_users_TO_posts
    FOREIGN KEY (creator_id)
    REFERENCES users (id);

ALTER TABLE post_likes
  ADD CONSTRAINT FK_posts_TO_post_likes
    FOREIGN KEY (post_id)
    REFERENCES posts (id);

ALTER TABLE post_likes
  ADD CONSTRAINT FK_users_TO_post_likes
    FOREIGN KEY (user_id)
    REFERENCES users (id);

        
      