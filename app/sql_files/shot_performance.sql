select
    url,
    gametype,
    "date",
    --shottype,
    shooter,
    sum(case when shottype like '%2-pt%' and shotoutcome='make' then 1 else 0 end) as "two_point_shots_made",
    sum(case when shottype like '%2-pt%' then 1 else 0 end) as "two_point_shots",
    sum(case when shottype like '%3-pt%' and shotoutcome='make' then 1 else 0 end) as "three_point_shots_made",
    sum(case when shottype like '%3-pt%' then 1 else 0 end) as "three_point_shots",
    sum(case when shotoutcome ='make' then 1 else 0 end) as "total_makes",
    count(*) as total_shots
--shotoutcome
from public.pbp
--where shooter = 'A. Baynes - baynear01'
group by 1,2,3,4