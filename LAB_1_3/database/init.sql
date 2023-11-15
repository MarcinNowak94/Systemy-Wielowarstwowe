CREATE TABLE Examples(
    ID    INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    ExampleName  TEXT NOT NULL,
    ExampleValue double precision NOT NULL
);

--Initialize data
INSERT INTO Examples(ExampleName, ExampleValue) Values
    ('Bit',     1),
    ('Bitter',  0),
    ('One',     4),
    ('Three',   11),
    ('Seven',   3.14);
