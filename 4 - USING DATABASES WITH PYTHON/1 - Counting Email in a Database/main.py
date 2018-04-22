import sqlite3

conn = sqlite3.connect('ceiDB.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))


conn.commit()

# Check if the script has run as it would have
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

print("ORGANIZATION | COUNT")
for row in cur.execute(sqlstr):
    print(str(row[0]), str(row[1]))

cur.close()