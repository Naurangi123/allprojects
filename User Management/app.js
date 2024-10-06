const express = require("express");
const mongoose = require("mongoose");
const User = require("./models/user");

const app = express();
const dbURI = "mongodb://localhost:27017/employee_management";

mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    console.log("Database connected");
    app.listen(8080);

  })
  .catch((err) => console.log(err));

app.set("view engine", "ejs");

app.use(express.static("public"));
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.redirect("/users");
});

app.get("/users", (req, res) => {
  User.find().sort({ createdAt: -1 })
    .then((result) => {
      res.render("index", { users: result, title: "Home" });
    })
    .catch((err) => {
      console.log(err);
    });
});

app.get("/about", (req, res) => {
  res.render("about", { title: "About" });
});

app.get("/user/create", (req, res) => {
  res.render("adduser", { title: "Add-User" });
});

app.get("/users/:id", (req, res) => {
  const id = req.params.id;
  User.findById(id)
    .then((result) => {
      res.render("details", { user: result, action: "edit", title: "User Details" });
    })
    .catch((err) => {
      console.log(err);
    });
});

app.get("/edit/:name/:action", (req, res) => {
  const name = req.params.name;
  User.findOne({ name: name })
    .then((result) => {
      res.render("edit", { user: result, title: "Edit-User" });
    })
    .catch((err) => {
      console.log(err);
    });
});

app.post("/user/create", (req, res) => {
  const user = new User(req.body);
  user.save()
    .then(() => {
      res.redirect("/users");
    })
    .catch((err) => {
      console.log(err);
    });
});

app.post("/edit/:id", (req, res) => {
  User.updateOne({ _id: req.params.id }, req.body)
    .then(() => {
      res.redirect("/users");
      console.log("User profile updated");
    })
    .catch((err) => {
      console.log(err);
    });
});

app.post("/users/:name", (req, res) => {
  const name = req.params.name;
  User.deleteOne({ name: name })
    .then(() => {
      res.redirect("/users");
    })
    .catch((err) => {
      console.log(err);
    });
});

app.use((req, res) => {
  res.render("404", { title: "NotFound" });
});
