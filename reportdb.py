import psycopg2
import bleach

DBNAME = "news"

# get top 3 articles
get_top_articles = '''
                    SELECT articles.title, COUNT(log.path) AS num
                    FROM log, articles
                    WHERE articles.slug = SUBSTRING(log.path, '[^/]*$')
                    GROUP BY articles.title
                    ORDER BY num DESC
                    LIMIT 3;
                   '''

# get top 3 authors
get_top_authors = '''
                    SELECT authors.name, COUNT(log.path) AS num
                    FROM log, authors, articles
                    WHERE authors.id=articles.author
                    AND articles.slug = SUBSTRING(log.path, '[^/]*$')
                    GROUP BY authors.name
                    ORDER BY num DESC
                    LIMIT 3;
                    '''

# get the date that HTTP failed rate is greater than 1 percent
get_failed_rate_greater_than_1 = '''
                    SELECT CAST(log.time AS DATE)
                    AS days,
                    CAST(sum(
                        CASE
                            WHEN log.status='404 NOT FOUND' THEN 1 ELSE 0
                        END)*100
                        AS FLOAT
                        )/COUNT(*)
                    AS percentage_greater_than_1
                    FROM log
                    GROUP BY days
                    HAVING CAST(sum(
                        CASE
                            WHEN log.status='404 NOT FOUND' THEN 1 ELSE 0
                        END)*100
                        AS FLOAT)/COUNT(*)>1
                    ORDER BY days DESC;
                    '''


def run_query(sql_query):
    """Connect to data base and run query. After the query is finished,
    disconnect the database."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    result = c.fetchall()
    db.close()
    return result


def print_top_articles():
    '''
        run query and print out information
    '''
    top_articles = run_query(get_top_articles)
    print("Top 3 articles")
    for row in top_articles:
        print(row[0] + " - " + str(row[1]))


def print_top_authors():
    '''
        run query and print out information
    '''
    top_authors = run_query(get_top_authors)
    print("Top 3 authors")
    for row in top_authors:
        print(row[0] + " - " + str(row[1]))


def print_fail_rate_greater_than_1():
    '''
        run query and print out information
    '''
    rate_greater_than_1 = run_query(get_failed_rate_greater_than_1)
    print("The date that failed rate is greater than 1")
    for row in rate_greater_than_1:
        print(str(row[0]) + " - " + str(round(row[1], 2)) + "%.")


# start of the program
print_top_articles()
print ""
print_top_authors()
print ""
print_fail_rate_greater_than_1()
