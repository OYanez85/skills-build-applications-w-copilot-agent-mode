// Initialize the MongoDB database and create collections with the required structure

// Explicitly reference the database for each operation
const db = db.getSiblingDB("octofit_db");

// Create the users collection with a unique index on the email field
db.createCollection("users");
db.users.createIndex({ "email": 1 }, { unique: true });

// Create the teams collection
db.createCollection("teams");

// Create the activity collection
db.createCollection("activity");

// Create the leaderboard collection
db.createCollection("leaderboard");

// Create the workouts collection
db.createCollection("workouts");
