CREATE TABLE flow_items(
   id serial PRIMARY KEY,
   li text,
   de text,
   roadway text,
   pc decimal not null,
   qd varchar(1),
   le decimal not null,
   ty text,
   sp decimal,
   su decimal,
   ff decimal not null,
   jf decimal not null,
   cn decimal not null,
   pbt timestamp NOT NULL,
   processed_at timestamp
   -- geom geometry(MultiLineString, 4326)
);
