/*1*/
select * 
from chat
limit 15;

select * 
from stream
limit 15;

/*2*/
select game, count(distinct game)
from stream
group by game;

/*3*/
select channel, count(distinct channel)
from stream
group by channel;

/*4*/
SELECT game, COUNT(*)
FROM stream
GROUP BY game
ORDER BY COUNT(*) DESC;

/*5*/
SELECT country, COUNT(*)
FROM stream
GROUP BY country
having game = "League of Legends"
ORDER BY COUNT(*) DESC;

/*6*/
SELECT player, COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

/*7*/
SELECT game,
 CASE
  WHEN game = 'Dota 2'
      THEN 'MOBA'
  WHEN game = 'League of Legends' 
      THEN 'MOBA'
  WHEN game = 'Heroes of the Storm'
      THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive'
      THEN 'FPS'
    WHEN game = 'DayZ'
      THEN 'Survival'
    WHEN game = 'ARK: Survival Evolved'
      THEN 'Survival'
  ELSE 'Other'
  END AS 'genre',
  COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC;

/*8 y 9*/
SELECT time,
   strftime('%S', time)
FROM stream
GROUP BY 1
LIMIT 20;

/*10*/
SELECT strftime('%H', time),
   COUNT(*)
FROM stream
GROUP BY 1;

/*11*/
SELECT *
FROM stream
JOIN chat
  ON stream.device_id = chat.device_id;


