const submit_btn=document.querySelector('#submit_btn');
const check_otp=document.querySelector('#check_otp');
const sent_otp=document.querySelector("#sent_otp");
const id_contact=document.querySelector("#id_contact");
const otp_box=document.querySelector('#otp_box');
const details_form=document.querySelector('#details_form');

submit_btn.style.display="none";


details_form.addEventListener("submit",()=>
{
    id_contact.disabled=false;
    return true;
})


const sendOtp=async()=>
{
    response= await fetch("/sendotp/?contact_no="+id_contact.value);
    return response.text()

}

sent_otp.addEventListener("click",()=>
{
    id_contact.disabled=true;
    id_contact.style.cursor="not-allowed";
    id_contact.readOnly=true;
    id_contact.addEventListener("click",(e)=>
    {
        id_contact.blur();
    })
    
    
    sent_otp.style.display='none';
    otp_box.style.display='block';
    
    sendOtp().then((data)=>{
        console.log(data)
    }).catch((error)=>
    {
        console.log(error)
    })
})



//----------------check otp -----------------------------------
const id_otp=document.querySelector("#id_otp");
const checkOtp=async ()=>
{
    response= await fetch("/check_otp/?otp="+id_otp.value);
    return response.text()
}

check_otp.addEventListener("click",()=>
{
    checkOtp().then((data)=>
    {
        console.log(data);
        if(data=="True"){
            otp_box.style.display="none";
            submit_btn.style.display="inline";
        }



    }).catch((error)=>
    {
        console.error(error);

    }) 
})

