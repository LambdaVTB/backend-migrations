CREATE CONSTRAINT constraint_users FOR (u:User) REQUIRE (u.identifier) IS UNIQUE;
CREATE CONSTRAINT constraint_items FOR (i:Item) REQUIRE (i.identifier) IS UNIQUE;
