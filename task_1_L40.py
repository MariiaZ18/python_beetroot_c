import sqlite3

con = sqlite3.connect('task1.db')
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS TASK1")
table = """ CREATE TABLE task1 (
            First_Name CHAR(25) NOT NULL,
            Last_Name CHAR(25),
            Age INT
        ); """

cur.execute(table)
new_column = "ALTER TABLE task1 ADD COLUMN User_Name CHAR(25)"
cur.execute(new_column)

insert_data = "INSERT INTO task1 (First_Name, Last_Name, Age, User_Name) VALUES ('Eva', 'Milos', 21, 'eva_m_20');"
insert_data2 = "INSERT INTO task1 (First_Name, Last_Name, Age, User_Name) VALUES ('Diana', 'Zeikan', 25, 'Di_222');"
cur.execute(insert_data)
cur.execute(insert_data2)
cur.execute(
    "INSERT INTO task1 VALUES('Krishna', 'Sharma', 19, 'kris_19' ),('Raj', 'Kandukuri', 20, 'raj_raj123'),('Ramya', 'Ramapriya', 25, 'ramya_tttt'),('Mac', 'Mohan', 26, 'mac_gg');")

update = "UPDATE task1 SET AGE = 28 WHERE First_Name = 'Diana'"
cur.execute(update)
cur.execute("DELETE FROM task1 WHERE Last_Name = 'Milos'")

con.commit()
con.close()
