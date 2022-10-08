CREATE CONSTRAINT constraint_users FOR (u:User) REQUIRE (u.id) IS UNIQUE;
CREATE CONSTRAINT constraint_items FOR (i:Item) REQUIRE (i.id) IS UNIQUE;
