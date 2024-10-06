const mongoose=require('mongoose')
const dotenv = require('dotenv');
dotenv.config({ path: './config.env' });
const app = require('./app');



mongoose.connect(process.env.MONGODB_URL, {
  useNewUrlParser: true,
  useCreateIndex:true,
  useUnifiedTopology:true,
  useFindAndModify:false
})
.then(()=>console.log('Connected to the database!'))



const port = process.env.PORT || 8000;
app.listen(port, () => {
  console.log(`App running on port http://localhost:${port}`);
});