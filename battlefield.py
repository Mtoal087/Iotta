import sqlite3

connect = sqlite3.connect("Iotta.db")


def battle(username):
	view_offline(username)


def view_offline(username):
    from first import options
    cursor = connect.cursor()
    boolean = False
    cursor.execute("SELECT user FROM Login WHERE login =?", (boolean,))
    results = cursor.fetchall()
    i = 1
    print()
    
    if not results:
        print("No offline users found.")
        return
    print()
    print("Who would you like to battle?")
    for result in results:
        print(f"{i}\t\t{result[0]}")
        i += 1
    print(f"0\t\tTo go back to homepage")
    
    user = int(input())
    if user == 0:
        options(username)
    else:
        if user > len(results):
            print("Invalid input")
            print("Please try again!")
            print()
            view_offline(username)
        else:
            checkFor_Creatures(username, results[user - 1][0])
    


##### checks if each user has at least one creature
def checkFor_Creatures(username, opponent):
    cursor = connect.cursor()

    cursor.execute("SELECT noOfCreatures FROM User WHERE user =?", (username,))
    userResults = cursor.fetchone()

    if userResults[0] == 0:
        print()
        print("You have not created any creatures.")
        print()
        view_offline(username)

    cursor.execute("SELECT noOfCreatures FROM User WHERE user =?", (opponent,))
    opponentResults = cursor.fetchone()

    if opponentResults[0] == 0:
        print()
        print("The opponent has not created any creatures.")
        print()
        view_offline(username)
    else:
        print(f"BATTLING...")
        battling(username, opponent)


def battling(username, opponent):
    cursor = connect.cursor()


    # Gets all creatures for the user
    cursor.execute("SELECT damage, health FROM Creature WHERE user =?", (username,))
    userResults = cursor.fetchall()

    # Gets all creatures for the opponent
    cursor.execute("SELECT damage, health FROM Creature WHERE user =?", (opponent,))
    opponentResults = cursor.fetchall()

    userHealth = 0
    userDamage = 0
    total = 0
    for creature in userResults:
        if creature[0] + creature[1] > total:
            total = creature[0] + creature[1]
            userHealth = creature[1]
            userDamage = creature[0]

    opponentHealth = 0
    opponentDamage = 0
    oTotal = 0
    for creature in opponentResults:
        if creature[0] + creature[1] > oTotal:
            oTotal = creature[0] + creature[1]
            opponentHealth = creature[1]
            opponentDamage = creature[0]

    #print(f"User/ Damage: {userDamage}, health: {userHealth}")
    #print(f"Opponent/ Damage: {opponentDamage}, health: {opponentHealth}")

    while userHealth > 0 and opponentHealth > 0:
        opponentHealth -= userDamage
        userHealth -= opponentDamage
    
    if userHealth > 0:
        print(f"You have won!")
        updateRank(username, opponent, username, opponent)
    elif opponentHealth > 0:
        print(f"The opponent has won...")
        updateRank(username, opponent, opponent, username)
    else:
        print("DRAW")
        view_offline(username)



def updateRank(username, opponent, winner, loser):
    cursor = connect.cursor()
    cursor.execute("UPDATE User SET rank = rank + 2 WHERE user =?", (winner,))
    connect.commit()
    cursor.execute("UPDATE Leaderboard SET rank = rank + 2 WHERE user =?", (winner,))
    connect.commit()

    cursor.execute("SELECT rank FROM User WHERE user =?", (loser,))
    loserRank = cursor.fetchone()
    loserRank = loserRank[0]
    if loserRank > 1:
        cursor.execute("UPDATE User SET rank = rank - 1 WHERE user =?", (loser,))
        connect.commit()
        cursor.execute("UPDATE Leaderboard SET rank = rank - 1 WHERE user =?", (loser,))
        connect.commit()

    cursor.execute("SELECT rank FROM User WHERE user =?", (username,))
    rank = cursor.fetchone()
    rank = rank[0]
    print(f"Your rank is: {rank}")

    updateBattleTable(username, opponent, winner)
    view_offline(username)


def updateBattleTable(username, opponent, winner):
    cursor = connect.cursor()
    cursor.execute('''INSERT INTO Battle (user, opponent, winner) VALUES (?,?,?)''',
                (username, opponent, winner))
    connect.commit()
    return
