//********************   slider    ******************************************************** */
$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})






//******************** ajax for + - remove cart ******************************************* */
let pbtns=Array.from(document.querySelectorAll(".plus-cart"));
let mbtns=Array.from(document.querySelectorAll(".minus-cart"));
let rbtns=Array.from(document.querySelectorAll(".rbtn"));
let camt=document.querySelector("#camt");
let tot_amt=document.querySelector("#tot_amt");


const ajaxRequest=async(pid)=>
{
    
    const response=await fetch("/pluscart/?prod_id="+pid);
    const data=response.json()
    return data
}




pbtns.forEach((pbtn,index)=>
{
    pbtn.addEventListener("click",(e)=>
{

     let pid= pbtn.getAttribute('pid').toString();
    let qts=Array.from(document.querySelectorAll(".quantity"));
    

    ajaxRequest(pid).then((data)=>
    {
        qts[index].innerText=data.quantity;
        camt.innerText=data.amount;
        tot_amt.innerText=data.total_amount;

    }).catch((err)=>
    {
        console.error(err);
    })
})

});

//------------------------------ minus -----------------------------------------



const ajaxRequest1=async(pid)=>
{
    
    const response=await fetch("/minuscart/?prod_id="+pid);
    const data=response.json()
    return data
}




mbtns.forEach((mbtn,index)=>
{
    mbtn.addEventListener("click",(e)=>
{

    let pid= mbtn.getAttribute('pid').toString();
    let qts=Array.from(document.querySelectorAll(".quantity"));
    

    ajaxRequest1(pid).then((data)=>
    {
        
        qts[index].innerText=data.quantity;
        camt.innerText=data.amount;
        tot_amt.innerText=data.total_amount;

    }).catch((err)=>
    {
        
        console.error(err);
    })
})

});


//------------------------------ Remove cart -----------------------------------------



const ajaxRequest2=async(pid)=>
{
    
    const response=await fetch("/removecart/?prod_id="+pid);
    const data=response.json()
    return data
}

rbtns.forEach((rbtn,index)=>
{ 
    rbtn.addEventListener("click",(e)=>
{

    let pid= rbtn.getAttribute('pid').toString();
    console.log(rbtn.innerHTML);
    
    

    ajaxRequest2(pid).then((data)=>
    {

        let elm= e.target;
        
        console.log(elm.parentNode.parentNode.parentNode.parentNode.remove());
        
        
        camt.innerText=data.amount;
        tot_amt.innerText=data.total_amount;

    }).catch((err)=>
    {
        
        console.error(err);
    })
})

});













