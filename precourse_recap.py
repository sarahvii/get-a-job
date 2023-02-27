current_week = 1
current_day_of_week = 1
total_course_weeks = 16
total_course_days_per_week = 5

def weeks_to_go():
    weeks_left = total_course_weeks - current_week
    days_left = total_course_days_per_week - current_day_of_week
    print(f"Only {weeks_left} weeks and {days_left} days to go!")

def get_a_job():
    print("ALMOST TIME TO GET A JOB!")

weeks_to_go()
get_a_job()
