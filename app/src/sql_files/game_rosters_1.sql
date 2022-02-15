select
    url,
    gametype,
    "date",
    hometeam,
    awayteam,
    homeplay,
    awayplay,
    shooter,
    regexp_match(shooter, '[A-Z]\. [A-Z][a-z]+') as shooterregex,
    regexp_match(homeplay, '[A-Z]\. [A-Z][a-z]+') as homeplayer,
    regexp_match(awayplay , '[A-Z]\. [A-Z][a-z]+') as awayplayer
from public.pbp