import sqlite3

class DB(object):
    conn = None
    cur = None
    table = ''
    where = ''

    def __init__(self, dbname = 'example.db'):
        self.connect(dbname)

    def __del__(self):
        self.conn.close()

    def connect(self, dbname):
        self.conn = sqlite3.connect(dbname)
        return self

    def table(self, name):
        self.table = name
        return self.create_table_if_not_exists(name)

    def create_table_if_not_exists(self, table):
        self.query(open(table + '.sql').read())
        self.conn.commit()
        return self

    def insert(self, fields):
        keys = ', '.join(fields.keys())
        values = "', '".join(fields.values())
        sql = "INSERT INTO %s (%s) VALUES ('%s')" % (self.table, keys, values)

        self.query(sql)
        self.conn.commit()
        return self.last_row_id()

    def insert_many(self, list_of_fields_to_insert):
        sql = 'INSERT INTO %s VALUES (%s)' % (self.table, (len(list_of_fields_to_insert[0]) * '?,')[:-1])
        self.cur = self.conn.cursor()
        self.cur.executemany(sql, list_of_fields_to_insert)
        self.conn.commit()
        return self

    def update(self, fields):
        to_set = ''
        for key, value in fields.iteritems():
            to_set += "%s = '%s'" % (key, value)
        sql = "UPDATE %s SET %s%s" % (self.table, to_set, self.where)
        return self.query(sql)

    def where(self, *where):
        # default operator will be = (equal)
        operator = '='

        if len(where) is 3:
            [field, operator, value] = list(where)
        elif len(where) is 2:
            [field, value] = list(where)

        self.where = " WHERE %s %s '%s'" % (field, operator, value)
        return self

    def fetch_query(self):
        sql = "SELECT * FROM %s%s" % (self.table, self.where)
        return self.query(sql)

    def first(self):
        self.fetch_query()
        return self.cur.fetchone()

    def get(self):
        self.fetch_query()
        return self.cur.fetchall()

    def many(self, records):
        self.fetch_query()
        return self.cur.fetchmany(records)

    def all(self):
        sql = 'SELECT * FROM %s' % self.table
        self.query(sql)
        return self.cur.fetchall()

    def count(self):
        return len(self.all())

    def last_row_id(self):
        if not self.cur is None:
            return self.cur.lastrowid
        self.query('SELECT * FROM %s' % self.table)
        return self.last_row_id()

    def query(self, sql):
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
        return self
