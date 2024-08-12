-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN users_id INT)
BEGIN
  DECLARE weighted_sum FLOAT DEFAULT 0;
  DECLARE total_weight FLOAT DEFAULT 0;
  DECLARE avg_score FLOAT DEFAULT 0;

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
END$$
DELIMITER ;
