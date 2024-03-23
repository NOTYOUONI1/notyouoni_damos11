/*for(let i = 1;i<101;i++){
    //console.log(i)
    if(i%2!==0)
        console.log(i)
}*/



//let o = prompt("gace number");
//let k = 25;

/*while(k != o){
    o = prompt("gace number");
}
console.log('Win')*/



/*let str = 'rakib';
let d = 'sakib'
let s = `raki` 

console.log(d[3])*/


/*let obj = {
    item: "pen",
    price: 10
}
let t = `item name is ${obj.item} item price is ${obj.price}`
console.log(t)

let d = "KING"
d = d.toLowerCase()
console.log(d)

let p = "abcdefg"
let l = p.concat(d)
console.log(l)

let u = "Hello"
u = u.replace('H','j')
console.log(u)

let y = prompt("Enter your FullName :")
let low = y.toLowerCase()
let username = '@'+low+y.length
console.log("your fullname",y,'\n',username)*/

/*let mask = ['rakib','sakib','maruf'];

for(let o = 0;o < mask.length;o++){
    console.log(mask[o])
}

for(let g of mask){
    console.log(g.toUpperCase())
}

for(let d of mask){
    console.log()
}

let num = [15,51,55,6,88,99,55,44,]
let sum = 0;
for(let j of num){
    sum += j
    console.log(j,sum,)
}
console.log('total number =',sum)

let df = [100,200,300,400,500,600,700,800]

for(let ok = 0;ok < df.length;ok++){
    offer = df[ok]/10 
    kl = df[ok] - offer
    console.log(df[ok],'is offer price',kl)
}*/

/*function dd (name){
    console.log('Hi',name)
}

dd ('rakib')

function sum(b,n){
    console.log(b+n)
}

let ff = (a,b)=>{
    return a+ b; 
}

let k = ff(6,8)

console.log(ff(2,5))

function en (str){
    let count = 0;
    for (const i of str){
        if(i == 'a' ||i == 'e'||i == 'i'||i == 'o'||i == 'u'){
            count ++;
        }
    }
    console.log(str,"vawel =",count)
}

en("aeiou")*/
/*
let va = (name)=>{
    let count = 0;
    for(let ta of name){
        if(ta == "a"||ta == "e"||ta == "i"||ta == "u"||ta == "o"){
            count ++;
        }
    }
    console.log(name, "vawul =",count)
}

va('rakibaa')

let arr = [1,2,3,4]
arr.forEach(function ff(val){
    console.log(val)
})

arr.forEach((val)=>{
    console.log(val)
})
*/

/*let dei = [1,2,3,4,5]
dei.forEach((dei) => {
    console.log(dei*dei)
})


let newarr = dei.map((val) => {
    return val*4;
})

console.log(newarr)*/

/*let fg = [1,2,3,4,5,6]
let even = fg.filter((val)=>{
    return val % 2 ==0;
})

console.log(even)*/

let ff = [1,2,3,4]

let outpot = ff.reduce((res,ff)=>{
    return res + ff
})

console.log(outpot)