CREATE TABLE Values(
    ID    INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    Name  TEXT NOT NULL,
    Value double precision NOT NULL
)

--Initialize data
INSERT INTO [Values]([Name], [Value]) Values
    ("Bit",     1),
    ("Bitter",  0),
    ("One",     4),
    ("Three",   11),
    ("Seven",   3.14);
