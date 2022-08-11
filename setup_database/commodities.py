from finance_database.utils import COMMODITIES
from finance_database import Database

db = Database()
con = db.connection
cur = db.cursor

for name, properties in COMMODITIES.items():
    sector_id = cur.execute(f"SELECT id FROM cme_commodity_sectors WHERE name = ?", (properties['sector name'],)).fetchone()[0]
    exchange_id = cur.execute(f"SELECT id FROM yahoo_exchanges WHERE yahoo_suffix = '.CME'").fetchone()[0]
    cur.execute(
        f"INSERT OR IGNORE INTO cme_commodities (name, exchange_id, sector_id) VALUES (?, ?, ?)",
        (name, exchange_id, sector_id)
    )

con.commit()
con.close()