const express=require('express')
const User=require('../models/users')
const multer=require('multer')
const mongoose = require('mongoose')
const router=express.Router()
const fs=require("fs")
const users = require('../models/users')



var storage=multer.diskStorage({
    destination:function(req,file,next){
        next(null,'./uploads')
    },
    filename:function(req,file,next){
        next(null,file.fieldname+"_"+Date.now()+"_"+file.originalname);
    },
})

var upload=multer({
    storage:storage,
}).single("image")

//insert user in db

router.post('/add', upload, (req, res) => {
    const user = new User({
        name: req.body.name,
        email: req.body.email,
        phone: req.body.phone,
        image: req.file.filename,
    });
    user.save()
    .then(() => {
        req.session.message = {
            type: 'success',
            message: "User added successfully",
        };
        res.redirect("/");
    })
    .catch((err) => {
        req.session.message = {
            type: 'danger',
            message: 'Failed to add user: ' + err.message,
        };
    }); 
});

router.get('/', (req, res) => {
    User.find().exec()
    .then(users => {
        res.render('index', {
            title: "Home Page",
            users: users
        });
    })
    .catch(err => {
        res.json({ message: err.message });
    });
});


router.get('/add',(req,res)=>{
    res.render('add_users',{title:'Add Users'})
})
//Edit user
router.get('/edit/:id', (req, res) => {
    let id = req.params.id;
    User.findById(id)
    .then(user => {
        if (!user) {
            return res.status(404).render('error', { message: "User not found" });
        }
        res.render('edit_users', {
            title: "Edit Page",
            user: user // Pass user directly, not in an array
        });
    })
    .catch(err => {
        res.status(500).render('error', { message: err.message });
    });
});

//Update user route

router.post('/update/:id',upload,(req,res)=>{
    let id=req.params.id;
    let new_image='';

    if(req.file){
        new_image=req.file.filename;
        try {
            fs.unlinkSync('./uploads/'+req.body.old_image)
        } catch (err) {
            console.log(err)
        }
    }else{
        new_image=req.body.old_image;
    }
    User.findByIdAndUpdate(id,{
        name: req.body.name,
        email: req.body.email,
        phone: req.body.phone,
        image: new_image,
    })
    .then(result => {
        res.redirect("/");
    })
    .catch(err => {
        res.render('error', { message: err.message });
    });
})

//delete user
router.get('/delete/:id', (req, res) => {
    const id = req.params.id;

    User.findByIdAndDelete(id)
    .then(deletedUser => {
        if (!deletedUser) {
            return res.json({ message: 'User not found' });
        }
        req.session.message = { type: 'info', text: 'User deleted successfully' }; // Corrected the assignment
        res.redirect("/");
    })
    .catch(err => {
        res.json({ message: err.message });
    });
});


module.exports=router;