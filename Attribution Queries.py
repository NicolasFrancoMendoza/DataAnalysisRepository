/*1*/
select utm_source, count(*)
from page_visits
group by utm_source;

select utm_campaign, count(*)
from page_visits
group by utm_campaign;
/*2*/
select distinct page_name
from page_visits;

/*3 first touch*/
WITH first_touch AS (
    SELECT user_id,
        MIN(timestamp) as first_touch_at
    FROM page_visits
    GROUP BY user_id)
SELECT
    pv.utm_source,
		pv.utm_campaign,
    count(ft.first_touch_at)
FROM first_touch ft
JOIN page_visits pv
    ON ft.user_id = pv.user_id
    AND ft.first_touch_at = pv.timestamp
group by utm_campaign;

/*4 last touch*/
WITH first_touch AS (
    SELECT user_id,
        MAX(timestamp) as first_touch_at
    FROM page_visits
    GROUP BY user_id)
SELECT 
    pv.utm_source,
		pv.utm_campaign,
    count(ft.first_touch_at)
FROM first_touch ft
JOIN page_visits pv
    ON ft.user_id = pv.user_id
    AND ft.first_touch_at = pv.timestamp
group by utm_campaign;

/*5*/
with dst_user_count as (
SELECT DISTINCT user_id
from page_visits
where page_name = "4 - purchase"
group by user_id)
select count(*)
from dst_user_count;

/*6. last touches that become in purchase*/
WITH first_touch AS (
    SELECT user_id,
        MAX(timestamp) as first_touch_at
    FROM page_visits
    GROUP BY user_id)
SELECT 
    pv.utm_source,
		pv.utm_campaign,
    count(ft.first_touch_at)
FROM first_touch ft
JOIN page_visits pv
    ON ft.user_id = pv.user_id
    AND ft.first_touch_at = pv.timestamp
    and pv.page_name = "4 - purchase"
group by utm_campaign;


