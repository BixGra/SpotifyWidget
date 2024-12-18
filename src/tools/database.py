import sqlite3 as sl

from src.tools.utils import random_string


class Database:
    def __init__(self):
        self.con = sl.connect("./src/data/spotifywidget.db", check_same_thread=False)

        with self.con:
            self.con.execute("""
                CREATE TABLE IF NOT EXISTS SPOTIFYWIDGET (
                    id TEXT NOT NULL PRIMARY KEY,
                    mail TEXT NOT NULL UNIQUE,
                    token TEXT NOT NULL,
                    refresh_token TEXT NOT NULL,
                    last_update TEXT DEFAULT CURRENT_TIMESTAMP
                );
            """)


    def exists_id(self, user_id: str) -> bool:
        """Return True is the id exists, else False"""
        with self.con:
            cur = self.con.cursor()
            cur.execute(f"""
                SELECT id FROM SPOTIFYWIDGET WHERE id = "{user_id}";
            """)
            return bool(cur.fetchone())


    def exists_mail(self, mail: str) -> [None|str]:
        """Returns the token if the mail exists, else None"""
        with self.con:
            cur = self.con.cursor()
            cur.execute(f"""
                SELECT id FROM SPOTIFYWIDGET WHERE mail = "{mail}";
            """)
            if result:= cur.fetchone():
                return result[0]
            else:
                return None


    def create_user(self, mail: str, token: str, refresh_token: str) -> str:
        """Creates a new user and returns their token"""
        with self.con:
            cur = self.con.cursor()
            if user_id:= self.exists_mail(mail):
                cur.execute(f"""
                    UPDATE SPOTIFYWIDGET
                    SET token = "{token}", refresh_token = "{refresh_token}"
                    WHERE id = "{user_id}";
                """)
                return user_id
            else:
                cur.execute("""
                    SELECT id FROM SPOTIFYWIDGET;
                """)
                user_ids = cur.fetchall()
                user_id = random_string(16)
                while user_id in user_ids:
                    user_id = random_string(16)
                cur.execute(f"""
                    INSERT INTO SPOTIFYWIDGET (id, mail, token, refresh_token)
                    values ("{user_id}", "{mail}", "{token}", "{refresh_token}");
                """)
                return user_id

    def delete_user(self, user_id: str):
        with self.con:
            cur = self.con.cursor()
            cur.execute(f"""
                DELETE FROM SPOTIFYWIDGET
                WHERE id = "{user_id}";
            """)


    def get_token(self, user_id: str) -> [str|None]:
        if self.exists_id(user_id):
            with self.con:
                cur = self.con.cursor()
                cur.execute(f"""
                    SELECT token FROM SPOTIFYWIDGET WHERE id = "{user_id}";
                """)
                return cur.fetchone()[0]
        else:
            return None


    def get_refresh_tokens(self) -> list[tuple]:
        """Returns a list of tuples (refresh_token, user_id)"""
        with self.con:
            cur = self.con.cursor()
            cur.execute("""
                SELECT refresh_token, id FROM SPOTIFYWIDGET;
            """)
            return cur.fetchall()


    def set_refreshed_tokens(self, refreshed_tokens: list[tuple]) -> None:
        """Takes a list of tuples (refreshed_token, user_id)"""
        query = """
                UPDATE SPOTIFYWIDGET
                SET token=?
                WHERE id=?;
            """
        with self.con:
            cur = self.con.cursor()
            cur.executemany(query, refreshed_tokens)
