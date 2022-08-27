import pymysql
from config import db_name, host, password, user

from YM_news.pars_Y_news import get_data, send_url


def push_mysql(values):
    """Import values in Postgres"""
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("successfully connected...")

        try:
            cursor = connection.cursor()

            """create table"""
            # with connection.cursor() as cursor:
            #     create_table_query = "CREATE TABLE `news`(id int AUTO_INCREMENT," \
            #                          "title varchar(255)," \
            #                          "datetime DATETIME," \
            #                          "tags varchar(32), PRIMARY KEY (`id`));"
            #     cursor.execute(create_table_query)
            #     print("Table created successfully")

            k = 0
            v = 1
            for i in values:
                title = values[k]
                print(title)
                datetime = values[v]
                print(datetime)
                k += 2
                v += 2

                """insert data"""
                with connection.cursor() as cursor:
                    insert_query = (
                        "INSERT INTO parsing_news "
                        "(id, title, datetime, tags) "
                        "VALUES ('%(id)s', '%(title)s', '%(datetime)s', '%(tags)s')"
                        % {
                            "id": id,
                            "title": title,
                            "datetime": datetime,
                            "tags": "Yandex",
                        }
                    )
                    cursor.execute(insert_query)
                    connection.commit()

            """select all data from table"""
            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM `parsing_news`"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)


push_mysql(get_data(send_url))
