from math import sqrt
import numpy
# critics dictionary
critics = {
    'Lisa Rose': {
        'Lady in the water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0
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
    'Vova': {
        'Snakes on a Plane': 4.5,
        'You, Me and Dupree': 1.0,
        'Superman Returns': 4.0
    }
}

# Evklid distance


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


# koeff korr Pirsona


def sim_pearson(prefs, person1, person2):
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

# top films


def top_matches(prefs, person, n=5, simularity=sim_pearson):
    scores = [(simularity(prefs, person, other), other)
              for other in prefs if other != person]

    scores.sort()
    scores.reverse()
    return scores[0:n]

# top recommendations


def get_rec(prefs, person, simularity=sim_pearson):
    totals = {}
    sim_sums = {}
    for other in prefs:
        if other == person:
            continue
        sim = simularity(prefs, person, other)
        if sim <= 0:
            continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim

                sim_sums.setdefault(item, 0)
                sim_sums[item] += sim
    rank = [(total/sim_sums[item], item) for item, total in totals.items()]

    rank.sort()
    rank.reverse()
    return rank


if __name__ == "__main__":
    print(get_rec(critics, "Vova"))
