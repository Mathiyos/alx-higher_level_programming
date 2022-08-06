-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT c.name AS genre, COUNT(*) AS number_of_shows
FROM tv_shows a
INNER JOIN tv_show_genres b
ON a.id = b.show_id
INNER JOIN tv_genres c
ON b.genre_id = c.id
GROUP BY c.name
ORDER BY 2 DESC
