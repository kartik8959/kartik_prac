const form=document.querySelector('form');


//---------------------------------password visiblity---------------------------------------------------
let visiblity=false;
const eye_ico=document.querySelector("#f_eye");
const id_password=document.querySelector("#id_password");
// console.log(id_password.innerHTML=="")
eye_ico.addEventListener("click",(e)=>
{
    if(!visiblity && id_password.value!="" )
    {
        id_password.attributes.type.value="text";
        eye_ico.classList.add("text-danger");
        if(eye_ico.classList.contains("text-muted"))
        {
            eye_ico.classList.replace("text-muted","text-danger");
        }
        visiblity=true;
    }
    else{
        id_password.attributes.type.value="password";
        eye_ico.classList.replace("text-danger","text-muted");
        visiblity=false;

    }


})




//=======================================UNIQUE USERNAME=================================================
const usernamefield=form.username;
const error_message = error_username.innerHTML;
console.log("***********************");
 
const ajaxRequest = async ()=>
{
    const response = await fetch('/institute/checkusername/?username='+usernamefield.value);
    return response.text();
}
const checkUsername=()=>
{
    if(result['username'])
    {
       
        ajaxRequest().then((data)=>
        {
            const help_username=document.querySelector('#help_username');
            const error_username=document.querySelector('#error_username');
            

           if(data==='True')
           {
              

            usernamefield.classList.replace("success","fail");
            help_username.classList.replace('show',"hide");
            error_username.classList.replace("hide","show");
            error_username.innerHTML="An account  already exist with given username";
            result['username']='false';
           }
        }).catch((error)=>
        {
            console.error("Failed");
        })

    }
   
};
usernamefield.addEventListener("blur",checkUsername);











//------------------------validation---------------------------------------------------------------------
const result={
    username:false,
    email:false,
    password:false,
    contact_no:false
};

form.addEventListener("submit",(e)=>
{
//    alert(result.username+" "+result.email+" " + result.password+ result.contact_no);
    if(result.username && result.email && result.password && result.contact_no)
        return true
    e.preventDefault();
    return false

});

const inputs = document.querySelectorAll("input");
const font_tag=document.querySelector(".fa");
const patterns={
username: /^[a-zA-Z\d@_]{5,20}$/,
email: /^([a-zA-Z\d\._]+)@([a-zA-Z\d]{2,})\.([a-zA-Z\d]{2,5})(\.[A-Za-z]{2,5})?$/,
password: /^[a-zA-Z\d@]{6,20}$/,
contact_no: /^[5-9][\d]{9}$/

};
function validate(field,pattern)
{
    let valid_field   =  document.querySelector("#help_"+field.attributes.name.value);
    let inValid_field =  document.querySelector("#error_"+field.attributes.name.value);
    // console.log(valid_field);
    // console.log(inValid_field);

    if(pattern.test(field.value))
    {
        field.classList.replace('fail','success');
        result[field.attributes.name.value]=true;
    }
    else{
        if(field.classList.contains('success'))
        {
            field.classList.replace('success','fail');
        }
        
        field.classList.add('fail');
        result[field.attributes.name.value]=false;
        

    }
}

function calc(field,pattern)
{
    let valid_field   =  document.querySelector("#help_"+field.attributes.name.value);
    let inValid_field =  document.querySelector("#error_"+field.attributes.name.value);
    if(pattern.test(field.value))
    {
        valid_field.classList.add('show');
        if(valid_field.classList.contains("hide"))
        {
            valid_field.classList.replace("hide",'show')

        }
        inValid_field.classList.replace('show','hide');
        

    }
    else{
        // valid_field.classList.replace("show",'hide');
        if(valid_field.classList.contains("show"))
        {
            valid_field.classList.replace("show",'hide');
        }
        inValid_field.classList.replace('hide','show');


        valid_field.classList.add('hide');
        // inValid_field.classList.add('show');
    }
}

inputs.forEach((input)=>
{
    input.addEventListener('keyup',(event)=>
    {
        let pattern=patterns[event.target.attributes.name.value];
        let field=event.target;
        if(field.attributes.name.value=='username')
        {
            // const error_username=document.querySelector('#error_username');
            error_username.innerHTML=error_message;
            
        }
        validate(field,pattern);
    input.addEventListener("blur",(e)=>
    {
        calc(field,pattern);
    });
        

    });

})




