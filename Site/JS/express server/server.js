const express = require('express')
var bodyParser = require('body-parser')
var cors = require('cors')
const app = express()
const port = 8000

app.use(cors())
app.use(bodyParser.json())

app.post('/calculated', (req, res) => {

    send = {
        message: 'post request for calculated page successful',
    };
    res.send(JSON.stringify(send))
    console.log(req)
  })
  
  app.listen(port, () => {
    console.log(`Server listening on port ${port}`)
  })