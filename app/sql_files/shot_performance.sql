select
    url,
    gametype,
    "date",
    regexp_match(shooter, '[A-Z]\. [A-Z][a-z]+') as shooter,
    sum(case when shottype like '%%2-pt%%' and shotoutcome='make' then 1 else 0 end) as "two_point_shots_made",
    sum(case when shottype like '%%2-pt%%' then 1 else 0 end) as "two_point_shots",
    sum(case when shottype like '%%3-pt%%' and shotoutcome='make' then 1 else 0 end) as "three_point_shots_made",
    sum(case when shottype like '%%3-pt%%' then 1 else 0 end) as "three_point_shots",
    sum(case when shotoutcome ='make' then 1 else 0 end) as "total_makes",
    count(*) as total_shots
from public.pbp
group by 1,2,3,4
