survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python","JavaScript","C#"],
    ["Python","Java"],
    ["Python","C++","JavaScript"],
]
survey_sets = [set(participants) for participants in survey_results] 

survey_intersection = set.intersection(*survey_sets)
print("All languages known by all participants:", survey_intersection)