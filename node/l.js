const fs = require("fs");
// var a = {
//   name: "naurangi lal",
//   mob: 9675329115,
//   address: {
//     curr_palace: "Duhai",
//     permanent_palace: "Saray Barahaman",
//     teh: "Gunnaur",
//     disstt: "Sambhal",
//   },
//   desti: "Full Stack Developre",
// };
function add(a, b) {
  return a + b;
}
function subtract(a, b) {
  return a - b;
}

const c = add(1, subtract(3, 2));
console.log(c);

fs.writeFile("fiLe.txt", "Hello I'm Learning Node.js", (err) => {
  if (err) throw err;
  console.log("File has been written.");
});
