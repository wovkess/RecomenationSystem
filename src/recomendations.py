from math import sqrt
critics = {
    'Lisa Rose': {
        'Lady of the water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just my luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Wight Listener': 3.0
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0,
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5,
    },
    'Person1': {
        'Snakes on a Plane': 4.5,
        'You, Me and Dupree': 1.0,
        'Superman Returns': 4.0
    }
}


def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0:
        return 0

    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                         for item in prefs[person1] if item in prefs[person2]])
    return 1 / (1 + sqrt(sum_of_squares))


def sim_person(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

        if len(si) == 0:
            return 0

        sum1 = sum([prefs[person1][item] for item in si])
        sum2 = sum([prefs[person2][item] for item in si])

        sum1_sq = sum([pow(prefs[person1][item], 2) for item in si])
        sum2_sq = sum([pow(prefs[person2][item], 2) for item in si])

        p_sum = sum([prefs[person1][item]*prefs[person2][item] for item in si])

        num = p_sum - (sum1 * sum2/len(si))
        den = sqrt((sum1_sq - pow(sum1, 2)/len(si)) *
                   (sum2_sq - pow(sum2, 2) / len(si)))

        if den == 0:
            return 0

        return num/den


if __name__ == '__main__':
    print(sim_distance(critics, "Person1", "Lisa Rose"))
    print(sim_person(critics, "Person1", "Lisa Rose"))