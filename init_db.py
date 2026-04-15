import io
import os
import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

with con:
    data = {
        "theme": ["cross_joins", "cross_joins"],
        "exercise_name": ["beverages_and_foods", "sizes_and_trademarks"],
        "tables": [["beverages", "food_items"], ["sizes", "trademarks"]],
        "last_reviewed": ["1980-01-01", "1970-01-01"],
    }

    # memory_state_df = pd.DataFrame(data)
    memory_state_df = pd.DataFrame.from_dict(data)

    con.execute(
        "CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df"
    )

    # ------------------------------------------------------------
    # CROSS JOIN EXERCISES
    # ------------------------------------------------------------
    csv = """
    beverage,price
    orange juice,2.5
    Expresso,2
    Tea,3
    tedo,4
    """
    beverages = pd.read_csv(io.StringIO(csv))
    con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

    sizes = """
    size
    XS
    M
    L
    XL
    XXL
    """
    sizes = pd.read_csv(io.StringIO(sizes))
    con.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")

    trademarks = """
    trademark
    Nike
    Asphalte
    Abercrombie
    Lewis
    Asso
    """

    trademarks = pd.read_csv(io.StringIO(trademarks))
    con.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")
