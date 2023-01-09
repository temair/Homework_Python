import sqlite3
import datetime
import ast

class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS subscriptions(
   user_id INT PRIMARY KEY,
   status TEXT,
   ban TEXT,
   count_search INT,
   reg_date TEXT,
   photo_id INT,
   message_date TEXT,
   balance INT
   );
""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS log(
   log_id INT PRIMARY KEY,
   user_id INT,
   time TEXT,
   status TEXT,
   photo_id INT
   );
""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS phones(
   phone TEXT PRIMARY KEY,
   name TEXT
   );
""")
    def get_subscriptions(self, status = True):
        """Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()

    def subscriber_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status = True, ban = True, count_search = 0, reg_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), photo_id = 0, message_date = datetime.datetime.now().strftime('%Y/%m/%d/%H/%M/%S/%f'), balance = 30):
        """Добавляем нового подписчика"""
        with self.connection:
            self.cursor.execute("INSERT INTO subscriptions (user_id, status, ban, count_search, reg_date, photo_id, message_date, balance) VALUES(?,?,?,?,?,?,?,?)", (user_id,status,ban,count_search,reg_date,photo_id, message_date, balance))
            return self.connection.commit()

    def update_subscription(self, user_id, status):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))
            return self.connection.commit()

    def set_ban(self, user_id, ban):
        """Ставим бан пользователю"""
        with self.connection:
            self.cursor.execute("UPDATE `subscriptions` SET `ban` = ? WHERE `user_id` = ?", (ban, user_id))
            return self.connection.commit()

    def ban_exists(self, user_id):
        """Проверяем, есть ли бан у пользователя"""
        with self.connection:
            info_ban = self.cursor.execute("SELECT `ban` FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()[0][0]
            return bool(int(info_ban))

    def get_profile(self, user_id):
        """Получаем профиль пользователя"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()

    def update_count_search(self, user_id):
        """Увеличиваем кол-во поисков"""
        with self.connection:
            count_search = self.cursor.execute("SELECT `count_search` FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()[0][0]
            count_search += 1
            self.cursor.execute("UPDATE `subscriptions` SET `count_search` = ? WHERE `user_id` = ?", (count_search, user_id))
            return self.connection.commit()

    def save_photo(self, user_id, photo_id):
        """Сохраняем текущее фото"""
        with self.connection:
            self.cursor.execute("UPDATE `subscriptions` SET `photo_id` = ? WHERE `user_id` = ?", (photo_id, user_id))
            return self.connection.commit()

    def update_history(self, user_id, log_id = 0, time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), status = None, photo_id = 0):
        """Обоновляем лог"""
        with self.connection:
            self.cursor.execute("INSERT INTO `log` (`log_id`, `user_id`, `time`, `status`, `photo_id`) VALUES(?,?,?,?,?)", (log_id,user_id,time,status,photo_id))
            return self.connection.commit()

    def update_message_date(self, user_id):
        with self.connection:
            date = datetime.datetime.now() + datetime.timedelta(seconds=10)
            date = date.strftime('%Y/%m/%d/%H/%M/%S/%f')
            self.cursor.execute("UPDATE `subscriptions` SET `message_date` = ? WHERE `user_id` = ?", (date, user_id))
            return self.connection.commit()

    def get_message_date(self, user_id):
        with self.connection:
           date = self.cursor.execute("SELECT `message_date` FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()[0][0]
           return datetime.datetime.strptime(date, '%Y/%m/%d/%H/%M/%S/%f')

    def phone_exists(self, phone):
        with self.connection:
            return bool(len(self.cursor.exeucte("SELECT * FROM `phones` WHERE `phone` = ?", (phone,)).fetchall()))

    def get_name_for_phone(self, phone):
        with self.connection:
            return self.cursor.execute("SELECT `name` FROM `phones` WHERE `phone` = ?", (phone,)).fetchall()

    def add_phone(self, phone, name):
        with self.connection:
            return self.cursor.execute("INSERT INTO `phones` (phone, name) VALUES(?,?)", (phone, name))

    def get_balance(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT `balance` FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()[0][0]

    def update_balance(self, user_id, balance = 0):
        with self.connection:
            if balance:
                old_balance = self.get_balance(user_id)
                balance += old_balance
            return self.cursor.execute("UPDATE `subscriptions` SET `balance` = ? WHERE `user_id` = ?", (balance, user_id))

    def run_command(self, command):
        """Выполняем команду"""
        with self.connection:
            self.cursor.execute(command)
            result = self.cursor.fetchone()
            self.connection.commit()
            return result
            
    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()