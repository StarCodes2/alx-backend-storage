-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
  DECLARE weighted_sum FLOAT DEFAULT 0;
  DECLARE total_weight FLOAT DEFAULT 0;
  DECLARE avg_score FLOAT DEFAULT 0;
  DECLARE users_id INT;
  DECLARE done INT DEFAULT 0;

  DECLARE user_cur CURSOR FOR
    SELECT id FROM users;

  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

  OPEN user_cur;

  user_loop: LOOP
    FETCH user_cur INTO users_id;
    IF done THEN
      LEAVE user_loop;
    END IF;

    SELECT SUM(score * weight), SUM(weight)
    INTO weighted_sum, total_weight
    FROM corrections
    JOIN projects
      ON corrections.project_id = projects.id
    WHERE corrections.user_id = users_id;

    IF total_weight > 0 THEN
      SET avg_score = weighted_sum / total_weight;
    ELSE
      SET avg_score = 0;
    END IF;

    UPDATE users
    SET average_score = avg_score
    WHERE id = users_id;
  END LOOP;

  CLOSE user_cur;
END$$
DELIMITER ;
