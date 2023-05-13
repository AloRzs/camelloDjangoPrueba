

const producto1Valor = 2000;
const producto2Valor = 9000;
const producto3Valor = 4800;
const producto4Valor = 2000;
const producto5Valor = 2500;

function incremento(id){
    let i=0;
    i++;
    
    var cantidad= document.getElementById("cantidad"+id);

    cantidad.innerHTML=parseInt(cantidad.innerHTML)+i;

}

function decremento(id){

    var cantidad= document.getElementById("cantidad"+id);

    if (parseInt(cantidad.innerHTML)>0){
        cantidad.innerHTML=parseInt(cantidad.innerHTML)-1;
    }
    
}

function calcular(){
    var Total=0;
    var cantidad1=parseInt(document.getElementById("cantidad1").innerHTML);
    var cantidad2=parseInt(document.getElementById("cantidad2").innerHTML);
    var cantidad3=parseInt(document.getElementById("cantidad3").innerHTML);
    var cantidad4=parseInt(document.getElementById("cantidad4").innerHTML);
    var cantidad5=parseInt(document.getElementById("cantidad5").innerHTML);


    var valorSub1 =cantidad1*producto1Valor;
    var valorSub2 =cantidad2*producto2Valor;
    var valorSub3 =cantidad3*producto3Valor;
    var valorSub4 =cantidad4*producto4Valor;
    var valorSub5 =cantidad5*producto5Valor;


    Total+=valorSub1+valorSub2+valorSub3+valorSub4+valorSub5;


    
    document.getElementById("total").innerHTML=Total;

}






