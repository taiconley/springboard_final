SELECT
    url,
    gametype,
    "date",
    hometeam,
    awayteam,
    shooterregex as player,
    case when shooterregex = homeplayer then hometeam
     when shooterregex = awayplayer then awayteam
     end as team
FROM public.game_rosters_1
group by 1,2,3,4,5,6,7