const fs = require("fs");

const File = fs.readFileSync("./files/file.txt", "utf-8");

module.exports = File;
