from database.DB_connect import DBConnect
from model.state import State


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getShape():
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        query = """select DISTINCT shape 
from sighting s
"""
        cursor.execute(query, ())
        results = []
        for row in cursor:
            results.append(row[0])
        cursor.close()
        conn.close()
        return results
    @staticmethod
    def getStates():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        query = """select *
from state s 
"""
        cursor.execute(query, ())
        results = []
        for row in cursor:
            results.append(State(**row))
        cursor.close()
        conn.close()
        return results
    @staticmethod
    def getPeso(anno, shape):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        query = """SELECT n.state1, n.state2 , count(*) as N
                    FROM sighting s , neighbor n 
                    where year(s.`datetime`) = %s
                    and s.shape = %s
                    and (s.state = n.state1 or s.state = n.state2 )
                    and n.state1 < n.state2
                    group by n.state1 , n.state2
"""
        cursor.execute(query, (anno, shape))
        results = {}
        for row in cursor:
            results[(row['state1'], row['state2'])] = row['N']
        cursor.close()
        conn.close()
        return results
