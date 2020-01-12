import sqlite3
from discord.member import Member

class DBHandler:
    """provides contextual functions to query db information"""

    def __init__(self, fn):
        self.conn = sqlite3.connect(fn) # 'tfa.db'
        self.c = conn.cursor()

    def update_member(self, member:Member):
        self.c.execute("UPDATE Member SET (discordDisplayName=?,discordUserTag=?) WHERE discordUserId=?;", member.display_name, member.name+member.discriminator, member.id)
        if self.c.rowcount == 0:
            self.c.execute("INSERT INTO Member VALUES(?,?,?)", member.id, member.display_name, member.name+member.discriminator)
        
    def create_member_skill(self, member:Member, skill:int):
        """skill:int : skillid"""
