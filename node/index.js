const calcArea = require("area-of-square");
const circleArea = require("./utils/area/circle");
const rectangleOfArea = require("./utils/area/rectangle");
const FileRead = require("./files/file");

const File = require("./files/file.txt");
const areaOfRectangle = rectangleOfArea(12, 12);
const Area = calcArea(400);
const Cier = circleArea(4);

// console.log("Area from index :", Area);
// console.log("it from rectanglesquare = ", areaOfRectangle);
// console.log("Circle Area:", Cier);
// console.log(FileRead);
// console.log(Data.address.curr_palace);
// console.log(Data.desti);
// console.log(Data.add(1, subtract(3, 2)));
