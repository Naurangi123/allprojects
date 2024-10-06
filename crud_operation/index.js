
require('dotenv').config()
const express=require('express')
const mongoose=require('mongoose')
const session=require('express-session')
const app=express()
const data=require('./routes/routes')

const PORT=process.env.PORT || 3000;

//database connnection
mongoose.connect(process.env.MONGODB_URL, { useNewUrlParser: true,useUnifiedTopology:true });
const db = mongoose.connection;
db.on('error', (error) => {
    console.log('Error connecting to database:', error);
});

db.once('open', () => {
    console.log('Connected to the database!');
});

//MIddleware

app.use(express.urlencoded({extended:false}))
app.use(express.json())
app.use(session({
    secret:'my secert key',
    saveUninitialized:true,
    resave:false,
}))
app.use((req,res,next)=>{
    res.locals.message=req.session.message
    delete req.session.message
    next();

})

app.use(express.static('uploads'))
//set template engine
app.set('view engine',"ejs");

//routes prefix
app.use('',data)

app.listen(PORT,()=>{
    console.log(`port listen at http://localhost:${PORT}`)
})

