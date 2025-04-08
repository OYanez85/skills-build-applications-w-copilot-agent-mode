// Switch to the octofit_db database
use octofit_db;

// List all collections in the database
printjson(db.getCollectionNames());
