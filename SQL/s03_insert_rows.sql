# 전체 데이터 조회
SELECT * FROM prj_db.info_port;

# 1)
INSERT INTO `prj_db`.`info_port` (`id`,  `camera_no`, `situation_type`, `date`, `time`, `link_storage`)
VALUES (NULL, 10, 'FIRE', '2023-05-09', '15:03:02', 'https://naver.com');
# 2)
INSERT INTO `prj_db`.`info_port` 
VALUES (NULL, 4, 'NORMAL', '2023-05-09', '15:09:32', 'https://www.google.com/');
# 3)
INSERT INTO `prj_db`.`info_port` 
VALUES (NULL, 4, 'INVASION', '2023-05-09', '15:10:57', 'https://www.skuniv.ac.kr/notice');
# 4)
INSERT INTO `prj_db`.`info_port` 
VALUES (NULL, 2, 'FALL', '2023-05-12', '08:30:12', 'https://github.com/');
# 5)
INSERT INTO `prj_db`.`info_port` 
VALUES (NULL, 7, 'TRAFFIC', '2023-05-13', '12:30:12', 'https://learn.smau.or.kr/');
