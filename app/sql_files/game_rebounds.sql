select
    url,
    gametype,
    "date",
    regexp_match(rebounder, '[A-Z]\. [A-Z][a-z]+') as rebounder,
    sum(case when reboundtype ='defensive' then 1 else 0 end) as "defensive_rebounds",
    sum(case when reboundtype ='offensive' then 1 else 0 end) as "offensive_rebounds"
from public.pbp
where rebounder is not null
group by 1,2,3,4
