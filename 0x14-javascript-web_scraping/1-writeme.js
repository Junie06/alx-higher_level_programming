#!/usr/bin/node
// a script that writes data to a file
const fs = require('fs');

const file = process.argv[2];

fs.writeFile(file, process.argv[3], { flag: 'w' }, (err) => {
  if (err) {
    console.log(err);
  }
});
