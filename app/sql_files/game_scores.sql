select
    url,
    gametype,
    "date",
    hometeam,
    awayteam,
    max(awayscore) as awayscore,
    max(homescore) as homescore
from public.pbp
group by 1,2,3,4,5