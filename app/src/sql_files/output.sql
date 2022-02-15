SELECT
    ros.url,
    ros.gametype,
    ros."date",
    ros.hometeam,
    ros.awayteam,
    ros.player,
    ros.team,
    pgsp.two_point_shots_made,
    pgsp.two_point_shots,
    pgsp.three_point_shots_made,
    pgsp.three_point_shots,
    pgsp.total_makes,
    pgsp.total_shots,
    gr.defensive_rebounds,
    gr.offensive_rebounds,
    gs.homescore,
    gs.awayscore
FROM public.game_rosters_2 ros
    left join public.player_game_shot_performance pgsp
    on ros.url = pgsp.url
        and ros.player = pgsp.shooter
    left join game_rebounds gr
    on ros.url = gr.url
        and ros.player = gr.rebounder
    left join game_scores gs
    on ros.url = gs.url
order by url
;
