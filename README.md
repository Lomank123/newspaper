# newspaper
Auto posting news project, including user management and reactions.

## Services

### accounts

User management and all related stuff. Provide API to fetch user data from connected db.


### articles

Articles management. Categories, articles and related stuff. Provide API to fetch data from connected db.


### data_loader

Periodically auto-insert new data (e.g. articles) to db by fetching it from external API.


### reactions

User reactions to articles. Each article can have multiple different reactions from different users. Provide API to fetch reactions from connected db.
