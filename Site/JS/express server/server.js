const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const app = express()
const port = 8000

let dataToSend;

app.use(cors())
app.use(bodyParser.json())
app.route('/calculated')
    .post((req, res) => {
        send = { message: 'post request for calculated page successful'};
        res.send(send)
        console.log(req.body)
        dataToSend = req.body;
    })
    .get((req,res) => {
        res.send("info")
    });

  app.listen(port, () => {
    console.log(`Server listening on port ${port}`)
  })