from django.db import connection

def get_packed_orders():
    with connection.cursor() as cursor:
        cursor.execute("\
        	select user_name, date(wpt.input_post.ctime) as Working_Date, \
        	wpt.users_profile.name, count(distinct work_complete) as Num_of_Orders\
			from wpt.input_post \
			left join wpt.users_profile\
			on wpt.input_post.user_id = wpt.users_profile.id\
			where substr(task, 4, 7) = 'PACK001'\
			and wpt.input_post.ctime >= subdate(current_date, 7)\
			group by user_name, date(wpt.input_post.ctime);")
        row = cursor.fetchall()
    print(row)
    return row