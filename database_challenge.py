import sqlite3

values = (("Jean-Baptiste Zorg","Human",122),("Korben Dallas","Meat Puppet",100),("Ak'not","Mangalore",-5))

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

with conn:
    cur.execute("CREATE TABLE IF NOT EXISTS Roster( \
        Name TEXT, \
        Species TEXT, \
        IQ INTEGER \
        );")
    conn.commit()
    
    cur.executemany("INSERT INTO Roster (Name, Species, IQ) VALUES (?,?,?)",(values))
    conn.commit()

    cur.execute("UPDATE Roster SET Species=? WHERE Name=?",("Human","Korben Dallas"))
    conn.commit()

    cur.execute("SELECT Name, IQ FROM Roster WHERE Species='Human'")
    data = cur.fetchall()
    for row in data:
        print(row)
conn.close()
