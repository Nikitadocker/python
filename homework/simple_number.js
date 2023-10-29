
let start = 2;

let finish = 10;

let currentnumber = start;

pusk:
for (currentnumber >= start; currentnumber <= finish; currentnumber++) {

    let delitel = currentnumber;

    for (delitel >= start; delitel <= Math.sqrt(currentnumber); delitel++) {

        if (currentnumber % delitel == 0) {

            continue pusk; 

        }
         

         else print (currentnumber)



    }

}






