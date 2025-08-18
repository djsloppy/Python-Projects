import sqlite3

# This function will connect to the database, check to see if the table 
# exists and if not will create it. If it does exist, will ignore that 
# line. Finally it will close the db connection.
def create_tbl():
    conn = sqlite3.connect('python_bc.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            fileName TEXT \
            )")
        conn.commit()
    conn.close()

# This function will use the fileList and search it for all .txt files and
# then will connect to the database, enter them into the database. It will
# also display them to the screen.
def enterdata():
    fileList = ('information.docx','Hello.txt','myImage.png', \
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    for x in fileList:
        if x.endswith('.txt'):
            conn = sqlite3.connect('python_bc.db')
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files(fileName) VALUES (?)", (x,))
                print(x)
                conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tbl()
    enterdata()
