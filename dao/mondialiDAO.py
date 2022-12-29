from dao.utility.db import MySql
from dto.mondialiDTO import *

class MondialiDao:
    @classmethod
    def getNotHomeWinner(cls):
        MySql.openConnection()
        MySql.query("select s.nazione from squadra s \
                    inner join organizzazione o on s.anno=o.anno \
                    where s.nazione <> o.nazione and s.posizioneInClassifica=1 \
                    group by s.nazione \
                    except \
                    select s.nazione from squadra s \
                    inner join organizzazione o on s.anno=o.anno \
                    where s.nazione <> o.nazione and s.posizioneInClassifica=1 \
                    group by s.nazione;")
        data= MySql.getResults()
        result=[]
        for i in data:
            result.append(NotHomeWinner(i[0]))
        MySql.closeConnection()
        
        return result
    
    @classmethod
    def getAllHugeNationbyWC(cls):
        MySql.openConnection()
        MySql.query("SELECT Anno, Nazione, COUNT(Nazione) as Convocazioni \
                    FROM Partecipazione  p \
                    GROUP BY Anno, Nazione \
                    HAVING COUNT(Nazione) = (SELECT MAX(Convocati) \
                        FROM ( \
	                    SELECT Anno, Nazione, count(Nazione) as Convocati \
	                    FROM Partecipazione \
                        WHERE anno=P.anno \
	                    GROUP BY Anno, Nazione) s );")
        data= MySql.getResults()
        result=[]
        for i in data:
             result.append(AllHugeNationbyWC(i[0],i[1],i[2]))
        MySql.closeConnection()
        
        return result
    
    @classmethod
    def getPlayersWithThreeWCOrTwoNation(cls):
        MySql.openConnection()
        MySql.query("SELECT pg.Nome \
                    FROM (SELECT p.IDGiocatore, g.Nome, COUNT(*) as Partecipazioni \
                    FROM partecipazione p \
                    INNER JOIN giocatore g ON p.IDGiocatore = g.ID \
                    GROUP BY p.IDGiocatore, g.Nome) as pg \
                    WHERE pg.Partecipazioni >= 3 OR 1 < (SELECT COUNT(*) as numero_nazioni \
                                   FROM partecipazione p \
                                   WHERE p.IDGiocatore = pg.IDGiocatore);")
        data= MySql.getResults()
        result=[]
        for i in data:
            result.append(PlayersWithThreeWCOrTwoNation(i[0]))
        MySql.closeConnection()
        
        return result