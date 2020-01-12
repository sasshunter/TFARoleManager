import sqlite3
from discord.member import Member

class DBHandler:
    """provides contextual functions to query db information"""

    def __init__(self, fn):
        self.conn = sqlite3.connect(fn) # 'tfa.db'
        self.c = self.conn.cursor()

    def update_member(self, member:Member):
        self.c.execute("UPDATE Member SET (discordDisplayName=?,discordUserTag=?) WHERE discordUserId=?;", (member.display_name, member.name+member.discriminator, member.id))
        if self.c.rowcount == 0:
            self.c.execute("INSERT INTO Member VALUES(?,?,?);", member.id, member.display_name, member.name+member.discriminator)
        
    def create_member_skill(self, id:str, skillroleid:str):
        self.c.execute("INSERT OR IGNORE INTO MemberSkill VALUES (?,?);", (id, skillroleid))

    def get_members_with_skill(self, skillroleid:str):
        self.c.execute("SELECT Member.* FROM MemberSkill WHERE DiscordRoleId_=? JOIN Member ON MemberSkill.DiscordUserId_ = Member.DiscordUserId;",(skillroleid,))
        return self.c.fetchall()

    def get_member_by_name(self,name:str):
        """get a single user by nickname"""
        print("Trying to find user "+name +" in db")
        self.c.execute("SELECT * FROM Member WHERE discordDisplayName LIKE ?;", (name,))
        res = self.c.fetchall()

        # we only want one user, so fail if we match with more than one - or none
        if len(res) == 1:
            return res[0] 
        elif len(res) > 1:
            return False
        else:
            return None

    def get_skill_by_easyname(self,easyname:str):
        print("get_skill_by_easyname(self, "+easyname+")")
        self.c.execute("SELECT * FROM Skill WHERE skillEasyName LIKE ?;", (easyname,))

        res = self.c.fetchall()

        # bork if we don't get one
        if len(res) == 1:
            return res[0] 
        else:
            return None