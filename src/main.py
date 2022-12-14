from math import sqrt
from tkinter import *
import pprint


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


prefs = critics
person = 'Vova'


def result(prefs, person,  simularity=sim_pearson):
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
    a = int(input_value.get())
    temp = rank[:a]
    for i in temp:
        info["text"] = i
    return info


def main():
    print(result(prefs, person))


# GUI dev
root = Tk()
root['bg'] = '#3F6748'
root.title('Recommendation list')
root.geometry('700x700')
root.resizable(width=False, height=False)
root.iconphoto(False, PhotoImage(
    file='D:\Study\Python\RecomenationSystem\img\icon.png'))

frame_top = Frame(root, bg='#fafafa', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#3F6748', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

input_value = Entry(frame_top, bg="white", font=30)
input_value.pack()
btn = Button(frame_top, text='Show list', command=main)
btn.pack()

info = Label(frame_bottom, text='Recommendation information',
             bg='#3F6748', font=("Arial", 10))
info.pack()

root.mainloop()
