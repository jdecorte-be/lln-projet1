from LibrairieLectureFichierQCM import qcm
import sys
import random


# Chargement du questionnaire

questions = qcm.build_questionnaire(sys.argv[1])

random.shuffle(questions)


'''
    Systeme de cotation : 
    - Easy : correct : +2 incorrect : -1
'''

print("\033[0;36mWelcome to the best QCM Shuffle in the world.")
print("\033[0;36m================================================\033[0;35m")
print("\033[0;36mChoisissez votre difficultées :\n\t1)Facile\t2)Moyen\t\t3)Dur")
print("\033[0;36m================================================\033[0;35m")

while True :
    lvl = input("\033[0;36mEntrer votre difficultées : \u001b[37m")
    if (not lvl.isnumeric()) :
        print("\u001b[31mVotre reponse doit être un nombre!")
    elif not (1 <= int(lvl) and int(lvl) <= 3):
        print("\u001b[31mCette reponse existe pas! Entrer un index valide...")
    else :
        break


if(lvl == "1") :
    up_point = 2
    down_point = 1
elif(lvl == "2") :
    up_point = 1
    down_point = 1
elif(lvl == "3") :
    up_point = 1
    down_point = 2

point = len(questions) * up_point
q = 0
while q < len(questions):


    print("\t\033[0;36mQuestion " + str(q+1) + ": \"" + questions[q][0] + "\"\033[0;35m")
    for r in range(len(questions[q][1])):
        print("\t\t" + str(r+1) + ") " + questions[q][1][r][0])

    print("\u001b[37mINFO : Pour naviger entre les questions entrer prev ou next\033[0;36m")





    '''
        La while permet de demander a l'utilisateur ca reponse tout en
        sachant si elle a le format valide. C'est a dire
    
    '''
    while True :
        n = input("\033[0;36mEnter your answer : \u001b[37m")

        if (n != "prev" and n != "next" and not n.isnumeric()) :
            print("\u001b[31mVotre reponse doit être un nombre, prev ou next!")
        elif  (not (1 <= int(n) and int(n) <= len(questions[q][1]))):
            print("\u001b[31mCette reponse existe pas! Entrer un index valide...")
        else :
            break

    if(n == "next") :
        q += 1
        continue

    if(str(questions[q][1][int(n) - 1][1]) == "True") :
        print("\033[0;32mBravo ! Tu as bon !\033[0;35m")
    else :
        print("\033[0;31mTu as mauvais...\033[0;35m")
        point -= down_point

    print("Tes points sont a " + str(point) + "/" + str(len(questions) * up_point))

    q+=1

