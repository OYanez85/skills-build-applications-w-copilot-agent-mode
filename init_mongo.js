// Switch to the octofit_db database
use octofit_db;

// Create collections
db.createCollection('users');
db.createCollection('teams');
db.createCollection('activity');
db.createCollection('leaderboard');
db.createCollection('workouts');

// Create a unique index for the users collection
db.users.createIndex({ email: 1 }, { unique: true });
