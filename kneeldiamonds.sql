CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` INTEGER NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);


CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    [metal_id] INTEGER NOT NULL,
    [size_id] INTEGER NOT NULL,
    [style_id] INTEGER NOT NULL,
    FOREIGN KEY (`metal_id`) REFERENCES `Metals`(`id`)
    FOREIGN KEY (`size_id`) REFERENCES `Sizes`(`id`)
    FOREIGN KEY (`style_id`) REFERENCES `Styles`(`id`)
);




-- INSERT DATA BELOW

INSERT INTO Metals
(metal, price)
VALUES ("Sterling Silver", 12.42);

INSERT INTO Metals
(metal, price)
VALUES ("14k Gold", 736.4);

INSERT INTO Metals
(metal, price)
VALUES ("24K Gold", 1258.9);

INSERT INTO Metals
(metal, price)
VALUES ("Platinum", 795.45);

INSERT INTO Sizes
(carets, price)
VALUES (0.5, 405);

INSERT INTO Sizes
(carets, price)
VALUES (0.75, 782);

INSERT INTO Sizes
(carets, price)
VALUES (1, 1470);

INSERT INTO Sizes
(carets, price)
VALUES (1.5, 1997);

INSERT INTO Sizes
(carets, price)
VALUES (2, 3638);

INSERT INTO Styles
(style, price)
VALUES ("Classic", 500);

INSERT INTO Styles
(style, price)
VALUES ("Modern", 710);

INSERT INTO Styles
(style, price)
VALUES ("Vintage", 965);


INSERT INTO Orders
(metal_id, size_id, style_id)
VALUES (1,2,3);

INSERT INTO Orders
(metal_id, size_id, style_id)
VALUES (2,2,2);

INSERT INTO Orders
(metal_id, size_id, style_id)
VALUES (3,2,1);

INSERT INTO Orders
(metal_id, size_id, style_id)
VALUES (1,1,1);

