import pymysql


def connect(self, user, password, database):
        global db
        # prepare a cursor object using cursor() method
        db = pymysql.connect("localhost", user, password, database)

def insert(self, drink, alcohol, mixer, alcweight, mweight ):
    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO DRINKS(DRINK, ALCOHOL, MIXER, ALCWHEIGHT, MWEIGHT) VALUES('" + drink + ", " + mixer + ", " + alcweight + ", " + mweight + ")"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

def delete(drink):
    cursor = db.cursor()
    sql = ("DELETE FROM DRINKS WHERE NAME = '" + drink + "'")
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


def display_rows():
    cursor = db.cursor()
    rows = []

    try:
        cursor.execute("SELECT * FROM drinks")
        db_top_string = "\nDrink     	Mixer		alcWeight		mWeight"
        db_sep_string = "==========================================================="

        for reading in cursor.fetchall():
            rows.append((str(reading[0]) + "	" + str(reading[1]) + " 	" + reading[2] + "  	" + str(reading[3])))
    except:
        db.rollback()

    return db_top_string, db_sep_string, rows