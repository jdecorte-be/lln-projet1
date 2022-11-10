from LibrairieLectureFichierQCM import qcm
import sys
import random


# Chargement du questionnaire + selection du fichier en argv[1]
questions = qcm.build_questionnaire(sys.argv[1])

# Melange du questionnaire
random.shuffle(questions)

print("\033[0;36mWelcome to the best QCM Shuffle in the world.")
print("\033[0;36m================================================\033[0;35m")
print("\033[0;36mChoisissez votre difficultées :\n\t1)Facile\t2)Moyen\t\t3)Dur")
print("\033[0;36m================================================\033[0;35m")


'''
    Systeme de cotation : 
    - Easy : correct : +2 incorrect : -1
    - Medium : correct : +1 incorrect : -1
    - Hard : correct : +1 incorrect : -2
'''
while True :
    lvl = input("\033[0;36mEntrer votre difficultée : \u001b[37m")
    if (not lvl.isnumeric()) :
        print("\u001b[31mVotre reponse doit être un nombre!")
    elif not (1 <= int(lvl) and int(lvl) <= 3):
        print("\u001b[31mCette réponse existe pas! Entrer un index valide...")
    else :
        break
'''
    La while permet de demander a l'utilisateur ca réponse tout en
    sachant si elle a le format valide. C'est a dire si c'est bien un nombre
    sinon il renvoie une erreur et redemande une réponse valide
'''
if(lvl == "1") :
    up_point = 2
    down_point = 1
elif(lvl == "2") :
    up_point = 1
    down_point = 1
elif(lvl == "3") :
    up_point = 1
    down_point = 2

# Defini le max de point atteignable 
point = len(questions) * up_point

q = 0
while q < len(questions):
    print("\t\033[0;36mQuestion " + str(q+1) + ": \"" + questions[q][0] + "\"\033[0;35m")
    for r in range(len(questions[q][1])):
        print("\t\t" + str(r+1) + ") " + questions[q][1][r][0])

    '''
        La while permet de demander a l'utilisateur ca réponse tout en
        sachant si elle a le format valide. C'est a dire si c'est bien un nombre
        sinon il renvoie une erreur et demande une nouvelle réponse.
    '''

    while True :
        n = input("\033[0;36mEnter your answer : \u001b[37m")

        if (not n.isnumeric()) :
            print("\u001b[31mVotre réponse doit être un nombre!")
        elif  (not (1 <= int(n) and int(n) <= len(questions[q][1]))):
            print("\u001b[31mCette réponse existe pas! Entrer un index valide...")
        else :
            break


    '''
        Perd des points en cas de mauvaise réponse
        ou en gagne en cas de bonne réponse par rapport au niveau choisis.
    '''
    if(str(questions[q][1][int(n) - 1][1]) == "True") :
        print("\033[0;32mBravo ! Tu as bon !\033[0;35m")
    else :
        print("\033[0;31mTu as mauvais...\033[0;35m")
        point -= down_point

    if(questions[q][1][int(n) - 1][2]) :
        print("Feedback: " + questions[q][1][int(n) - 1][2])
    print("Tes points sont a " + str(point) + "/" + str(len(questions) * up_point))
    q+=1
