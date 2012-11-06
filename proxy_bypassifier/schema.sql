drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  url string not null,
  body string not null,
  last_update datetime not null
);
