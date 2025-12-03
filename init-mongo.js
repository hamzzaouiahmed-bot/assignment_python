db = db.getSiblingDB('AhmedDB');

db.users.insertMany([
  {
    name: "Ahmed",
    email: "ahmed@example.com",
    profile: { age: 23, city: "Tunis" }
  },
  {
    name: "Ons",
    email: "ons@example.com",
    profile: { age: 25, city: "Sousse" }
  },
  {
    name: "Alex",
    email: "alex@example.com",
    profile: { age: 28, city: "Monastir" }
  }
]);
