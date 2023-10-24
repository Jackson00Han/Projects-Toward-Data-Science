# MEteorite Cleaning

# Problem to Solve

As a data engineer at NASA, you often spend your time cleaning meteorites—or at least the data they create.

You’ve been given a CSV file of historical meteorite landings here on Earth, of which there are quite a few! Your job is to import the data into a SQLite database, cleaning it up along the way. After you’re done, the database will be used in analyses by some of your fellow engineers.

## Specification

In `import.sql`, write a series of SQL (and SQLite) statements to import and clean the data from `meteorites.csv` into a table, `meteorites`, in a database called `meteorites.db`.

Within `meteorites.db`, the `meteorites` table should have the following columns:

### Columns in the meteorites table

Keep in mind that not all columns in the CSV should end up in the final table!

To consider the data in the `meteorites` table clean, you should ensure…

- Any empty values in `meteorites.csv` are represented by NULL in the `meteorites` table.
  - Keep in mind that the mass, year, lat, and long columns have empty values in the CSV.
- All columns with decimal values (e.g., 70.4777) should be rounded to the nearest hundredths place (e.g., 70.4777 becomes 70.48).
  - Keep in mind that the mass, lat, and long columns have decimal values.
- All meteorites with the nametype “Relict” are not included in the `meteorites` table.
- The meteorites are sorted by year, oldest to newest, and then—if any two meteorites landed in the same year—by name, in alphabetical order.
- You’ve updated the IDs of the meteorites from `meteorites.csv`, according to the order specified in #4.
  - The id of the meteorites should start at 1, beginning with the meteorite that landed in the oldest year and is the first in alphabetical order for that year.

